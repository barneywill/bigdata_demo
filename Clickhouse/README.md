# Clickhouse

ClickHouse® is a high-performance, column-oriented SQL database management system (DBMS) for online analytical processing (OLAP).

ClickHouse is the fastest and most resource efficient open-source database for real-time apps and analytics.

https://www.vldb.org/pvldb/vol17/p3731-schulze.pdf

| |Index|
|---|---|
|1|[Concepts(Columnar, OLAP, MPP, Vectorized)](#concept)|
|2|[Table(Table Engines, Data Ingestion, Sharding, Data Compression, Data Replication)](#table)|
|3|[Approximate calculation](#approximate)|
|4|[Index](#index)|
|5|[SSB (Star Schema Benchmark)](#ssb)|
|6|[Other](#other)|

![Clickhouse](https://github.com/barneywill/bigdata_demo/blob/main/imgs/clickhouse_architecture.jpg)

## 1 <a id='concept'></a>Concepts
### 1.1 Columnar(Column-oriented)
- The values of each column are stored sequentially one after the other on disk, no unnecessary data is loaded when the query is run, which means only the columns required for a query are read from disk, avoiding unnecessary I/O for unused data.
- Column-stores are particularly well suited for such compression as values of the same type and data distribution are located together.

![Clickhouse Columnar](https://github.com/barneywill/bigdata_demo/blob/main/imgs/clickhouse_columnar.gif)

### 1.2 OLAP(Online Analytical Processing)
- OLAP: 
  - Focus on building reports, each based on large volumes of historical data, but by doing it less frequently. 
  - Refers to SQL queries with complex calculations (e.g., aggregations, string processing, arithmetics) over massive datasets
  - Most OLAP databases are columnar.
- OLTP(Online Transactional Processing): 
  - Handle a continuous stream of transactions, constantly modifying the current state of data. 
  - Read and write just a few rows per query.
  - Most OLTP systems store data arranged by rows.

### 1.3 MPP(Massively Parallel Processing)
A processing paradigm where hundreds or thousands of processing nodes work on parts of a computational task in parallel.

![MPP](https://github.com/barneywill/bigdata_demo/blob/main/imgs/mpp.jpg)

### 1.4 Vectorized Execution Engine
"Vectorization" means that query plan operators pass intermediate result rows in batches instead of single rows. This leads to better utilization of CPU caches and allows operators to apply SIMD instructions to process multiple values at once.

![smid](https://github.com/barneywill/bigdata_demo/blob/main/imgs/simd.jpg)

## 2 <a id='table'></a>Table
- In ClickHouse, each table consists of multiple "table parts". A part is created whenever a user inserts data into the table (INSERT statement).
- To avoid that too many parts accumulate, ClickHouse runs a merge operation in the background which continuously combines multiple (small) parts into a single bigger part.
- Tables can be split ("sharded") and distributed across the nodes.

### 2.1 Table Engines

- Merge Tree
  - ReplacingMergeTree
  - AggregatingMergeTree
    - AggregateFunction
- Log
- Integrations
  - Kafka
  - Mysql
  - Iceberg
  - Azure Blob Storage
  - Azure Queue
  - S3
  - S3 Queue

### 2.2 Examples: PV, UV
<a href='https://github.com/barneywill/bigdata_demo/blob/main/Clickhouse/pv_uv.sql' target='_blank'>pv_uv.sql</a>

### 2.3 Data Ingestion
<a href='https://github.com/barneywill/bigdata_demo/blob/main/Clickhouse/clickhouse.sql' target='_blank'>clickhouse.sql</a>
- url
- local file
- Mysql
- Kafka
- Google Cloud Storage

![GCS HMAC KEY](https://github.com/barneywill/bigdata_demo/blob/main/imgs/gcs_hmac.jpg)

### 2.4 Sharding
Sharding data across multiple servers can be used to divide the load if you exceed the capacity of a single server. The destination server is determined by the sharding key, and is defined when you create the distributed table. 


### 2.5 Data Compression
Data compression not only reduces the storage size of the database tables, but in many cases, it also improves query performance as local disks and network I/O are often constrained by low throughput.
- general
  - LZ4
  - LZ4HC[(level)]: LZ4 HC (high compression) algorithm with configurable level.
  - ZSTD[(level)]
- specialized
  - Delta: for integer values, raw values are replaced by the difference of two neighboring values, except for the first value that stays unchanged.
  - DoubleDelta: for integer values, calculates delta of deltas and writes it in compact binary form.
  - GCD for integer values, calculates the greatest common denominator (GCD) of the values in the column, then divides each value by the GCD.
  - Gorilla for floating-point values
  - FPC for floating-point values
  - T64

### 2.6 Data Replication
Data can be replicated across multiple cluster nodes for high availability, failover, and zero downtime upgrades. Replication does not depend on sharding. Each shard has its own independent replication.
- ReplicatedMergeTree
- ReplicatedReplacingMergeTree
- ReplicatedAggregatingMergeTree

## 3 With Spark

```
# Put jars under $SPARK_HOME/jars
# clickhouse jdbc
https://repo1.maven.org/maven2/com/clickhouse/clickhouse-jdbc/0.7.2/clickhouse-jdbc-0.7.2.jar
# spark connector
https://repo1.maven.org/maven2/com/clickhouse/spark/clickhouse-spark-runtime-3.5_2.12/0.8.1/clickhouse-spark-runtime-3.5_2.12-0.8.1.jar
https://repo1.maven.org/maven2/com/clickhouse/clickhouse-client/0.7.2/clickhouse-client-0.7.2.jar
https://repo1.maven.org/maven2/com/clickhouse/clickhouse-http-client/0.7.2/clickhouse-http-client-0.7.2.jar
```

## 4 <a id='approximate'></a>Approximate calculation
ClickHouse provides ways to trade accuracy for performance. 
- some of its aggregate functions calculate the distinct value count, the median, and quantiles approximately.
- queries can be run on a sample of the data to compute an approximate result quickly.
- aggregations can be run with a limited number of keys instead of for all keys.
  
Like HLLC：Hyper LogLog Counting.

## 4 <a id='index'></a>Index
Aim to skip as many rows during full-column reads as possible because the fastest way to read data is to not read it at all.

### 4.1 Sparse Primary Indexes
Define the sort order of the table data.

![clickhouse index](https://github.com/barneywill/bigdata_demo/blob/main/imgs/clickhouse_index.jpg)

https://clickhouse.com/docs/en/optimize/sparse-primary-indexes

### 4.2 Data Skipping Indexes
Embed additional data statistics into columns, e.g. the minimum and maximum column value, the set of unique values, etc.

## 5 <a id='ssb'></a>SSB (Star Schema Benchmark)

Star Schema Benchmark(SSB) is a lightweight performance test set in the data warehouse scenario. SSB provides a simplified star schema data based on TPC-H, which is mainly used to test the performance of multi-table JOIN query under star schema. In addition, the industry usually flattens SSB into a wide table model (Referred as: SSB flat) to test the performance of the query engine, refer to Clickhouse.

https://www.cs.umb.edu/~poneil/StarSchemaB.PDF

https://github.com/vadimtk/ssb-dbgen

### Generate dataset
```
dbgen -s 100 -T a
```

### Run queries
```
./qgen -s 100
```

https://clickhouse.com/docs/en/getting-started/example-datasets/star-schema

![ssb](https://github.com/barneywill/bigdata_demo/blob/main/imgs/ssb.jpg)

## 6 <a id='other'></a>Others

### 6.1 Clickhouse Playground

https://sql.clickhouse.com/

### 6.2 Clickhouse vs Spark
- Spark: Shuffle Sort Merge Join
  - Distributed sorting isn’t the best way to perform reduce operations if the result of the operation and all the intermediate results (if there are any) are located in the RAM of a single server, which is usually the case for online queries.
  - Distributed sorting is one of the main causes of reduced performance when running simple map-reduce tasks.
- Clickhouse
  - In such a case, a hash table is an optimal way to perform reduce operations.
