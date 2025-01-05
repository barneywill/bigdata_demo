# Iceberg

Iceberg is a high-performance format for huge analytic tables.

| |Index|
|---|---|
|1|[Hierarchy(Catalog, metadata, manifest list, manifest file, data file)](#hierarchy)|
|2|[Performance](#performance)|
|3|[Near Real-time Data Warehouse](#realtime)|
|4|[Iceberg on Cloud](#cloud)|

![Iceberg Structure](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_structure.jpg)

## 1 <a id='hierarchy'></a>Hierarchy
track the data in the table at the file level
- metadata(json) -> snapshot -> manifest list(avro) -> manifest file(avro) -> data file(parquet)

### 1.1 Iceberg Catalog
where to find the current location of the current metadata pointer
- HDFS: a file called version-hint.text
- Hive: a table property which stores the location of the current metadata file

### 1.2 metadata(json)
metadata files store metadata about a table: the table’s schema, partition information, snapshots, and which snapshot is the current one.
- file path: table_name/metadata/\*.metadata.json

![Iceberg metadata](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_metadata.jpg)
  
### 1.3 manifest list(avro)
manifest list is a list of manifest files.
- file path: table_name/metadata/snap-\*.avro

![Iceberg manifest list](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_manifest_list.jpg)

### 1.4 manifest file(avro)
manifest files track data files as well as additional details and statistics about each file.structure
- file path: table_name/metadata/\*.avro

![Iceberg manifest file](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_manifest_file.jpg)

### 1.5 data file(parquet, or others)
- file path: table_name/data/partition_name=pv/\*.parquet

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

## 3 <a id='realtime'></a>Near Real-time Data Warehouse
From Kafka+Flink to Iceberg+Flink

![Near Real-time Data Warehouse](https://github.com/barneywill/bigdata_demo/blob/main/imgs/realtime_data_warehouse.jpg)

## 4 <a id='cloud'></a>Iceberg on Cloud

### 4.1 GCP

![iceberg on gcp](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_gcp.jpg)

### 4.2 Bigquery Iceberg Table

### 4.3 AWS

![iceberg on aws](https://github.com/barneywill/bigdata_demo/blob/main/imgs/iceberg_aws.jpg)
