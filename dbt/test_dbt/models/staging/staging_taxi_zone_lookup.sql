{{config(materialized='view')}}

select *
from {{source('staging', 'staging_taxi_zone_lookup')}}