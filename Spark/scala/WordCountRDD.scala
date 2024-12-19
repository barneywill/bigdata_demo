import org.apache.spark._
import org.apache.spark.rdd._

object WordCountRDD {
    def main(args : Array[String]) : Unit => {
        val sparkConf = new SparkConf()
            .setMaster("local[*]")
            .setAppName("WordCount_RDD_Scala")
        val sc = SparkContext(sparkConf)

        val filePath = "file://" + args[0]
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
