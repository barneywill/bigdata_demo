# Clickhouse

ClickHouse® is a high-performance, column-oriented SQL database management system (DBMS) for online analytical processing (OLAP).

ClickHouse is the fastest and most resource efficient open-source database for real-time apps and analytics.

## 1 SSB Schema Benchmark

https://www.cs.umb.edu/~poneil/StarSchemaB.PDF

### Generate dataset

https://github.com/vadimtk/ssb-dbgen

```
dbgen -s 100 -T a
```

![ssb](https://github.com/barneywill/bigdata_demo/blob/main/imgs/ssb.jpg)

## 2 Sparse Primary Indexes

![clickhouse index](https://github.com/barneywill/bigdata_demo/blob/main/imgs/clickhouse_index.jpg)

https://clickhouse.com/docs/en/optimize/sparse-primary-indexes
