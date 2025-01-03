
show clusters;

show databases;

show tables;

describe $table_name;

show create table $table_name;


-- load data from url
create table test.green_tripdata
engine = MergeTree
order by ()
empty as 
select * from url('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz', 'CSVWithNames');

insert into test.green_tripdata
select * from url('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz', 'CSVWithNames');


