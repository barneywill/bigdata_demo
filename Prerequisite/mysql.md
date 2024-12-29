# Mysql

| |Index|
|---|---|
|1|[User](#user)|
|2|[Dump & Import](#dump)|
|3|[Other](#other)|
|4|[Master & Slave](#master)|

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