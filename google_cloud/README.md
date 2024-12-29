# Google Cloud Platform

| |Index|
|---|---|
|1|[Comparison](#comparison)|
|2|[Bigquery Performance Optimization](#bigquery)|

## <a id='comparison'></a>1 Comparison

|Service|Amazon Web Services(AWS)|Microsoft Azure|Google Cloud Platform(GCP)|
|---|---|---|---|
|Market Share|32%|23%|9%|
|VM|EC2(Elastic Compute)|Azure Virtual Machine|Compute Engine|
|Container|AWS Batch|Azure Kubernetes Service(AKS)|Kubernetes Engine|
|Serverless Functions|AWS Lambda|Azure Function|Cloud Functions|
|RDBMS|AWS RDS|Azure SQL|Cloud SQL|
|NoSQL|DynamoDB|Azure Cosmos DB|Big Table|
|Object Storage|S3(Simple Storage Service)|Blob Storage|Cloud Storage|
|File Storage|Elastic File System|Azure File Storage|Google Filestore|
|Archive Storage|Glacier|Azure Archive Storage|Google Storage|
|Data Warehouse/Lake|Redshift|Azure Synapse Analytics|Bigquery|
|AI&ML|SegeMaker|Azure Machine Learning|Vertex AI, AutoML|
|BI|Quicksight|PowerBI|Looker|
|Airflow|MWAA(Amazon Managed Workflows for Apache Airflow)|Azure Data Factory Managed Airflow|Cloud Composer|
|Kafka|MSK(Amazon Managed Streaming for Kafka)|Azure Event Hubs|Google Cloud Managed Service for Apache Kafka|
|Hadoop/Spark|EMR(Elastic MapReduce)|Azure HDInsight|Dataproc|

## <a id='bigquery'></a>2 Bigqery Performance Optimization
- Reduce the amount of data to be processed by removing columns you don’t need from your queries.
- Prevent unnecessary data scanning by using WHERE conditions intelligently.
- Partitioning data sets by timestamp or a specific column value to scan only the relevant data sections.
- In JOIN operations, it is usually more efficient to put the smaller table on the left side.
- If possible, filter tables before performing a JOIN operation.
- Minimise the use of ORDER BY on large data sets.
- Avoid unnecessary column usage in GROUP BY operations.
- If possible, pre-summarise the data in another table and perform queries on this summarised data.Avoid unnecessary column usage in GROUP BY operations.
- Prevent unnecessary cost increases by monitoring your slot usage.
- Optimise performance and keep costs under control by adjusting the number of slots according to your workload.
- Examine query plans with EXPLAIN to identify potential bottlenecks and areas for optimisation.
- Break very large queries into smaller, manageable chunks.
- UDFs can degrade performance; use built-in functions when possible.
- Improve query performance by using reusable and optimised stored procedures.UDFs can degrade performance; use built-in functions when possible.
- Monitor query performance regularly and make improvements when necessary.
- As your data sets change or grow, adapt your queries to these changes.


### data source
https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/yellow
https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green
https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/misc
