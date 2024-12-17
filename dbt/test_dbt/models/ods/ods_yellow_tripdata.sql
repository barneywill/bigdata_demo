{{config(materialized='table')}}

select *, 'yellow' as service_type
from {{ref('stg_yellow_tripdata_201901')}}