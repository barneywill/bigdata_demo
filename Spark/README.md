# Install
```
export JAVA_HOME=/path/to/jdk
export SPARK_HOME=/path/to/spark

#not necessary
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH
```

## GCS Connector Hadoop3

### Put it under $SPARK_HOME/jars
https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-latest-hadoop2.jar

## Spark Bigquery Connector

### Put it under $SPARK_HOME/jars
https://storage.googleapis.com/spark-lib/bigquery/spark-bigquery-latest_2.12.jar
https://repo1.maven.org/maven2/com/google/inject/guice/7.0.0/guice-7.0.0.jar

# Run

```
#scala
spark-shell

#python
pyspark

#sql
spark-sql

#submit jar or py
spark-submit
```

## Hello World: Word Count

![word count](https://github.com/barneywill/bigdata_demo/blob/main/imgs/word_count.jpg)

## Implementations of Word Count

| |Python|Scala|Java|
|---|---|---|---|
|Single Machine|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_python.py'>word_count_python.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountDataScala.scala'>WordCountScala.scala</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/java/WordCountJava.java'>WordCountJava.java</a>|
|Spark RDD|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_rdd.py'>word_count_rdd.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountDataRDD.scala'>WordCountRDD.scala</a>|
|Spark DataFrame|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_dataframe.py'>word_count_dataframe.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountDataFrame.scala'>WordCountDataFrame.scala</a>|
|Spark SQL|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_sql.py'>word_count_sql.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountSQL.scala'>WordCountSQL.scala</a>|
|Google Cloud|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_rdd_gcs.py'>word_count_rdd_gcs.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountRDDGCS.scala'>WordCountRDDGCS.scala</a>|
|Bigquery|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_sql_bigquery.py'>word_count_sql_bigquery.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountSQLBigquery.scala'>WordCountSQLBigquery.scala</a>|

![spark word count](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_job.jpg)

# Operations: Transformation & Actions

## RDD Operations

![spark operations](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_operations.jpg)

### RDD Transformations
#### Narrow Transformations

![spark narrow transformation](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_narrow_transformation.jpg)

#### Wide Transformations

![spark wide transformation](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_wide_transformation.jpg)

## DataFrame Operations

![dataframe operations](https://github.com/barneywill/bigdata_demo/blob/main/imgs/dataframe_operations.jpg)

# Internals

## Memory Management
- spark.memory.fraction
- spark.memory.storageFraction

## Partition, Shuffle
Pull based

![shuffle](https://github.com/barneywill/bigdata_demo/blob/main/imgs/shuffle.jpg)

## Join
- Broadcast Hash Join
- Shuffle Hash Join
- Shuffle Sort Merge Join
- Cartesian Join

## Sort

## Whole Stage Code Generation

## Vectorized Execution Engine

## Adaptive Query Execution

# Trouble Shooting
- Job and event timeline
- Long stages
- Slow stages
- Skew and spill

