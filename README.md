# bigdata_demo
A bigdata demo project

## 1 <a href='https://github.com/barneywill/bigdata_demo/tree/main/google_cloud'>Google Cloud Platform</a>
For: Data Storage, Data Warehouse, BI
### 1.1 Google Cloud Storage
### 1.2 Google Bigquery
Data Warehouse, Best Practice, free bigdata-public-data on marketplace
### 1.3 Service Account
Connect from remote
### 1.4 Programming
Use Python and Service Account to read and write Google Cloud Storage and Bigquery
### 1.5 Cloud Composer
Based on Airflow
### 1.6 Looker
BI with Bigquery, showing line, bar, pie, map, ...

![looker](https://github.com/barneywill/bigdata_demo/blob/main/imgs/looker.jpg)

## 2 <a href='https://github.com/barneywill/bigdata_demo/tree/main/dbt'>DBT</a>
For: Dimensional Modeling, Layers, Development(transparent to cloud platform), Data Validation, Data Assets and Lineage, CI/CD
### 2.1 profiles.yml 
With Bigquery
### 2.2 packages.yml
dbt_utils
### 2.3 macros
UDF
### 2.4 models
Layer: staging, ods, dwd, dim, dws
### 2.5 dbt build
### 2.6 test
Data Validation
### 2.7 codegen
Avoid hand coding
### 2.8 dbt docs generate/serve
Data Assets & Lineage
### 2.9 CI/CD
Github pull request, webhook

![Data Warehouse Layers](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bigquery_dataset_structure.jpg)

## 3 <a href='https://github.com/barneywill/bigdata_demo/tree/main/Airflow'>Airflow</a>
For: Ochestration
### 3.1 DAG
Directed Acyclic Graph: tasks, dependencies

## 4 Nifi
For: Data Loading

## 5 Spark
For: Data Processing

## 6 Machine Learning
For: Prediction, Classification, Clustering, Recommendation, ...
### 6.1 XGBoost
### 6.2 tensorflow/serving
Serve ML model on docker

## 7 Other
### 7.1 AWS
#### 7.1.1 Redshit 
Based on Postgresql
#### 7.1.2 Athena
Based on Presto
### 7.2 Databricks vs Snowflake