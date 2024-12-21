
import org.apache.spark._
import org.apache.spark.rdd._

object WordCountRDDGCS {
    def main(args : Array[String]) : Unit => {
        val sparkConf = new SparkConf()
            .setMaster("local[*]")
            .setAppName("WordCount_RDD_GCS_Scala")
            //choose one from the belowing
            //export GOOGLE_APPLICATION_CREDENTIALS=/home/to/your/credentials.json
            .set("GOOGLE_APPLICATION_CREDENTIALS", "/home/to/your/credentials.json")
        val sc = new SparkContext(sparkConf)
        
        val bucketName = args[0]
        val inputFileName = args[1]
        val outputFileName = args[2]
        val inputFilePath = "gs://" + bucketName + inputFileName
        val rdd = sc.textFile(inputFilePath)
        val word_count_rdd = rdd.flatMap(_.split(' '))
            .map(_.replaceAll("[^a-zA-Z]", "").toLowerCase)
            .filter(_ != "")
            .map((_, 1))
            .reduceByKey(_ + _)
            .sortBy(_._2, ascending=false)
        val top10 = word_count_rdd.take(10)

        top10.foreach(println)

        val outputFilePath = "gs://" + bucketName + outputFileName
        word_count_rdd.toDF().write.parquet(outputFilePath)
    }
}
