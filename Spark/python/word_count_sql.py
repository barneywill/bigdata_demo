from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master('local[*]') \
    .appName('WordCount_SQL_Python') \
    .getOrCreate()

file_path = 'file://' + '/path/to/a/textfile'
df = spark.read.text(file_path)
df.createOrReplaceTempView("tmp_words")
top10 = spark.sql("""
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
top10.show()