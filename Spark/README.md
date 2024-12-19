Apache Spark

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
|Python|word_count_python.py|word_count_rdd.py|word_count_dataframe.py|word_count_sql.py| |
|Scala|WordCountScala.scala|WordCountRDD.scala|WordCountDataFrame.scala|WordCountSQL.scala| |
