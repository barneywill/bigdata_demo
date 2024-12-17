{{config(materialized='table')}}

select *, 'yellow' as service_type
from {{ref('staging_yellow_tripdata_201901')}}