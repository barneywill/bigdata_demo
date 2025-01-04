from pyspark.sql import SparkSession

# Initialize Spark session with JARs
spark = SparkSession.builder \
    .appName("Clickhouse_JDBC") \
    .master("local[*]") \
    .getOrCreate()

url = "jdbc:ch://localhost:8123/test"
user = "your_user" 
password = "your_password"  
query = "select * from green_tripdata_file"
driver = "com.clickhouse.jdbc.ClickHouseDriver"

df = (spark.read
      .format('jdbc')
      .option('driver', driver)
      .option('url', url)
      .option('user', user)
      .option('password', password).option(
    'query', query).load())

df.show()