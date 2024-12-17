{{config(materialized='table')}}

select 
    locationid, 
    borough, 
    zone, 
    replace(service_zone,'Boro','Green') as service_zone 
from {{ ref('stg_taxi_zone_lookup') }}