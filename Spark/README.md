# Install
```
export JAVA_HOME=/path/to/jdk
export SPARK_HOME=/path/to/spark

#not necessary
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH
```

# Run Word Count

```
#scala
spark-shell

#python
pyspark

#jar
spark-submit
```

## Implementations

|Language|Single Machine|Spark RDD|Spark DataFrame|Spark SQL|Google Cloud|
|---|---|---|---|---|---|
|Python|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_python.py'>word_count_python.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_rdd.py'>word_count_rdd.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_dataframe.py'>word_count_dataframe.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_sql.py'>word_count_sql.py</a>| |
|Scala|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountDataScala.scala'>WordCountScala.scala</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountDataRDD.scala'>WordCountRDD.scala</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountDataFrame.scala'>WordCountDataFrame.scala</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountSQL.scala'>WordCountSQL.scala</a>| |
|Java|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/java/WordCountJava.java'>WordCountJava.java</a>| | | | |

![spark word count](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_job.jpg)