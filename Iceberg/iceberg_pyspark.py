from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .master('local[*]') \
    .appName('Iceberg_Python') \
	.config('spark.sql.catalog.local','org.apache.iceberg.spark.SparkCatalog') \
	.config('spark.sql.catalog.local.type','hadoop') \
	.config('spark.sql.catalog.local.warehouse', '/path/to/warehouse')    \
    .getOrCreate()

# set conf here or above
#spark.conf.set('spark.sql.catalog.spark_catalog','org.apache.iceberg.spark.SparkSessionCatalog')
#spark.conf.set('spark.sql.catalog.spark_catalog.type','hive')
spark.conf.set('spark.sql.catalog.local','org.apache.iceberg.spark.SparkCatalog')
spark.conf.set('spark.sql.catalog.local.type','hadoop')
spark.conf.set('spark.sql.catalog.local.warehouse', '/path/to/warehouse')

# .option("as-of-timestamp", "499162860000")
# .option("snapshot-id", 10963874102873L)
df = spark.read.format('iceberg') \
    .load('local.db_test.tb_page_access_log')
df.show()

new_df = df.select((col('user_id') + 1).alias('user_id'), 'access_time', 'create_time', 'page_url', 'dt')
new_df.show()

new_df.write.format('iceberg') \
    .mode('append') \
        .save('local.db_test.tb_page_access_log')
