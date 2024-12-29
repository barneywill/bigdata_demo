# Methodology

## 1 Data Warehouse
Data Warehouse Layers

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

## 2 Databases
- SQL vs No-SQL
- OLTP vs OLAP
- Column-based(Columnar) vs Row-based

![databases](https://github.com/barneywill/bigdata_demo/blob/main/imgs/databases.jpeg)

## 3 BI
- Column, Line, Area, Dot, Bar, Circle, Pie

![BI](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bi_charts.jpeg)
