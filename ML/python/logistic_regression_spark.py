
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler, VectorIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder \
    .appName("LogisticRegressionSpark_Python") \
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
# for classification
#labelIndexer = StringIndexer(inputCol=label_column, outputCol="{0}_indexed".format(label_column))
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
lr = LogisticRegression(featuresCol='features', labelCol=label_column, regParam=0.001)
pipeline = Pipeline(stages=indexers + encoders + [assembler, featureIndexer, lr])
model = pipeline.fit(df_train)
lr_model = model.stages[-1]
lr_model.save('lr_model_classification')

# Print the coefficients and intercept for linear regression
print("Coefficients: %s" % str(lr_model.coefficients))
print("Intercept: %s" % str(lr_model.intercept))
# Summarize the model over the training set and print out some metrics
trainingSummary = lr_model.summary
print("numIterations: %d" % trainingSummary.totalIterations)
print("objectiveHistory: %s" % str(trainingSummary.objectiveHistory))
trainingSummary.residuals.show()
print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
print("r2: %f" % trainingSummary.r2)

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
