
import org.apache.spark._

// do this before running
//export GOOGLE_CLOUD_PROJECT=project_id
//export GOOGLE_APPLICATION_CREDENTIALS=/home/to/your/credentials.json

object WordCountSQLBigquery {
    def main(args : Array[String]): Unit = {
        val spark = SparkSession.builder
            .master("local[*]")
            .appName("WordCount_SQL_Bigquery_Scala")
            .getOrCreate
        //for writing
        val bucket = "bucket_name"
        spark.conf.set("temporaryGcsBucket", bucket)

        val tableName = "bigquery-public-data:samples.shakespeare"
        val df = spark.read.format("bigquery")
            .option("table", tableName)
            .load()
        df.createOrReplaceTempView("tmp_words")
        val wordCountDf = spark.sql("""
            select word, sum(word_count) as wc
            from tmp_words
            where word <> ''
            group by word
            order by wc desc 
        """)
        val top10 = wordCountDf.take(10)
        top10.foreach(println)

        wordCountDf.write.format("bigquery")
            .option("table", "ny_taxi_dbt.word_count")
            .save()
    }
}
