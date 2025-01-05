from pyspark.sql import SparkSession

packages = [
    "com.clickhouse.spark:clickhouse-spark-runtime-3.4_2.12:0.8.0",
    "com.clickhouse:clickhouse-client:0.7.0",
    "com.clickhouse:clickhouse-http-client:0.7.0",
    "org.apache.httpcomponents.client5:httpclient5:5.2.1"
]

spark = (SparkSession.builder
        .appName("Clickhouse_Connector") \
        .master("local[*]") \
        .getOrCreate())

spark.conf.set("spark.sql.catalog.clickhouse", "com.clickhouse.spark.ClickHouseCatalog")
spark.conf.set("spark.sql.catalog.clickhouse.host", "127.0.0.1")
spark.conf.set("spark.sql.catalog.clickhouse.protocol", "http")
spark.conf.set("spark.sql.catalog.clickhouse.http_port", "8123")
spark.conf.set("spark.sql.catalog.clickhouse.user", "your_user")
spark.conf.set("spark.sql.catalog.clickhouse.password", "your_password")
spark.conf.set("spark.sql.catalog.clickhouse.database", "test")
spark.conf.set("spark.clickhouse.write.format", "json")

df = spark.sql("select * from clickhouse.test.green_tripdata_file")
df.show()