import scala.io.Source

/*
Word Count without Spark
 */
object WordCoundScala {
    def main(args : Array[String]): Unit = {
        val filePath = args[0]
        var lines = Source.fromFile(filePath).getLines.toArray
        lines.flatMap(_.split(" "))
            .map(_.replaceAll("[^a-zA-Z]", "").toLowerCase)
            .filter(_ != "")
            .map((_, 1))
            .groupBy(_._1)
            .map(_._2.reduce((v1, v2) => (v1._1, v1._2 + v2._2)))
            .toArray
            .sortWith(_._2 > _._2)
            .take(10)
            .foreach(println)
    }
}

