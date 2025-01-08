# Methodology

| |Index|
|---|---|
|1|[ETL/ELT](#etl)|
|2|[Map-Reduce](#mr)|
|3|[Data Warehouse](#dw)|
|4|[Databases](#db)|
|5|[BI](#bi)|
|6|[Data Engineering Skills](#de)|
|7|[Data Quality](#quality)|
|8|[Data Architecture](#architecture)|

![Data Lifecircle](https://github.com/barneywill/bigdata_demo/blob/main/imgs/data_lifecircle.jpg)

## <a id='etl'></a>1 ETL/ELT
- Extraction -> Transformation -> Load
  - Usually from Data Sources to Data Lake/Data Warehouse/Kafka
- Structured Data, Unstructured Data
- CDC: Change Data Capture
  - FlinkCDC, Debezium

![ETL](https://github.com/barneywill/bigdata_demo/blob/main/imgs/etl.jpg)

## <a id='mr'></a>2 Map-Reduce
- Map: data is split between parallel processing tasks. Transformation logic can be applied to each chunk of data.
- Reduce: handle aggregating data from the Map set

![Map Reduce](https://github.com/barneywill/bigdata_demo/blob/main/imgs/mr.jpg)

## <a id='dw'></a>3 Data Warehouse

### 3.1 Kimball's Dimensional Data Modeling
- Dimension Table, Fact Table
- Design Schema
  - Star Schema
  - Snowflake Schema: divides subdimensions into dimension tables

![Design Schema](https://github.com/barneywill/bigdata_demo/blob/main/imgs/design_schema.jpg)

### 3.2 Data Warehouse Layers

<table border="2" style="width:100%; padding: 10px;">
    <tr style="height:30px;"><th style="width:5%;text-align: center;">Layer</th><th style="width:20%;text-align: center;">Full Name</th><th style="text-align: center;">Explanation</th></tr>
    <tr><td style="font-weight:bold;">STG</td><td>Stage</td><td>Usually not necessary.</td></tr>
    <tr><td style="font-weight:bold;">ODS</td><td>Operational Data Store</td><td>A data warehouse preparation area that provides basic raw data for the DWD layer. Keep the same as tables in the business system.</td></tr>
    <tr><td style="font-weight:bold;">DWD</td><td>Data Warehouse Details</td><td>Responsible for cleaning and precipitating the data of the ODS layer, storing data in a subject-oriented manner, and storing historical incremental data or full data. Detailed data with the same granularity as ODS.</td></tr>
    <tr><td style="font-weight:bold;">DIM</td><td>Dimension</td><td>Dimension tables.</td></tr>
    <tr><td style="font-weight:bold;">DWS</td><td>Data Warehouse Service</td><td>A slightly summarized wide table divided by business and topic, is the subject of the data warehouse.</td></tr>
    <tr><td style="font-weight:bold;">ADS</td><td>Application Data Service</td><td>Provides users with visual data query and analysis services based on DWS based on the analysis business needs of users. </td></tr>
</table>

![data warehouse](https://github.com/barneywill/bigdata_demo/blob/main/imgs/data_warehouse.jpeg)

## <a id='db'></a>4 Databases
- SQL vs No-SQL
- OLTP vs OLAP
- Column-oriented(Columnar) vs Row-oriented
  - Row-oriented: In a row-oriented database, even though the query only processes a few out of the existing columns, the system still needs to load the data from other existing columns from disk to memory. 
  - Column-oriented: only the columns required for a query are read from disk, avoiding unnecessary I/O for unused data.

![databases](https://github.com/barneywill/bigdata_demo/blob/main/imgs/databases.jpeg)


## <a id='bi'></a>5 BI
Data Visualization
- Column, Line, Area, Dot, Bar, Circle, Pie

![BI](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bi_charts.jpeg)

## <a id='de'></a>6 Data Engineering Skills
- Data Source
  - Mysql, Postgresql, Log, Gateway
- Data Ingestion: Batch, Streaming
  - Nifi, Kafka
- Data Modeling
- Data Lake
  - Cloud Storage, Iceberg
- Data Warehouse
  - Bigquery
- Data Analytics: Batch, Streaming, OLAP
  - Spark, Dataproc, Clickhouse
- Data Governance: Catalog, Lineage
  - dbt
- Data Pipeline Orchestration
  - Airflow, Cloud Composer
- Data Quality
  - Deequ
- Data Application: BI, ML
  - Looker, Spark ML, XGBoost

## <a id='quality'></a> 7 Data Quality
- Completeness: missing or not
  - Attribute-level(columns), Record-level(rows)
- Validity: meet certain criteria
  - data format(phone, zipcode, email, date), data type(integer, string), data range(min, max, enumeration, nullable), complex rules(if a = 1 then b < 0.5)
- Uniqueness: duplication or not
- Timeliness: available before when
  - Freshness, Latency
- Consistency: like 10 records in ODS layer but only 1 record in ADS layer
- Accuracy: correct or not
- Integrity: the accuracy and consistency of data over its lifecycle

### Open Source Frameworks
- https://github.com/awslabs/deequ
- https://github.com/great-expectations/great_expectations
  - https://github.com/calogica/dbt-expectations
- https://github.com/sodadata/soda-core
- https://github.com/ubisoft/mobydq
  
![Data Quality](https://github.com/barneywill/bigdata_demo/blob/main/imgs/data_quality.jpg)

## <a id='architecture'></a> 8 Data Architecture
- Lambda: Batch + Real-time
  - Drawbacks: double code and system/conflicts
- Kappa: Only Real-time
  - Drawbacks: re-precess/out of order data/cold storage/complex joins

![bigdata cloud](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bigdata_cloud.jpg)
