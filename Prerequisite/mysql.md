# Mysql

| |Index|
|---|---|
|1|[User](#user)|
|2|[Dump & Import](#dump)|
|3|[Other](#other)|
|4|[Master & Slave](#master)|
|5|[Optimization](#optimization)|

## 1 <a id='user'></a>User

```
# Create user, % means other than localhost
CREATE USER 'username'@'%' IDENTIFIED BY 'password';
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

# Set a new password
SET PASSWORD FOR 'username'@'%' = PASSWORD('newpassword');

# grant, use * to represent all tables or all databases
GRANT privileges ON dbname.tablename TO 'username'@'%'

# revoke
REVOKE privilege ON dbname.tablename FROM 'username'@'%';

# show grants
show grants for username;
```

## 2 <a id='dump'></a>Dump & Import

```
# Dump,  --all-databases, --no-create-info, --skip-add-locks
mysqldump -u dbuser -p dbname [tablename1] [tablename2] > dump.sql

# Import
mysql -uusername -p dbname < dump.sql
or
mysql>source /path/dump.sql
```

## 3 <a id='other'></a>Other

```
# show process list
mysql>show processlist;

# show variables
mysql>show variables;

# show index
mysql>show index from $db.$table;

mysql>select @@profiling;

# profiling
mysql>set profiling=1;
mysql>select * from $table;
mysql>show profiles;
mysql>show profile all for query $query_id;
mysql>set profiling=0;

# alter char set
mysql> alter database $database_name character set utf8;
mysql> alter table $table_name default character set utf8;
mysql> alter table $table_name change $column_name $column_name varchar(50) character utf8;
```

## 4 <a id='master'></a>Master & Slave

### 4.1 Master

#### my.cnf
```
# vi /etc/my.cnf
[mysqld]
server-id=1
log-bin=master-bin
log-bin-index=master-bin.index
```

#### Restart Mysql
```
service mysqld restart
```

#### Start master
```
mysql>create user 'repl'@'%' IDENTIFIED BY 'repl';
mysql>GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
mysql> SHOW MASTER STATUS;
```

### 4.2 Slave

#### my.cnf
```
# vi /etc/my.cnf
[mysqld]
server-id=2
relay-log-index=slave-relay-bin.index
relay-log=slave-relay-bi
read_only=1
```

#### Restart Mysql
```
service mysqld restart
```

#### Start slave
```
mysql> change master to master_host='$master_server',master_port=3306,master_user='repl',master_password='repl',master_log_file='master-bin.000001',master_log_pos=0;
mysql> start slave;
mysql> show slave status;
```

## 5 <a id='optimization'></a>Optimization

### 5.1 Index
Indexes serve as the backbone for efficient query performance.

#### Clustered Index
 InnoDB tables use the primary key as the clustered index, meaning the data is physically organized based on the primary key values.
- Primary key

#### Secondary Index
A secondary or non-clustered index is an additional index separate from the primary (clustered) index. It just references the primary key.
- Unique
- Index: one column
- Composite indexes: multiple columns
- Full-text

#### Underlying Data Structure
B+ Trees: efficient for insertion, deletion, and lookup operations, with data stored in a sorted order.
- M-way search tree(from binary search tree), balance tree
- All data is only at leaf nodes.
- Leaf nodes are stored as structural linked list, so sequential access is possible just like linked list

![B+ Tree](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bplustree.jpg)

### 5.2 Window Function vs Group By

#### 5.2.1 Window Function
Window functions allow us to apply functions like AVG, COUNT, MAX, and MIN on a group of records while still leaving the individual records accessible.

##### Aggregate functions
```
AVG()
BIT_AND()
BIT_OR()
BIT_XOR()
COUNT()
JSON_ARRAYAGG()
JSON_OBJECTAGG()
MAX()
MIN()
STDDEV_POP(), STDDEV(), STD()
STDDEV_SAMP()
SUM()
VAR_POP(), VARIANCE()
VAR_SAMP()
```

##### Positional functions 
```
CUME_DIST()
DENSE_RANK()
FIRST_VALUE()
LAG()
LAST_VALUE()
LEAD()
NTH_VALUE()
NTILE()
PERCENT_RANK()
RANK()
ROW_NUMBER()
```

##### Example
```
SELECT year, country, product, profit,
    SUM(profit) OVER() AS total_profit,
    SUM(profit) OVER(PARTITION BY country) AS country_profit
FROM sales
ORDER BY country, year, product, profit;
```

#### 5.2.2 Group By
The GROUP BY clause allows us to group a set of records based on some criteria and apply a function (e.g. AVG or MAX) to each group, obtaining one result for each group of records.

##### Aggregate functions
Only

##### Example
```
SELECT year, country, product, 
    SUM(profit) AS total_profit
FROM sales
GROUP BY country, year, product
```

### 5.3 Optimization
- Improving query performance: By creating an index on the column used in the WHERE clause, the database can quickly locate the relevant rows, resulting in much faster query execution. 
- Joins
  - Indexing for joins: If two tables are frequently joined on a specific column, creating an index on that column in both tables can reduce the time required to match rows.
  - Choosing appropriate join techniques
  - Avoid cartesian
- Handling large datasets: Partitioning large tables and creating indexes on each partition can help distribute the workload and improve performance.
- Query structure rewriting: break down complex queries
- Explain: describe how SQL queries are being executed
- Limiting and Pagination
- Hint or update statistics: enable query optimizer to generate efficient execution plans
