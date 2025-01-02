# Spark

Apache Spark is a unified analytics engine for large-scale data processing.

| |Index|
|---|---|
|1|[Install](#install)|
|2|[Run](#run)|
|3|[Hello World: Word Count](#wordcount)|
|4|[Structured Streaming](#streaming)|
|5|[Operations: Transformation & Actions](#operation)|
|6|[Spark SQL](#sql)|
|7|[Internals](#internal)|
|8|[Trouble Shooting](#trouble)|

![spark execution](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_execution.jpg)

## <a id='install'></a>1 Install
```
export JAVA_HOME=/path/to/jdk
export SPARK_HOME=/path/to/spark

#not necessary
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH
```

### GCS Connector Hadoop3

#### Put it under $SPARK_HOME/jars
https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-latest-hadoop2.jar

### Spark Bigquery Connector

#### Put it under $SPARK_HOME/jars
https://storage.googleapis.com/spark-lib/bigquery/spark-bigquery-latest_2.12.jar
https://repo1.maven.org/maven2/com/google/inject/guice/7.0.0/guice-7.0.0.jar

## <a id='run'></a>2 Run

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

## <a id='wordcount'></a>3 Hello World: Word Count

![word count](https://github.com/barneywill/bigdata_demo/blob/main/imgs/word_count.jpg)

#### Implementations of Word Count

| |Python|Scala|Java|
|---|---|---|---|
|Single Machine|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_python.py'>word_count_python.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountDataScala.scala'>WordCountScala.scala</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/java/WordCountJava.java'>WordCountJava.java</a>|
|Spark RDD|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_rdd.py'>word_count_rdd.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountRDD.scala'>WordCountRDD.scala</a>|
|Spark DataFrame|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_dataframe.py'>word_count_dataframe.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountDataFrame.scala'>WordCountDataFrame.scala</a>|
|Spark SQL|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_sql.py'>word_count_sql.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountSQL.scala'>WordCountSQL.scala</a>|
|Google Cloud Storage|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_rdd_gcs.py'>word_count_rdd_gcs.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountRDDGCS.scala'>WordCountRDDGCS.scala</a>|
|Bigquery|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_sql_bigquery.py'>word_count_sql_bigquery.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountSQLBigquery.scala'>WordCountSQLBigquery.scala</a>|

![spark word count](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_job.jpg)

## <a id='streaming'></a>4 Structured Streaming
- Micro Batch Processing: 100ms exactly-once
- Continuous Processing: 1ms at-least-once
- State Store: State store is a versioned key-value store which provides both read and write operations.

```
# Put jars under $SPARK_HOME/jars
https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.4/spark-sql-kafka-0-10_2.12-3.5.4.jar
https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.5.2/kafka-clients-3.5.2.jar
https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10_2.12/3.5.4/spark-streaming-kafka-0-10_2.12-3.5.4.jar
https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.5.4/spark-token-provider-kafka-0-10_2.12-3.5.4.jar
https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.12.0/commons-pool2-2.12.0.jar
```

## <a id='operation'></a>5 Operations: Transformation & Actions

### 5.1 RDD Operations

![spark operations](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_operations.jpg)

#### RDD Transformations
##### Narrow Transformations

![spark narrow transformation](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_narrow_transformation.jpg)

##### Wide Transformations

![spark wide transformation](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_wide_transformation.jpg)

### 5.2 DataFrame Operations

![dataframe operations](https://github.com/barneywill/bigdata_demo/blob/main/imgs/dataframe_operations.jpg)

## <a id='sql'></a>6 Spark SQL
- Parser-Analyzer-Optimizer-Planner
  - Logical Plan: Scan/Filter/Join/Aggregate
  - Physical Plan: BroadcastExchange/BroadcastHashJoin/HashAggregate/ShuffleExchange
- UDF

## <a id='internal'></a>7 Internals

### Job Execution
- Job -> Stages -> Tasks

![Spark Job Stage Tasks](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_job_stage_task.jpg)

### Executor Memory Management
- Execution
- Storage: RDD Data, Cache
- Parameters
  - spark.memory.fraction: default 0.6
  - spark.memory.storageFraction: default 0.5

![Spark Memory Management](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_memory.jpg)

### Partition, Shuffle
Pull based

![shuffle](https://github.com/barneywill/bigdata_demo/blob/main/imgs/shuffle.jpg)

### Join
- Broadcast Hash Join: spark.sql.autoBroadcastJoinThreshold
  - No shuffle
- Shuffle Hash Join
  - Shuffle based on join keys
- Shuffle Sort Merge Join: spark.sql.join.preferSortMergeJoin
  - Shuffle based on join keys which are also sorted
- Cartesian Join

### Cache, Persist, Checkpoint
- Cache: Memory only
- Persist: Different Storage Levels
- Checkpoint: Disk Only, can restore after restarting

![Storage Levels](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_storage_level.jpg)

### Sort

### Whole Stage Code Generation, since version 2
- volcano iterator model
- WholeStageCodegenExe

### Vectorized Execution Engine, since version 3
- SMID: Single Instruction, Multiple Data

![smid](https://github.com/barneywill/bigdata_demo/blob/main/imgs/simd.jpg)

### Adaptive Query Execution, since version 3

## <a id='trouble'></a>8 Trouble Shooting
Spark UI
- Job and event timeline
  - failing jobs/executors
  - gaps in execution
  - long jobs
  - many small jobs
- Long stages
  - io details
    - high input, high output, high shuffle
  - number of tasks
- Slow stages
  - read/write a lot of small files
  - slow udf
  - cartesian join
  - exploding join
- Skew and spill

