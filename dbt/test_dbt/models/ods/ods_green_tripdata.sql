{{config(materialized='table')}}

select *, 'green' as service_type
from {{ref('stg_green_tripdata_201901')}}