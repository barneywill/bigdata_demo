# Kafka

Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.

| |Index|
|---|---|
|1|[Topic](#topic)|
|2|[Producer](#producer)|
|3|[Consumer](#consumer)|
|4|[Internals](#internal)|

![kafka architecture](https://github.com/barneywill/bigdata_demo/blob/main/imgs/kafka_architecture.jpg)

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

## <a id='internal'></a>4 Internals

### 4.1 zero-copy

![zero-copy](https://github.com/barneywill/bigdata_demo/blob/main/imgs/zero-copy.jpg)

### 4.2 ISR (In-Sync Replicas)
followers with a pool of fetch request

![Kafka ISR](https://github.com/barneywill/bigdata_demo/blob/main/imgs/kafka_isr.jpg)

### 4.3 Producer ACK
- acks=0: the producer will not wait for any acknowledgment from the server at all
- acks=1: the leader will write the record to its local log but will respond without awaiting full acknowledgement from all followers
- acks=all: the leader will wait for the full set of in-sync replicas to acknowledge the record

![Kafka ACK ALL](https://github.com/barneywill/bigdata_demo/blob/main/imgs/kafka_ack.jpg)

### 4.4 Consumer Offset
- __consumer_offsets topic
  - Format: ((group.id, topic, partition), offset)

![kafka Consumer Offset](https://github.com/barneywill/bigdata_demo/blob/main/imgs/kafka_consumer_offset.jpg)

### 4.5 Consumer Group Reblance
- group coordinator, group leader, assignment, consume, heart beat, rebalance
- assignment strategy: Range, Round robin, Sticky

![kafka Consumer Group](https://github.com/barneywill/bigdata_demo/blob/main/imgs/kafka_consumer_group.jpg)

https://developer.confluent.io/courses/architecture/consumer-group-protocol/