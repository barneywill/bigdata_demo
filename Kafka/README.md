

# Topic
```
# list all topics
bin/kafka-topics.sh --bootstrap-server $kafka_ip:9092 --list

# create a topic
bin/kafka-topics.sh --bootstrap-server $kafka_ip:9092 --create --partitions 2 --topic $topic_name

# delete a topic
bin/kafka-topics.sh --bootstrap-server $kafka_ip:9092 --delete --topic $topic_name
```

# Producer
```
# produce messages to a topic from a file
bin/kafka-console-producer.sh --bootstrap-server $kafka_ip:9092 --topic $topic_name < $file_path
```

# Consumer
```
# comsume messages from a topic
bin/kafka-console-consumer.sh --bootstrap-server $kafka_ip:9092 --topic $topic_name --from-beginning

# check consumer group offset
bin/kafka-consumer-groups.sh --bootstrap-server 192.168.4.50:9092 --group test --describe
```