# Methodology

| |Index|
|---|---|
|1|[ETL/ELT](#etl)|
|2|[Map-Reduce](#mr)|
|3|[Data Warehouse](#dw)|
|4|[Databases](#db)|
|5|[BI](#bi)|

## <a id='etl'></a>1 ETL/ELT
- Extraction -> Transformation -> Load

![ETL](https://github.com/barneywill/bigdata_demo/blob/main/imgs/etl.jpg)

## <a id='mr'></a>2 Map-Reduce
- Map: data is split between parallel processing tasks. Transformation logic can be applied to each chunk of data.
- Reduce: handle aggregating data from the Map set

![Map Reduce](https://github.com/barneywill/bigdata_demo/blob/main/imgs/mr.jpg)

## <a id='dw'></a>3 Data Warehouse

### 3.1 Kimball's Dimensional Modeling
- Dimension Table
- Fact Table
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
- Column-based(Columnar) vs Row-based

![databases](https://github.com/barneywill/bigdata_demo/blob/main/imgs/databases.jpeg)

## <a id='bi'></a>5 BI
- Column, Line, Area, Dot, Bar, Circle, Pie

![BI](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bi_charts.jpeg)
