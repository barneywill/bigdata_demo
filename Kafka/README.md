# Kafka

| |Index|
|---|---|
|1|[Topic](#topic)|
|2|[Producer](#producer)|
|3|[Consumer](#consumer)|

## <a id='topic'></a>1 Topic
```
# list all topics
bin/kafka-topics.sh --bootstrap-server $kafka_ip:9092 --list

# create a topic
bin/kafka-topics.sh --bootstrap-server $kafka_ip:9092 --create --partitions 2 --topic $topic_name

# delete a topic
bin/kafka-topics.sh --bootstrap-server $kafka_ip:9092 --delete --topic $topic_name
```

## <a id='producer'></a>2 Producer
```
# produce messages to a topic from a file
bin/kafka-console-producer.sh --bootstrap-server $kafka_ip:9092 --topic $topic_name < $file_path
```

## <a id='consumer'></a>3 Consumer
```
# comsume messages from a topic
bin/kafka-console-consumer.sh --bootstrap-server $kafka_ip:9092 --topic $topic_name --from-beginning

# check consumer group offset
bin/kafka-consumer-groups.sh --bootstrap-server $kafka_ip:9092 --group $group_id --describe

# reset consumer group offset: --to-datetime, --to-offset, --to-latest, --shift-by
bin/kafka-consumer-groups --bootstrap-server $kafka_ip --group $group_id --topic $topic_name --reset-offsets --to-earliest --execute
```

![kafka](https://github.com/barneywill/bigdata_demo/blob/main/imgs/apache_kafka.jpg)