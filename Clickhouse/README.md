# Clickhouse

ClickHouse® is a high-performance, column-oriented SQL database management system (DBMS) for online analytical processing (OLAP).

ClickHouse is the fastest and most resource efficient open-source database for real-time apps and analytics.

## 1 SSB (Star Schema Benchmark)

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

## 3 Table Engines

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

## 2 Sparse Primary Indexes

![clickhouse index](https://github.com/barneywill/bigdata_demo/blob/main/imgs/clickhouse_index.jpg)

https://clickhouse.com/docs/en/optimize/sparse-primary-indexes
