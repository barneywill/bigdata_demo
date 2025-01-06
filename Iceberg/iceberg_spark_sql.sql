
-- start spark-sql
spark-sql --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
    --conf spark.sql.catalog.local=org.apache.iceberg.spark.SparkCatalog \
    --conf spark.sql.catalog.local.type=hadoop \
    --conf spark.sql.catalog.local.warehouse=$PWD/warehouse


-- create table
create table local.db_test.tb_page_access_log (
    access_time timestamp, 
    create_time timestamp,
    page_url string, 
    user_id int
) using iceberg partitioned by (dt string);

create table local.db_test.tb_pv_uv_daily (
    page_url string, 
    pv int,
    uv int
) using iceberg partitioned by (dt string);

insert into local.db_test.tb_page_access_log partition(dt='20200101') values (cast('2020-01-01 00:00:00' as timestamp), cast('2020-01-01 00:00:00' as timestamp), '/home', 1),
       (cast('2020-01-01 00:00:00' as timestamp), cast('2020-01-01 00:00:00' as timestamp), '/home', 2),
       (cast('2020-01-01 00:00:00' as timestamp), cast('2020-01-01 00:00:00' as timestamp), '/about', 1),
       (cast('2020-01-01 00:00:00' as timestamp), cast('2020-01-01 00:00:00' as timestamp), '/about', 2);

insert into local.db_test.tb_page_access_log partition(dt='20200102') values (cast('2020-01-02 00:00:00' as timestamp), cast('2020-01-02 00:00:00' as timestamp), '/home', 1),
       (cast('2020-01-02 00:00:00' as timestamp), cast('2020-01-02 00:00:00' as timestamp), '/home', 2),
       (cast('2020-01-02 00:00:00' as timestamp), cast('2020-01-02 00:00:00' as timestamp), '/about', 1),
       (cast('2020-01-02 00:00:00' as timestamp), cast('2020-01-02 00:00:00' as timestamp), '/about', 2);

-- check the data
select * from local.db_test.tb_page_access_log;

-- check snapshots
select * from local.db_test.tb_page_access_log.snapshots;

-- time travel
select * from local.db_test.tb_page_access_log timestamp as of '2025-01-06 09:30:00';
select * from local.db_test.tb_page_access_log for system_time as of '2025-01-06 09:30:00';
select * from local.db_test.tb_page_access_log version as of $snapshot_id;

-- insert overwrite
insert overwrite local.db_test.tb_page_access_log partition(dt='20200101')
values (cast('2020-01-01 00:00:00' as timestamp), cast('2020-01-01 00:00:00' as timestamp), '/home', 1),
       (cast('2020-01-01 00:00:00' as timestamp), cast('2020-01-01 00:00:00' as timestamp), '/home', 2),
       (cast('2020-01-01 00:00:00' as timestamp), cast('2020-01-01 00:00:00' as timestamp), '/about', 1),
       (cast('2020-01-01 00:00:00' as timestamp), cast('2020-01-01 00:00:00' as timestamp), '/about', 2);

-- update
update local.db_test.tb_page_access_log set user_id = user_id + 3 where page_url = '/home' and dt = '20200101';

-- delete
delete from local.db_test.tb_page_access_log where page_url = '/home' and user_id = 5 and dt = '20200101';


-- insert or update
merge into local.db_test.tb_pv_uv_daily t 
using (select * from local.db_test.tb_pv_uv_daily) u on t.page_url = u.page_url and t.dt = u.dt
when matched then update set t.pv = t.pv + u.pv, t.uv = t.uv + u.uv
when not matched then insert *;
