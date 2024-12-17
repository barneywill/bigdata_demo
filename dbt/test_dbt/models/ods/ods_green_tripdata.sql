{{config(materialized='table')}}

select *, 'green' as service_type
from {{ref('staging_green_tripdata_201901')}}