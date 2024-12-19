from pyspark.conf import SparkConf
from pyspark.context import SparkContext

import re

sparkConf = SparkConf().master('local[*]') \
    .appName('WordCount_RDD_Python')
sc = SparkContext(sparkConf)

file_path = 'file://' + '/path/to/a/textfile'
rdd = sc.textFile(file_path)
top10 = rdd.flatMap(lambda item: item.split(' ')) \
    .map(lambda item: re.sub(r'[^a-zA-Z]', '', item).lower()) \
    .filter(lambda item: item != '') \
    .map(lambda item: (item, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[1], ascending=False) \
    .take(10)
print(top10)