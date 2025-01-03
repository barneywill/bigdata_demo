# DBT (Data Build Tool)

dbt is the industry standard for data transformation. Transform raw data into analysis-ready insights, and make data-driven decisions with confidence.

| |Index|
|---|---|
|1|[Install](#install)|
|2|[Move profiles.yml to the location and fill in details](#move)|
|3|[Running the following commands](#run)|
|4|[Data Layers](#layers)|
|5|[codegen](#codegen)|
|6|[Data Assets and Lineage](#doc)|
|7|[Test](#test)|

![DBT](https://github.com/barneywill/bigdata_demo/blob/main/imgs/dbt_architecture.jpg)

## <a id='install'></a>1 Install
- pip install dbt
- pip install dbt-bigquery

If you want to create a new project:
- dbt init

## <a id='move'></a>2 Move profiles.yml to the location and fill in details:
- ~/.dbt/profiles.yml

## <a id='run'></a>3 Running the following commands:
- cd /direcotry/to/test_dbt
- dbt clean
- dbt deps
- dbt build --vars 'is_test_run: false'
- dbt run --vars 'is_test_run: false'

## <a id='layers'></a>4 Data Layers:
### staging:
    stg_yellow_tripdata_201901
    stg_green_tripdata_201901
    stg_taxi_zone_lookup
### ods:
    ods_yellow_tripdata
    ods_green_tripdata
### dwd:
    dwd_tripdata
### dim:
    dim_taxi_zone
### dws:
    dws_zone_revenue_daily

![bigquery dataset](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bigquery_dataset_structure.jpg)

## <a id='codegen'></a>5 codegen
- dbt run-operation generate_source --args '{"schema_name":"staging","database_name":"database_name","table_names":["staging_green_tripdata_201901","staging_yellow_tripdata_201901", "staging_taxi_zone_lookup"],"generate_columns":true}'
- dbt run-operation generate_base_model --args '{"source_name":"staging","table_name":"staging_green_tripdata_201901"}'
- dbt run-operation generate_model_yaml --args '{"model_names":["dwd_tripdata"]}'

## <a id='doc'></a>6 doc
- Data Assets
- Data Lineage
```
dbt docs generate
dbt docs serve
```

![dbt layers](https://github.com/barneywill/bigdata_demo/blob/main/imgs/dbt.jpg)

## <a id='test'></a>7 Tests
- tests: on columns
- unit-tests: test your sql like code
- dbt-expectations: an extension package for dbt, inspired by the Great Expectations package for Python.
  - https://github.com/calogica/dbt-expectations
