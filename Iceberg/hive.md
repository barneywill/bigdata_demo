# Hive

![Hive Architecture](https://github.com/barneywill/bigdata_demo/blob/main/imgs/hive_architecture.jpg)

## 1 Problems
data in the table is tracked at the folder level
- Changes to the data are inefficient
  - copy and write on partition level
- There’s no way to safely change data in multiple partitions as part of one operation
- In practice, multiple jobs modifying the same dataset isn’t a safe operation
- All of the directory listings needed for large tables take a long time
- Users have to know the physical layout of the table
  - use where to prune partitions
- Hive table statistics are usually stale
- The filesystem layout has poor performance on cloud object storage

