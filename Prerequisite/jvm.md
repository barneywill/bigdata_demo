# JVM

Java and Scala programs are running on JVM(Java Virtual Machine).

Apache Spark and Kafka are writen by Scala. Nifi and Iceberg are writen by Java. (Also Flink, Hadoop, Hive, HBase, Zookeeper, Oozie, and Elasticsearch are writen by Java)

## 1 Commands
```
# show all java processes
jps

# show java heap
jmap -heap $pid

# show objects in java heap
jmap -histo $pid

# dump java heap
jmap -dump:format=b,file=test.dump $pid

# analyze java heap dump
jhat test.dump
or
Memory Analyzer：http://www.eclipse.org/mat/

# show garbage collection state
jstat -gcutil $pid

# show all threads in a process
jstack $pid

# show class signature
javap -cp $jar_path $class_name

# show all files in a jar
vim $jar_name
or
unzip -l $jar_name
```

## 2 GC (Garbage Collection)
- Serial
- Parallel
- CMS
- G1, from 9
- ZGC, from 15

![GC](https://github.com/barneywill/bigdata_demo/blob/main/imgs/gc.jpg)
