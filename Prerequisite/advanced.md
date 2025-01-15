# Advanced

| |Index|
|---|---|
|1|[CAP](#cap)|
|2|[Transaction](#transaction)|
|3|[WAL(Write Ahead Log)](#wal)|
|4|[Paxos](#paxos)|
|5|[Quorum](#quorum)|
|6|[Leader and Followers](#leader)|
|7|[Generation Clock](#clock)|
|8|[Log](#log)|
|9|[SkipList](#skiplist)|
|10|[Write & Flush](#flush)|

## <a id='cap'></a>1 CAP
Any distributed data store can provide only two of the following three guarantees:
- Consistency: Every read receives the most recent write or an error.
- Availability: Every request received by a non-failing node in the system must result in a response.
- Partion Tolerance: The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.

Example: 
- HBase: CP
- Kafka: CP or AP
  - replication.factor
  - min.insync.replicas
  - replica.lag.time.max.ms
  - unclean.leader.election.enable


## <a id='transaction'></a>2 Transaction
A transaction is any operation that is treated as a single unit of work, which either completes fully or does not complete at all, and leaves the storage system in a consistent state.
### ACID
- Atomicity: each statement in a transaction (to read, write, update or delete data) is treated as a single unit.
- Consistency: ensures that transactions only make changes to tables in predefined, predictable ways.
- Isolation: when multiple users are reading and writing from the same table all at once, isolation of their transactions ensures that the concurrent transactions don't interfere with or affect one another.
- Durability: ensures that changes to your data made by successfully executed transactions will be saved, even in the event of system failure.

### Two-phase commit
Update resources on multiple nodes in one atomic operation.
- coordinator
- phase 1
- phase 2

https://martinfowler.com/articles/patterns-of-distributed-systems/two-phase-commit.html

## <a id='wal'></a>3 WAL(Write Ahead Log)
Provide durability guarantee without the storage data structures to be flushed to disk, by persisting every state change as a command to the append only log.

https://martinfowler.com/articles/patterns-of-distributed-systems/wal.html

### 3.1 Segmented Log
Split log into multiple smaller files instead of a single large file for easier operations.

https://martinfowler.com/articles/patterns-of-distributed-systems/log-segmentation.html

### 3.2 Replicated Log
Keep the state of multiple nodes synchronized by using a write-ahead log that is replicated to all the cluster nodes.

https://martinfowler.com/articles/patterns-of-distributed-systems/replicated-log.html

### 3.3 High-Water Mark
An index in the write ahead log showing the last successful replication.

https://martinfowler.com/articles/patterns-of-distributed-systems/high-watermark.html

### 3.4 Low-Water Mark
An index in the write ahead log showing which portion of the log can be discarded.

https://martinfowler.com/articles/patterns-of-distributed-systems/low-watermark.html

## <a id='paxos'></a>4 Paxos
Use two consensus building phases to reach safe consensus even when nodes disconnect

https://martinfowler.com/articles/patterns-of-distributed-systems/paxos.html

## <a id='quorum'></a>5 Quorum
Avoid two groups of servers making independent decisions, by requiring majority for taking every decision.

https://martinfowler.com/articles/patterns-of-distributed-systems/quorum.html

## <a id='leader'></a>6 Leader and Followers
Have a single server to coordinate replication across a set of servers.

https://martinfowler.com/articles/patterns-of-distributed-systems/leader-follower.html

## <a id='clock'></a>7 Generation Clock
A monotonically increasing number indicating the generation of the server.

https://martinfowler.com/articles/patterns-of-distributed-systems/generation.html

## <a id='log'></a>8 Log

### 8.1 The Log: What every software engineer should know about real-time data's unifying abstraction
https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying

### 8.2 On Disk IO, Part 1: Flavors of IO
https://medium.com/databasss/on-disk-io-part-1-flavours-of-io-8e1ace1de017

### 8.2 On Disk IO, Part 2: More Flavours of IO
https://medium.com/databasss/on-disk-io-part-2-more-flavours-of-io-c945db3edb13

## 9 <a id='skiplist'></a>SkipList

https://www.epaperpress.com/sortsearch/download/skiplist.pdf

![SkipList](https://github.com/barneywill/bigdata_demo/blob/main/imgs/skiplist.jpg)

## 10 <a id='flush'></a>Write & Flush
- sync: sync the whole OS
- fsync: flush the file from kernel buffer to the disk
  - fsync() transfers ("flushes") all modified in-core data of (i.e., modified buffer cache pages for) the file referred to by the file descriptor fd to the disk device (or other permanent storage device) so that all changed information can be retrieved even after the system crashed or was rebooted. 
- fdatasync

Normally, the data already written by the application into a kernel buffer with write() will not be affected by the application exiting or getting killed in any way. Exiting or getting killed implicitly closes all file descriptors, so there should be no difference, the kernel will handle the flushing afterwards. So no fdatasync() or similar calls are neccessary.

if the application uses user-land buffering (not calling the write() system call, but instead caching the data in a user-space buffer, with fwrite()), those buffers might not get flushed unless a proper user-space file close is executed - getting killed by a SIGKILL will definitely cause you to lose the contents of those buffers,

if the kernel dies as well (loss of power, kernel crash, etc.), your data might have missed getting written to the disks from the kernel buffers, and will then get lost.

