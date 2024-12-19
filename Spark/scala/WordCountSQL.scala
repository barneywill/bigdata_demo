import org.apache.spark._

object WordCountSQL {
    def main(args : Array[String]): Unit = {
        val spark = SparkSession.builder
            .master("local[*]")
            .appName("WordCount_SQL_Scala")
            .getOrCreate

        val filePath = "file://" + args[0]
        val df = spark.read.text(filePath)
        df.createOrReplaceTempView("tmp_words")
        val top10 = spark.sql("""
            select word_clean_lower, count(1) as wc
            from
            (
                select lower(regexp_replace(word, '[^a-zA-Z]', '')) as word_clean_lower
                from tmp_words lateral view explode(split(value, ' ')) as word 
            ) a
            where word_clean_lower <> ''
            group by word_clean_lower
            order by wc desc
            limit 10
        """)

        top10.show
    }
}
