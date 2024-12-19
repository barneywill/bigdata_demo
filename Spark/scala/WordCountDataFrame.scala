import org.apache.spark._
import org.apache.spark.sql.functions._

object WordCountDataFrame {
    def main(args : Array[String]): Unit = {
        val spark = SparkSession.builder
            .master("local[*]")
            .appName("WordCount_DataFrame_Scala")
            .getOrCreate

        val filePath = "file://" + args[0]
        val df = spark.read.text(filePath)
        val top10 = df.withColumn("word", explode(split(col("value"), " ")))
            .select(regexp_replace(col("word"), "[^a-zA-Z]", "").alias("word_clean"))
            .select(lower(col("word_clean")).alias("word_clean_lower"))
            .where("word_clean_lower != ''")
            .groupBy("word_clean_lower")
            .count()
            .sort(desc("count"))
            .limit(10)

        top10.show
    }
}
