
from pyspark.sql import SparkSession

import re

spark = SparkSession.builder \
    .master('local[*]') \
    .appName('WordCount_RDD_GCS_Python') \
    .getOrCreate()
sc = spark.sparkContext

spark._jsc.hadoopConfiguration().set('google.cloud.auth.service.account.json.keyfile', '/home/to/your/credentials.json')

bucket_name = 'bucket_name'
input_file_name = '/textfile'
output_file_name = '/result'

input_file_path = 'gs://' + bucket_name + input_file_name
rdd = sc.textFile(input_file_path)
word_count_rdd = rdd.flatMap(lambda item: item.split(' ')) \
    .map(lambda item: re.sub(r'[^a-zA-Z]', '', item).lower()) \
    .filter(lambda item: item != '') \
    .map(lambda item: (item, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[1], ascending=False)
top10 = word_count_rdd.take(10)
print(top10)

output_file_path = 'gs://' + bucket_name + output_file_name
word_count_rdd.toDF().write.parquet(output_file_path)