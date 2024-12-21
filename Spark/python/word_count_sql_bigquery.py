
from pyspark.sql import SparkSession

# do this before running
#export GOOGLE_CLOUD_PROJECT=project_id
#export GOOGLE_APPLICATION_CREDENTIALS=/home/to/your/credentials.json

spark = SparkSession.builder \
    .master('local[*]') \
    .appName('WordCount_SQL_Bigquery_Python') \
    .getOrCreate()
#for writing
bucket = 'bucket_name'
spark.conf.set('temporaryGcsBucket', bucket)

table_name = 'bigquery-public-data:samples.shakespeare'
df = spark.read.format('bigquery') \
    .option('table', table_name) \
    .load()
df.createOrReplaceTempView("tmp_words")
word_count_df = spark.sql("""
    select word, sum(word_count) as wc
    from tmp_words
    where word <> ''
    group by word
    order by wc desc 
    """)
top10 = word_count_df.take(10)
print(top10)

word_count_df.write.format('bigquery') \
    .option('table', 'ny_taxi_dbt.word_count') \
    .save()