from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, regexp_replace, lower

spark = SparkSession.builder \
    .master('local[*]') \
    .appName('WordCount_DataFrame_Python') \
    .getOrCreate()

file_path = 'file://' + '/path/to/a/textfile'
df = spark.read.text(file_path)
top10 = df.withColumn('word', explode(split(col('value'), ' '))) \
    .select(regexp_replace('word', '[^a-zA-Z]', '').alias('word_clean')) \
    .select(lower('word_clean').alias('word_clean_lower')) \
    .where('word_clean_lower != ""') \
    .groupBy('word_clean_lower') \
    .count() \
    .sort('count', ascending=False) \
    .limit(10)
    
top10.show()
    
    