# Parquet

- Parquet is built from the ground up with complex nested data structures in mind, and uses the record shredding and assembly algorithm described in the Dremel paper. 
- Parquet is built to support very efficient compression and encoding schemes. 

## 1 Hierarchy
- file -> row groups -> column chunks -> pages(data/index/dictionary)

![parquet](https://github.com/barneywill/bigdata_demo/blob/main/imgs/parquet.jpg)
