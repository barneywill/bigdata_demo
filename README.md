# A bigdata demo project

## 1 Prerequisite
### 1.1 DBeaver
For writing SQL on almost any databases, like:
- RDBMS: Mysql, Postgresql, Oracle, SQLServer
- Open Source Big Data Frameworks: Hive, Spark, Clickhouse, Impala, Doris, Presto
- No SQL: Redis, ElasticSearch, Cassandra, MongoDB
- Cloud: Redshift, Athena, Bigquery, Databricks, Snowflake
### 1.2 Docker
### 1.3 Python
Just install anaconda, and you get everything you need.

## 2 <a href='https://github.com/barneywill/bigdata_demo/tree/main/google_cloud'>Google Cloud Platform</a>
For: Data Storage, Data Warehouse, BI
### 2.1 Google Cloud Storage
### 2.2 Google Bigquery
Data Warehouse, Best Practice, free bigdata-public-data on marketplace
### 2.3 Service Account
Connect from remote
### 2.4 Programming
Use Python and Service Account to read and write Google Cloud Storage and Bigquery
### 2.5 Cloud Composer
Based on Airflow
### 2.6 Looker
BI with Bigquery, showing line, bar, pie, map, ...

![looker](https://github.com/barneywill/bigdata_demo/blob/main/imgs/looker.jpg)

## 3 <a href='https://github.com/barneywill/bigdata_demo/tree/main/dbt'>DBT</a>
For: Dimensional Modeling, Layers, Development(transparent to cloud platform), Data Validation, Data Assets and Lineage, CI/CD
### 3.1 profiles.yml 
With Bigquery
### 3.2 packages.yml
dbt_utils
### 3.3 macros
UDF
### 3.4 models
Layer: staging, ods, dwd, dim, dws
### 3.5 dbt build
### 3.6 test
Data Validation
### 3.7 codegen
Avoid hand coding
### 3.8 dbt docs generate/serve
Data Assets & Lineage
### 3.9 CI/CD
Github pull request, webhook

![Data Warehouse Layers](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bigquery_dataset_structure.jpg)

## 4 <a href='https://github.com/barneywill/bigdata_demo/tree/main/Airflow'>Airflow</a>
For: Ochestration, Workflow, Data Pipeline Management
### 4.1 DAG
Directed Acyclic Graph: tasks, dependencies
### 4.2 Retry & Backfill

![dag](https://github.com/barneywill/bigdata_demo/blob/main/imgs/dag.jpg)

## 5 Nifi
For: Data Loading

## 6 <a href='https://github.com/barneywill/bigdata_demo/tree/main/Spark'>Spark</a>
For: Data Processing, batch or streaming, Machine Learning
### 6.1 Spark on GCP

## 7 Iceberg

## 8 Machine Learning
For: Prediction, Classification, Clustering, Recommendation, ...
### 8.1 Spark ML
### 8.2 XGBoost
### 8.3 tensorflow/serving
Serve ML model on docker

## 9 Other
### 9.1 AWS
#### 9.1.1 Redshit 
Based on Postgresql
#### 9.1.2 Athena
Based on Presto
### 9.2 Databricks vs Snowflake