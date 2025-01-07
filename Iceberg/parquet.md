# Parquet

- Parquet is built from the ground up with complex nested data structures in mind, and uses the record shredding and assembly algorithm described in the Dremel paper. 
- Parquet is built to support very efficient compression and encoding schemes. 

## 1 Hierarchy
- file -> row groups -> column chunks -> pages(data/index/dictionary)

![parquet](https://github.com/barneywill/bigdata_demo/blob/main/imgs/parquet.jpg)


Version 1.2 supports run-length and dictionary encodings and version 2.0 added support for delta and optimized string encodings. The most recent version (Parquet 2.0) also implements embedded statistics: inlined column statistics for further optimization of scan efficiency, e.g. min/max indexes.
