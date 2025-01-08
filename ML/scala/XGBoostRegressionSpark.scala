
import org.apache.spark._
import org.apache.spark.ml.feature.{StringIndexer, OneHotEncoder, VectorAssembler, VectorIndexer}
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.Pipeline
import ml.dmlc.xgboost4j.scala.spark.XGBoostClassifier
import ml.dmlc.xgboost4j.scala.spark.XGBoostClassificationModel


object XGBoostRegressionSpark {
    def main(args: Array[String]): Unit = {
        val spark = SparkSession.builder
            .master("local[*]")
            .appName("XGBoostRegression_Spark_Scala")
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

        val xgbParam = Map("eta" -> 0.1f,
            "max_depth" -> 2,
            "objective" -> "multi:softprob",
            "num_class" -> 3)
        val xgbClassifier = new XGBoostClassifier(xgbParam).
            setNumRound(100).
            setNumWorkers(2).
            setFeaturesCol("indexedFeatures").
            setLabelCol(labelColumn)

        val pipeline = new Pipeline().setStages(indexers ++ encoders ++ Array(assembler, featureIndexer, xgbClassifier))
        val model = pipeline.fit(df_train)
        val xgboostModel = model.stages.last.asInstanceOf[XGBoostClassificationModel]
        xgboostModel.save("xgboostModel")

        xgboostModel.extractParamMap().toSeq.foreach(println)

        // 4 Evaluate
        val predictions = model.transform(df_test)
        val evaluator = new RegressionEvaluator().setLabelCol(labelColumn).setPredictionCol("prediction").setMetricName("rmse")
        val rmse = evaluator.evaluate(predictions)
        println(s"Root Mean Squared Error (RMSE) on test data = $rmse")

    }
}