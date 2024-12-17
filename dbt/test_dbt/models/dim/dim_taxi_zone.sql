{{config(materialized='table')}}

select 
    locationid, 
    borough, 
    zone, 
    replace(service_zone,'Boro','Green') as service_zone 
from {{ ref('staging_taxi_zone_lookup') }}