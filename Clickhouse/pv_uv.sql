
create database test;

-- page_access_log
create table if not exists test.page_access_log
(
    `access_time` DateTime comment 'Access Time',
    `create_time` DateTime comment 'Create Time',
    `page_url` String comment 'Page URL',
    `user_id` UInt64 comment 'User ID',
) engine = MergeTree()
    partition by toYYYYMMDD(access_time)
    order by `access_time`;


-- daily_pv_uv, partitioned by access_date
create materialized view if not exists test.daily_pv_uv
    engine = AggregatingMergeTree()
    partition by access_date
    order by (access_date, page_url)
as
select toDate(access_time) as access_date,
       page_url,
       sumState(1) as pv,
       uniqState(user_id, access_date) as uv
from test.page_access_log
group by access_date, page_url;


-- total_pv_uv
create materialized view if not exists test.total_pv_uv
    engine = AggregatingMergeTree()
    order by (page_url)
as
select page_url,
       sumState(1) as pv,
       uniqState(user_id) as uv
from test.page_access_log
group by page_url;


-- insert
insert into test.page_access_log(access_time, create_time, page_url, user_id)
values ('2020-01-01 00:00:00', '2020-01-01 00:00:00', '/home', 1),
       ('2020-01-01 00:00:00', '2020-01-01 00:00:00', '/home', 2),
       ('2020-01-01 00:00:00', '2020-01-01 00:00:00', '/about', 1),
       ('2020-01-01 00:00:00', '2020-01-01 00:00:00', '/about', 2),
       ('2020-01-02 00:00:00', '2020-01-02 00:00:00', '/home', 1),
       ('2020-01-02 00:00:00', '2020-01-02 00:00:00', '/home', 2),
       ('2020-01-02 00:00:00', '2020-01-02 00:00:00', '/about', 1),
       ('2020-01-02 00:00:00', '2020-01-02 00:00:00', '/about', 2);

select * from test.page_access_log;
select * from test.daily_pv_uv;
select * from test.total_pv_uv;

-- query
select access_date, page_url, sumMerge(pv), uniqMerge(uv) 
from test.daily_pv_uv
group by access_date, page_url;

select page_url, sumMerge(pv), uniqMerge(uv) 
from test.total_pv_uv
group by page_url;

