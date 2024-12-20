
import org.apache.spark._
import org.apache.spark.rdd._

object WordCountRDDGCP {
    def main(args : Array[String]) : Unit => {
        val sparkConf = new SparkConf()
            .setMaster("local[*]")
            .setAppName("WordCount_RDD_GCP_Scala")
            //choose one from the belowing
            //export GOOGLE_APPLICATION_CREDENTIALS=/home/to/your/credentials.json
            .set("GOOGLE_APPLICATION_CREDENTIALS", "/home/to/your/credentials.json")
        val sc = spark.sparkContext
        
        val bucketName = args[0]
        val fileName = args[1]
        val filePath = "gs://" + bucketName + fileName
        val rdd = sc.textFile(filePath)
        val top10 = rdd.flatMap(_.split(' '))
            .map(_.replaceAll("[^a-zA-Z]", "").toLowerCase)
            .filter(_ != "")
            .map((_, 1))
            .reduceByKey(_ + _)
            .sortBy(_._2, ascending=false)
            .take(10)

        top10.foreach(println)
    }
}
