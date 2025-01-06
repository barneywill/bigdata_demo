# Iceberg

Iceberg is a high-performance format for huge analytic tables.

| |Index|
|---|---|
|1|[Hierarchy(Catalog, metadata, manifest list, manifest file, data file)](#hierarchy)|
|2|[Performance](#performance)|
|3|[Schema Evolution](#evolution)|
|4|[With Spark](#spark)|
|5|[Near Real-time Data Warehouse](#realtime)|
|6|[Iceberg on Cloud(GCP, AWS)](#cloud)|

![Iceberg Structure](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_structure.jpg)

## 1 <a id='hierarchy'></a>Hierarchy
track the data in the table at the file level
- metadata(json) -> snapshot -> manifest list(avro) -> manifest file(avro) -> data file(parquet)

### 1.1 Iceberg Catalog
where to find the current location of the current metadata pointer
- hdfs: a file called version-hint.text
- hive: a table property which stores the location of the current metadata file
- glue: AWS Glue
- jdbc: database

### 1.2 metadata(json)
metadata files store metadata about a table: the table’s schema, partition information, snapshots, and which snapshot is the current one.
- file path: database_name/table_name/metadata/v\*.metadata.json

![Iceberg metadata](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_metadata.jpg)
  
### 1.3 manifest list(avro)
manifest list is a list of manifest files.
- file path: database_name/table_name/metadata/snap-\*.avro

![Iceberg manifest list](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_manifest_list.jpg)

### 1.4 manifest file(avro)
manifest files track data files as well as additional details and statistics about each file.structure
- file path: database_name/table_name/metadata/\*.avro

![Iceberg manifest file](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_manifest_file.jpg)

### 1.5 data file(parquet, or others)
- file path: database_name/table_name/data/partition_name=pv/\*.parquet

<a href='https://github.com/barneywill/bigdata_demo/blob/main/Iceberg/parquet.md'>Parquet</a>

### 1.6 Benefits
- Snapshot isolation for transactions
- Faster planning and execution
  - statistics in manifest files
- Abstract the physical, expose a logical view
- All engines see changes immediately
- Event listeners
- Efficiently make smaller updates

## 2 <a id='performance'></a>Performance
- Watch out on the size of metadata, because each insert will copy and create a new metadata file.
- Avoid writing just a few records a time.
- Compaction, merge small files.
- Clarify the need of Time Travel, and expire useless snapshots as soon as possible.
- Keep track on garbage files.

## 3 <a id='evolution'></a>Schema Evolution
Iceberg schema updates are metadata changes, so no data files need to be rewritten to perform the update.
- ADD columns
- Drop columns
- Rename columns
- Update a column type
- Reorder columns
- Update partitions

## 4 <a id='spark'></a>With Spark

```
# jdk 11 or higher
https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz
# Put jars under $SPARK_HOME/jars
https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.7.1/iceberg-spark-runtime-3.5_2.12-1.7.1.jar
```

### spark-sql
<a href='https://github.com/barneywill/bigdata_demo/blob/main/Iceberg/iceberg_spark_sql.sql' target='_blank'>iceberg_spark_sql.sql</a>
```
# creates a path-based catalog named local for tables under $PWD/warehouse
# make sure there is not HADOOP_HOME or HIVE_HOME as environment variables
spark-sql --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
    --conf spark.sql.catalog.local=org.apache.iceberg.spark.SparkCatalog \
    --conf spark.sql.catalog.local.type=hadoop \
    --conf spark.sql.catalog.local.warehouse=$PWD/warehouse
```

### pyspark
<a href='https://github.com/barneywill/bigdata_demo/blob/main/Iceberg/iceberg_pyspark.py' target='_blank'>iceberg_pyspark.py</a>

### Structured Streaming
```
val df = spark.readStream
    .format("iceberg")
    .option("stream-from-timestamp", Long.toString(streamStartTimestamp))
    .load("database.table_name")
```

![iceberg folders and files](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_files.jpg)

## 5 <a id='realtime'></a>Near Real-time Data Warehouse
From Kafka+Flink to Iceberg+Flink

![Near Real-time Data Warehouse](https://github.com/barneywill/bigdata_demo/blob/main/imgs/realtime_data_warehouse.jpg)

## 6 <a id='cloud'></a>Iceberg on Cloud

### 6.1 GCP

![iceberg on gcp](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_gcp.jpg)

### 6.2 Bigquery Iceberg Table
```
CREATE TABLE dataset_name.table_name (
 column1 STRING,
 column2 INT64
)
WITH CONNECTION connection_name
OPTIONS (
 file_format = ‘PARQUET’,
 table_format = ‘ICEBERG’,
 storage_uri = ‘gs://your-bucket/path-to-data’
);
```

### 6.3 AWS

![iceberg on aws](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_aws.jpg)
