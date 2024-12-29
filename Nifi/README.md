# Nifi

| |Index|
|---|---|
|1|[Run](#run)|
|2|[Open](#open)|
|3|[Scenario](#scenario)|

## <a id='run'></a>1 Run
```
#start
bin/nifi.sh start

#add user
bin/nifi.sh set-single-user-credentials $username $password
```

## <a id='open'></a>2 Open
## Use a host name or an ip to access
https://whatever-host-name:8443/nifi

## <a id='scenario'></a>3 Scenario

### 3.1 Daily Mysql to Google Cloud Storage
- QueryDatabaseTableRecord -> PutGCSObject

```
#Expression
yesterday: ${now():toNumber():minus(86400000):format('yyyy-MM-dd')} 
today: ${now():format('yyyy-MM-dd') }
tomorrow: ${now():plus(86400000):format('yyyy-MM-dd') }
```

![mysql_2_google_cloud_storage](https://github.com/barneywill/bigdata_demo/blob/main/imgs/mysql_2_google_cloud_storage.jpg)

### 3.2 Realtime Mysql to Kafka
- CaptureChangeMySQL -> PublishKafka

```
#Mysql
GRANT SELECT, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'username'@'hostname';
FLUSH PRIVILEGES;
```

![mysql_2_kafka](https://github.com/barneywill/bigdata_demo/blob/main/imgs/mysql_2_kafka.jpg)

### 3.3 Bigquery to Kafka
- ExecuteSQLRecord -> PublishKafkaRecord

```
#Bigquery jdbc driver download url
https://mvnrepository.com/artifact/com.simba/bigquery

#Configuration
Database Connection URL: jdbc:bigquery://https://www.googleapis.com/bigquery/v2:443;ProjectId=your-project-if-here;OAuthType=0;OAuthServiceAcctEmail=your-email-for-service-account-here;OAuthPvtKeyPath=path_on_nifi_server_where_the_service_account_json_is_located;
Database Driver Class Name: com.simba.googlebigquery.jdbc.Driver
Database Driver Location: full_path_to_jars_folder_location/
```

![bigquery_2_kafka](https://github.com/barneywill/bigdata_demo/blob/main/imgs/bigquery_2_kafka.jpg)

### 3.4 Change Data Capture
- QueryDatabaseTableRecord -> ConvertJSONToSQL -> PutSQL

### 3.5 Kafka to Bigquery
- ConsumeKafka -> PutBigQuery

### 3.6 Bigquery to Clickhouse



