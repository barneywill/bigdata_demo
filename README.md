# A bigdata demo project

![bigdata demo](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bigdata_demo.jpg)

|Framework|Remarks|
|---|---|
|<a href='https://github.com/barneywill/bigdata_demo/tree/main/Prerequisite'>Prerequisite</a>|DBeaver, Docker, <a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/terraform'>Terraform</a>, <a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/linux.md'>Linux</a>, Python, VSCode, <a href='https://github.com/barneywill/bigdata_demo/blob/main/Prerequisite/theory.md'>Theory</a>|
|<a href='https://github.com/barneywill/bigdata_demo/tree/main/google_cloud'>Google Cloud Platform</a>|Cloud Storage, Bigquery, IMA, Cloud Composer, Dataproc, Kafka, Looker|
|<a href='https://github.com/barneywill/bigdata_demo/tree/main/dbt'>dbt</a>|macro, model, command(build, codegen, docs)|
|<a href='https://github.com/barneywill/bigdata_demo/tree/main/Airflow'>Airflow</a>|DAG, Google Cloud Dataproc Operators|
|<a href='https://github.com/barneywill/bigdata_demo/tree/main/Kafka'>Kafka</a>|Topic, Partition, Producer, Consumer, Consumer Group, Rebalance, Offset|
|<a href='https://github.com/barneywill/bigdata_demo/tree/main/Nifi'>Nifi</a>|Process Group, Processor, Parameter Context, Expression, State|
|<a href='https://github.com/barneywill/bigdata_demo/tree/main/Spark'>Spark</a>|<a href='https://github.com/barneywill/bigdata_demo/tree/main/Spark/python'>Word Count Codes</a>, Operations, Spark SQL, Structured Streaming, <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/scala'>ML</a>|
|<a href='https://github.com/barneywill/bigdata_demo/tree/main/Iceberg'>Iceberg</a>|
|<a href='https://github.com/barneywill/bigdata_demo/tree/main/ML'>Machine Learning</a>|<a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>Linear Regression</a>, <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>Logistic Regression</a>, <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>Decision Tree</a>, <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML/python'>XGBoost</a>|
|<a href='https://github.com/barneywill/bigdata_demo/tree/main/Clickhouse'>Clickhouse</a>|

## Architecture
![bigdata cloud](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bigdata_cloud.jpg)

## 1 <a href='https://github.com/barneywill/bigdata_demo/tree/main/Prerequisite'>Prerequisite</a>
### 1.1 DBeaver
For writing SQL on almost any databases, like:
- RDBMS: Mysql, Postgresql, Oracle, SQLServer, ...
- Open Source Big Data Frameworks: Hive, Spark, Clickhouse, Impala, Doris, Presto, ...
- No SQL: Redis, ElasticSearch, Cassandra, MongoDB, ...
- Cloud: Redshift, Athena, Bigquery, Databricks, Snowflake, ...
### 1.2 Docker
### 1.3 Terraform
### 1.4 Linux
### 1.5 Python
Just install anaconda, and get everything you need.
- Numpy, Pandas, scikit-learn, seaborn, matplotlib
- Jupyter Notebook
### 1.6 VSCode
For writing and running Python, Scala, Java, and connecting GitHub, Copilot, Jupyter Server, Remote Linux, Database, also forwarding port 
### 1.7 Theory
Data Warehouse, Dimensional Modeling

## 2 <a href='https://github.com/barneywill/bigdata_demo/tree/main/google_cloud'>Google Cloud Platform</a>
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

## 3 <a href='https://github.com/barneywill/bigdata_demo/tree/main/dbt'>DBT</a>
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

## 4 <a href='https://github.com/barneywill/bigdata_demo/tree/main/Airflow'>Airflow</a>
For: Ochestration, Workflow, Data Pipeline Management
### 4.1 DAG
- Directed Acyclic Graph: tasks, dependencies
### 4.2 webserver, scheduler, worker
### 4.3 Retry & Backfill
### 4.4 Google Cloud Dataproc Operators
- DataprocCreateClusterOperator, DataprocStartClusterOperator, DataprocStopClusterOperator, DataprocDeleteClusterOperator
- DataprocSubmitJobOperator, DataprocCreateBatchOperator

![dag](https://github.com/barneywill/bigdata_demo/blob/main/imgs/dag.jpg)

## 5 <a href='https://github.com/barneywill/bigdata_demo/tree/main/Kafka'>Kafka</a>
### 5.1 Broker, ISR
### 5.2 Topic, Partition
### 5.3 Producer, Consumer, Consumer Group, Rebalance, Offset

![kafka](https://github.com/barneywill/bigdata_demo/blob/main/imgs/apache_kafka.jpg)

## 6 <a href='https://github.com/barneywill/bigdata_demo/tree/main/Nifi'>Nifi</a>
For: Data Loading
### 6.1 Process Group, Processor
### 6.2 Parameter Context, Expression
### 6.3 Run Once, Clear State

![mysql_2_google_cloud_storage](https://github.com/barneywill/bigdata_demo/blob/main/imgs/mysql_2_google_cloud_storage.jpg)

## 7 <a href='https://github.com/barneywill/bigdata_demo/tree/main/Spark'>Spark</a>
For: Data Processing, batch or streaming, Machine Learning
### 7.1 Word Count
- By Python, Scala, Java
- By Spark RDD, Spark DataFrame, Spark SQL
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
### 7.5 Spark ML

![spark word count](https://github.com/barneywill/bigdata_demo/blob/main/imgs/spark_job.jpg)

## 8 <a href='https://github.com/barneywill/bigdata_demo/tree/main/Iceberg'>Iceberg</a>
For: Data Lake, Almost Realtime Data Warehouse, Parquet on any cloud storage
### 8.1 Iceberg on Google Cloud Storage

## 9 <a href='https://github.com/barneywill/bigdata_demo/tree/main/ML'>Machine Learning</a>
For: Prediction, Classification, Clustering, Recommendation, ...
### 9.1 Linear Regression
### 9.2 Logistic Regression
### 9.3 Decision Tree
### 9.4 XGBoost
### 9.5 tensorflow/serving
Serve ML model on docker

![xgboost](https://github.com/barneywill/bigdata_demo/blob/main/imgs/xgboost_model.jpg)

## 10 <a href='https://github.com/barneywill/bigdata_demo/tree/main/Clickhouse'>Clickhouse</a>

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