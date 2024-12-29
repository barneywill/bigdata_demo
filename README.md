# A Bigdata Demo Project

![bigdata demo](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bigdata_demo.jpg)

| |Category|Content|
|---|---|---|
|1|[Prerequisite](#prerequisite)|DBeaver, Docker, <a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/terraform'>Terraform</a>, <a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/linux.md'>Linux</a>, <a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/mysql.md'>Mysql</a>, Python, VSCode, JVM, <a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/methodology.md'>Methodology</a>|
|2|[Google Cloud Platform](#gcp)|Cloud Storage, Bigquery, IMA, Cloud Composer, Dataproc, Kafka, Looker|
|3|[dbt](#dbt)|macro, model, command(build, codegen, docs)|
|4|[Airflow](#airflow)|DAG, Google Cloud Dataproc Operators|
|5|[Kafka](#kafka)|Topic, Partition, Producer, Consumer, Consumer Group, Rebalance, Offset|
|6|[Nifi](#nifi)|Process Group, Processor, Parameter Context, Expression, State|
|7|[Spark](#spark)|<a href='https://github.com/barneywill/bigdata_demo/tree/main/Spark/python'>Word Count Codes</a>, Operations, Spark SQL, Structured Streaming, <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/scala'>ML</a>|
|8|[Iceberg](#iceberg)|Parquet|
|9|[Machine Learning](#ml)|<a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>Linear Regression</a>, <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>Logistic Regression</a>, <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>Decision Tree</a>, <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>XGBoost</a>|
|10|[Clickhouse](#clickhouse)|SSB|

## Architecture
![bigdata cloud](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bigdata_cloud.jpg)

## 1 <a id='prerequisite' href='https://github.com/barneywill/bigdata_demo/tree/main/Prerequisite'>Prerequisite</a>
### 1.1 DBeaver
For writing SQL on almost any databases, like:
### 1.2 Docker
### 1.3 <a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/terraform'>Terraform</a>
For allocating and destroying cloud resources any time easily.
### 1.4 <a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/linux.md'>Linux</a>
### 1.5 <a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/mysql.md'>Mysql</a>
### 1.6 Python
Just install anaconda, and get everything you need.
### 1.7 VSCode
For writing and running Python, Scala, Java, and connecting GitHub, Copilot, Jupyter Server, Remote Linux, Database, also forwarding port 
### 1.8 <a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/methodology.md'>Methodology</a>
Data Warehouse, Kimball's Dimensional Data Modeling

## 2 <a id='gcp' href='https://github.com/barneywill/bigdata_demo/tree/main/google_cloud'>Google Cloud Platform</a>
For: Data Storage, Data Warehouse, BI
### 2.1 Google Cloud Storage
- Bucket, Object
### 2.2 Google Bigquery
- Data Warehouse
- Best Practice
- Explain Plans: Performance Optimization
- Externally Partitioned Tables
- Iceberg Tables
- Machine Learning
- Free bigdata-public-data on marketplace, free big data sources to play with

![big query dataset](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bigquery_dataset_structure.jpg)

### 2.3 IAM, Service Account
- Connect from remote, Permission control
### 2.4 Programming
- Use Python and Service Account to read and write Google Cloud Storage and Bigquery
### 2.5 Cloud Composer
- Based on Airflow
### 2.6 Dataproc
- Spark on GCP
- GCS Connector Hadoop3, Spark Bigquery Connector
### 2.7 Google Cloud Managed Service for Apache Kafka
### 2.8 Looker
- BI with Bigquery, showing lines, bars, pies, maps, ...

![looker](https://github.com/barneywill/bigdata_demo/blob/main/imgs/looker.jpg)

## 3 <a id='dbt' href='https://github.com/barneywill/bigdata_demo/tree/main/dbt'>DBT</a>
For: Dimensional Modeling, Layers, Development(transparent to cloud platform), Data Validation, Data Assets and Lineage, CI/CD
### 3.1 profiles.yml 
- With Bigquery
### 3.2 packages.yml
- dbt_utils
### 3.3 macros
- UDF
### 3.4 models
- Layer: staging, ods, dwd, dim, dws
### 3.5 dbt build
### 3.6 test
- Data Validation
### 3.7 codegen
- Avoid hand coding
### 3.8 dbt docs generate/serve
- Data Assets & Lineage
### 3.9 CI/CD
- Github pull request, webhook

![dbt layers](https://github.com/barneywill/bigdata_demo/blob/main/imgs/dbt.jpg)

## 4 <a id='airflow' href='https://github.com/barneywill/bigdata_demo/tree/main/Airflow'>Airflow</a>
For: Ochestration, Workflow, Data Pipeline Management
### 4.1 DAG
- Directed Acyclic Graph: tasks, dependencies
### 4.2 webserver, scheduler, worker
### 4.3 Retry & Backfill
### 4.4 Google Cloud Dataproc Operators
- DataprocCreateClusterOperator, DataprocStartClusterOperator, DataprocStopClusterOperator, DataprocDeleteClusterOperator
- DataprocSubmitJobOperator, DataprocCreateBatchOperator

![dag](https://github.com/barneywill/bigdata_demo/blob/main/imgs/dag.jpg)

## 5 <a id='kafka' href='https://github.com/barneywill/bigdata_demo/tree/main/Kafka'>Kafka</a>
### 5.1 Broker, ISR
### 5.2 Topic, Partition
### 5.3 Producer, Consumer, Consumer Group, Rebalance, Offset

![kafka](https://github.com/barneywill/bigdata_demo/blob/main/imgs/apache_kafka.jpg)

## 6 <a id='nifi' href='https://github.com/barneywill/bigdata_demo/tree/main/Nifi'>Nifi</a>
For: Data Loading
### 6.1 Process Group, Processor
### 6.2 Parameter Context, Expression
### 6.3 Run Once, Clear State

![mysql_2_google_cloud_storage](https://github.com/barneywill/bigdata_demo/blob/main/imgs/mysql_2_google_cloud_storage.jpg)

## 7 <a id='spark' href='https://github.com/barneywill/bigdata_demo/tree/main/Spark'>Spark</a>
For: Data Processing, batch or streaming, Machine Learning
### 7.1 <a href='https://github.com/barneywill/bigdata_demo/tree/main/Spark/python'>Word Count</a>

| |Python|Scala|Java|
|---|---|---|---|
|Single Machine|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_python.py'>word_count_python.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountDataScala.scala'>WordCountScala.scala</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/java/WordCountJava.java'>WordCountJava.java</a>|
|Spark RDD|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_rdd.py'>word_count_rdd.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountDataRDD.scala'>WordCountRDD.scala</a>|
|Spark DataFrame|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_dataframe.py'>word_count_dataframe.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountDataFrame.scala'>WordCountDataFrame.scala</a>|
|Spark SQL|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_sql.py'>word_count_sql.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountSQL.scala'>WordCountSQL.scala</a>|
|Google Cloud|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_rdd_gcs.py'>word_count_rdd_gcs.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountRDDGCS.scala'>WordCountRDDGCS.scala</a>|
|Bigquery|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/python/word_count_sql_bigquery.py'>word_count_sql_bigquery.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/Spark/scala/WordCountSQLBigquery.scala'>WordCountSQLBigquery.scala</a>|

### 7.2 Operations
- RDD vs DataFrame
- Transformations, Actions
- Shuffle, Join
### 7.3 Spark SQL
- Parser-Analyzer-Optimizer-Planner
- Logical Plan, Physical Plan
- UDF
### 7.4 Structured Streaming
- Micro Batch Processing
- Continuous Processing
- State Store
### 7.5 <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/scala'>Spark ML</a>

![spark word count](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_job.jpg)

## 8 <a id='iceberg' href='https://github.com/barneywill/bigdata_demo/tree/main/Iceberg'>Iceberg</a>
For: Data Lake, Almost Realtime Data Warehouse, Parquet on any cloud storage
### 8.1 Parquet
### 8.2 Iceberg on Google Cloud Storage

## 9 <a id='ml' href='https://github.com/barneywill/bigdata_demo/tree/main/ML'>Machine Learning</a>
For: Prediction, Classification, Clustering, Recommendation, ...

| |Linear Regression|Logistic Regression|Decision Tree|XGBoost|
|---|---|---|---|---|
|Single Machine|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/linear_regression_python.py'>linear_regression_python.py</a>| |
|scikit-learn|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/linear_regression_scikit.py'>linear_regression_scikit.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/logistic_regression_scikit.py'>logistic_regression_scikit.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/decision_tree_regression_scikit.py'>decision_tree_regression_scikit.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/decision_tree_classification_scikit.py'>decision_tree_classification_scikit.py</a>
|XGBoost| | | |<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/xgboost_regression.py'>xgboost_regression.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/xgboost_classification.py'>xgboost_classification.py</a>|
|Spark|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/linear_regression_spark.py'>linear_regression_spark.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/scala/LinearRegressionSpark.scala'>LinearRegressionSpark.scala</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/logistic_regression_spark.py'>logistic_regression_spark.py</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/decision_tree_regression_spark.py'>decision_teer_regression_spark.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/decision_tree_classification_spark.py'>decision_teer_classification_spark.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/scala/DecisionTreeClassificationSpark.scala'>DecisionTreeClassificationSpark.scala</a>|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/xgboost_regression_spark.py'>xgboost_regression_spark.py</a><br><a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/python/xgboost_classification_spark.py'>xgboost_classification_spark.py</a>|
|Bigquery|<a href='https://github.com/barneywill/bigdata_demo/blob/main/ML/bigquery/linear_regression_bigquery.sql'>linear_regression_bigquery.sql</a>|

### 9.1 <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>Linear Regression</a>
### 9.2 <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>Logistic Regression</a>
### 9.3 <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>Decision Tree</a>
### 9.4 <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>XGBoost</a>
### 9.5 tensorflow/serving
Serve ML model on docker

![xgboost](https://github.com/barneywill/bigdata_demo/blob/main/imgs/xgboost_model.jpg)

## 10 <a id='clickhouse' href='https://github.com/barneywill/bigdata_demo/tree/main/Clickhouse'>Clickhouse</a>

## 11 Other
### 11.1 AWS
#### 11.1.1 Redshit 
Based on Postgresql
#### 11.1.2 Athena
Based on Presto
### 11.2 Databrics

### 11.3 Databricks vs Snowflake

Thanks for:
[data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)
[machine-learning-zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp)