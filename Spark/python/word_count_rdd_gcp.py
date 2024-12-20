
from pyspark.sql import SparkSession

import re

spark = SparkSession.builder \
    .master('local[*]') \
    .appName('WordCount_RDD_GCP_Python') \
    .getOrCreate()
sc = spark.sparkContext

spark._jsc.hadoopConfiguration().set('google.cloud.auth.service.account.json.keyfile', '/home/to/your/credentials.json')

bucket_name = 'bucket_name'
file_name = '/textfile'
file_path = 'gs://' + bucket_name + file_name
rdd = sc.textFile(file_path)
top10 = rdd.flatMap(lambda item: item.split(' ')) \
    .map(lambda item: re.sub(r'[^a-zA-Z]', '', item).lower()) \
    .filter(lambda item: item != '') \
    .map(lambda item: (item, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[1], ascending=False) \
    .take(10)
print(top10)