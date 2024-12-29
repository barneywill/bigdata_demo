# JVM

## Commands
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