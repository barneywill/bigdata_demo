
show clusters;
show databases;
use $database_name;
show tables;
desc $table_name;
show create table $table_name;


-- 1 load data
create database test;

-- 1.1 load data from url
create table test.green_tripdata_url
engine = MergeTree
order by ()
empty as 
select * 
from url('https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2024-01.parquet', 'Parquet') limit 10;

insert into test.green_tripdata
select * from url('https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2024-01.parquet', 'Parquet');

select count(1) from test.green_tripdata;


-- 1.2 load data from local file

-- prepare data
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2024-01.parquet

-- load data
create table test.green_tripdata_file
engine = MergeTree
order by ()
empty as 
select * from file('/path/to/green_tripdata_2024-01.parquet', 'Parquet') limit 10;

insert into test.green_tripdata_file
select * from file('/path/to/green_tripdata_2024-01.parquet', 'Parquet');

select * from test.green_tripdata_file limit 10;


-- 1.3 load data from Mysql
-- prepare data from parquet file to mysql by pyspark
--mysql
create database test;

--pyspark
df = spark.read.parquet('file:///path/to/green_tripdata_2024-01.parquet')
df.show()
df.write.format('jdbc').options(
    url='jdbc:mysql://localhost:3306/test',
    driver='com.mysql.jdbc.Driver',
    dbtable='green_tripdata',
    user='mysql_user',
    password='password'
).mode('append').save()

--mysql
select * from green_tripdata limit 10;

-- load data
create table test.green_tripdata_mysql
engine = MergeTree
order by ()
empty as
SELECT *
FROM mysql(
    '127.0.0.1:3306',
    'test',
    'green_tripdata',
    'mysql_user',
    'password'
) 
limit 10
;

insert into test.green_tripdata_mysql
select * 
from mysql(
    '127.0.0.1:3306',
    'test',
    'green_tripdata',
    'mysql_user',
    'password'
);

select * from test.green_tripdata_mysql limit 10;


-- 1.4 load data from Kafka
-- prepare data from parquet file to json file by pyspark, from json file to kafka by kafka-console-producer.sh
--kafka
bin/kafka-topics.sh --bootstrap-server $kafka_ip:9092 --create --partitions 2 --topic green_tripdata

--pyspark
df = spark.read.parquet('file:///path/to/green_tripdata_2024-01.parquet')
df.show()
df.write.json('file:///path/to/green_tripdata_2024-01_json', mode='append')

--kafka
bin/kafka-console-producer.sh --bootstrap-server $kafka_ip:9092 --topic green_tripdata < /path/to/green_tripdata_2024-01_json/*.json
bin/kafka-console-consumer.sh --bootstrap-server $kafka_ip:9092 --topic green_tripdata --from-beginning|more

-- load data
create table test.green_tripdata_kafka as test.green_tripdata_mysql
engine = Kafka()
settings kafka_broker_list = '$kafka_ip:9092',
         kafka_topic_list = 'green_tripdata',
         kafka_group_name = 'test',
         kafka_format = 'JSONEachRow';

set stream_like_engine_allow_direct_select=1;

select count(1) from test.green_tripdata_kafka;


-- 1.5 load data from Google Cloud Storage, same as S3
-- prepare data, upload the parquet file to a bucket in Google Cloud Storage

-- load data
create table test.green_tripdata_gcs
engine = MergeTree
order by ()
empty as
select *
from s3(
  'https://storage.googleapis.com/my-bucket/green_tripdata_2024-01.parquet',
  'MY_GCS_HMAC_KEY',
  'MY_GCS_HMAC_SECRET_KEY',
  'Parquet'
)
limit 10;

insert into test.green_tripdata_gcs
select * 
from s3(
  'https://storage.googleapis.com/my-bucket/green_tripdata_2024-01.parquet',
  'MY_GCS_HMAC_KEY',
  'MY_GCS_HMAC_SECRET_KEY',
  'Parquet'
);

select * from test.green_tripdata_gcs limit 10;
