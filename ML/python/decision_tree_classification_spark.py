
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler, VectorIndexer, StringIndexerModel, IndexToString
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder \
    .appName("DecisionTreeClassificationSpark_Python") \
    .getOrCreate()

# 1 Data preparation
file_path = 'file://' + '/path/to/a/csvfile'
feature_columns = ['feature1', 'feature2', 'feature3', 'featuren']
label_column = 'label'
categorical_columns = ['cat1', 'cat2', 'catn']
df = spark.read.csv(file_path, header=True, inferSchema=True)

# 2 Split train set and test set
df_train, df_test = df.randomSplit([0.8, 0.2], seed=1)

# 3 Train
# if your label column is not numerical, you need to encode it
labelIndexer = StringIndexer(inputCol=label_column, outputCol="indexedLabel").fit(df_train)
labelIndexer.save('labelIndexer')
indexers = [
    StringIndexer(inputCol=c, outputCol="{0}_indexed".format(c))
    for c in categorical_columns
]
encoders = [
    OneHotEncoder(dropLast=False,inputCol=indexer.getOutputCol(), outputCol="{0}_encoded".format(indexer.getOutputCol())) 
    for indexer in indexers
]
assembler = VectorAssembler(inputCols=feature_columns + [encoder.getOutputCol() for encoder in encoders], outputCol='features', handleInvalid='skip')
featureIndexer = VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=5)
dt = DecisionTreeClassifier(featuresCol='indexedFeatures', labelCol="indexedLabel", maxDepth=3)
pipeline = Pipeline(stages=[labelIndexer] + indexers + encoders + [assembler, featureIndexer, dt])
model = pipeline.fit(df_train)
dt_model = model.stages[-1]
dt_model.save('dt_model_classification')

# Show feature importance
feature_importance = dt_model.featureImportances.toArray()
for i, column in enumerate(assembler.getInputCols()):
    print(f"Feature '{column}': {feature_importance[i]:.2f}")
# Visualize the decision tree
print(dt_model.toDebugString)

# 4 Evaluation
predictions = model.transform(df_test)
# AUC-ROC
evaluator = BinaryClassificationEvaluator(labelCol=label_column, rawPredictionCol="rawPrediction")
auc = evaluator.evaluate(predictions)
print(f"AUC-ROC: {auc:.4f}")
# Accuracy, Precision, and Recall
multi_evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction")
accuracy = multi_evaluator.evaluate(predictions, {multi_evaluator.metricName: "accuracy"})
precision = multi_evaluator.evaluate(predictions, {multi_evaluator.metricName: "weightedPrecision"})
recall = multi_evaluator.evaluate(predictions, {multi_evaluator.metricName: "weightedRecall"})
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")

# 5 Convert the prediction back to label
loaded_model = StringIndexerModel.load('labelIndexer')
label_converter = IndexToString(inputCol="prediction", outputCol="predictedLabel", labels=loaded_model.labels)
predictions_with_label = label_converter.transform(predictions)