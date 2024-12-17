{{config(materialized='table')}}

with green_tripdata as 
(
    select *
    from {{ref('ods_green_tripdata')}}
),
yellow_tripdata as
(
    select *
    from {{ref('ods_yellow_tripdata')}}
),
tripdata as
(
    select * from green_tripdata
    union all
    select * from yellow_tripdata
)

select a.*
from tripdata a
