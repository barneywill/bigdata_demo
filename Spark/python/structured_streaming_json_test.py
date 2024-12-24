from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BooleanType, LongType, TimestampType
from pyspark.sql import Window
import pyspark.sql.functions as F

schema = StructType([
    StructField('tripid', StringType(), True),
    StructField('vendorid', IntegerType(), True),
    StructField('ratecodeid', IntegerType(), True),
    StructField('pickup_locationid', IntegerType(), True),
    StructField('dropoff_locationid', IntegerType(), True),
    StructField('pickup_datetime', StringType(), True),
    StructField('dropoff_datetime', StringType(), True),
    StructField('store_and_fwdflag', BooleanType(), True),
    StructField('passenger_count', IntegerType(), True),
    StructField('trip_distance', StringType(), True),
    StructField('trip_type', IntegerType(), True),
    StructField('fare_amount', StringType(), True),
    StructField('extra', StringType(), True),
    StructField('mta_tax', StringType(), True),
    StructField('tip_amount', StringType(), True),
    StructField('tolls_amount', StringType(), True),
    StructField('ehail_fee', StringType(), True),
    StructField('improvement_surcharge', StringType(), True),
    StructField('total_amount', StringType(), True),
    StructField('payment_type', IntegerType(), True),
    StructField('payment_type_description', StringType(), True),
])

spark = SparkSession.builder \
    .master('local[*]') \
    .appName('StructuredStreamingJSONTest') \
    .config('spark.streaming.stopGracefullyOnShutdown', True) \
    .getOrCreate()

topic_name = 'your_topic_name'
kafka_servers = 'your_kafka_servers'
group_id = 'test'

df_stream = spark.readStream \
    .format('kafka') \
    .option('kafka.bootstrap.servers', kafka_servers) \
    .option('subscribe', topic_name) \
    .option('kafka.group.id', group_id) \
    .option('startingOffsets', 'earliest') \
    .option('checkpointLocation', 'checkpoint') \
    .load()
    
df = df_stream.select(F.from_json(F.col('value').cast('string'), schema).alias('json')) \
    .select(F.col('json.*')) \
    .select('vendorid', 'pickup_locationid', F.col('pickup_datetime').cast(TimestampType()).alias('pickup_datetime'))

df.printSchema()

df_agg = df.withWatermark('pickup_datetime', '10 minutes') \
    .groupBy(F.window(F.col('pickup_datetime'), '10 minutes', '5 minutes'), F.col('pickup_locationid')) \
    .count()

# Append, Complete, Update
df_agg.writeStream \
    .outputMode('Append') \
    .trigger(processingTime = '5 seconds') \
    .format('console') \
    .start()
    
spark.streams.awaitAnyTermination()
