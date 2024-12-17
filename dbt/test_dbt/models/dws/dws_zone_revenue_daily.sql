{{ config(materialized='table') }}

with dwd_tripdata as (
    select * from {{ ref('dwd_tripdata') }}
),
dim_taxi_zone as
(
    select *
    from {{ref('dim_taxi_zone')}}
)

select 
-- Reveneue grouping 
b.zone as revenue_zone,
{{ dbt.date_trunc("day", "a.pickup_datetime") }} as revenue_date, 
a.service_type, 
-- Revenue calculation 
sum(a.fare_amount) as revenue_daily_fare,
sum(a.extra) as revenue_daily_extra,
sum(a.mta_tax) as revenue_daily_mta_tax,
sum(a.tip_amount) as revenue_daily_tip_amount,
sum(a.tolls_amount) as revenue_daily_tolls_amount,
sum(a.ehail_fee) as revenue_daily_ehail_fee,
sum(a.improvement_surcharge) as revenue_daily_improvement_surcharge,
sum(a.total_amount) as revenue_daily_total_amount,
-- Additional calculations
count(a.tripid) as total_daily_trips,
avg(a.passenger_count) as avg_daily_passenger_count,
avg(a.trip_distance) as avg_daily_trip_distance
from dwd_tripdata a
join dim_taxi_zone b on a.pickup_locationid = b.locationid
group by 1,2,3