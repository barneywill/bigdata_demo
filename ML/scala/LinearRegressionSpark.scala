import org.apache.spark._
import org.apache.spark.ml.regression.{LinearRegression, LinearRegressionModel}
import org.apache.spark.ml.feature.{StringIndexer, OneHotEncoder, VectorAssembler, VectorIndexer}
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.Pipeline


object LinearRegressionSpark {
    def main(args: Array[String]): Unit = {
        val spark = SparkSession.builder
            .master("local[*]")
            .appName("LinearRegressionSpark_Scala")
            .getOrCreate

        // 1 Data preparation
        val filePath = "file://" + args[0]
        var featureColumns = ["feature1", "feature2", "feature3", "featuren"]
        var labelColumn = "label"
        val categoricalColumns = ["cat1", "cat2", "cat3"]
        val df = spark.read.csv(filePath)

        // 2 Split train set and test set
        df_train, df_test = df.randomSplit([0.8, 0.2], seed=1)

        // 3 Train
        val indexers = categoricalColumns.map {colName => new StringIndexer().setInputCol(colName).setOutputCol(colName + "_indexed")}
        val encoders = indexers.map {indexer => new OneHotEncoder().setInputCol(indexer.getOutputCol).setOutputCol(indexer.getOutputCol + "_encoded")}
        val assembler = new VectorAssembler().setInputCols(featureColumns ++ encoders.map {encoder => encoder.getOutputCol}).setOutputCol("features").sethandleInvalid("skip")
        val featureIndexer = new VectorIndexer().setInputCol("features").setOutputCol("indexedFeatures").setMaxCategories(5)
        val lr = new LinearRegression().setLabelCol(labelColumn).setFeaturesCol("indexedFeatures").setRegParam(0.3)

        val pipeline = new Pipeline().setStages(indexers ++ encoders ++ Array(assembler, featureIndexer, lr))
        val model = pipeline.fit(df_train)
        val lrModel = model.stages.last.asInstanceOf[LinearRegressionModel]

        // Print the coefficients and intercept for linear regression
        println(s"Coefficients: ${lrModel.coefficients} Intercept: ${lrModel.intercept}")
        // Summarize the model over the training set and print out some metrics
        val trainingSummary = lrModel.summary
        println(s"numIterations: ${trainingSummary.totalIterations}")
        println(s"objectiveHistory: [${trainingSummary.objectiveHistory.mkString(",")}]")
        trainingSummary.residuals.show()
        println(s"RMSE: ${trainingSummary.rootMeanSquaredError}")
        println(s"r2: ${trainingSummary.r2}")

        // 4 Evaluate
        val predictions = model.transform(df_test)
        val evaluator = new RegressionEvaluator().setLabelCol(labelColumn).setPredictionCol("prediction").setMetricName("rmse")
        val rmse = evaluator.evaluate(predictions)
        println(s"Root Mean Squared Error (RMSE) on test data = $rmse")
    }
}