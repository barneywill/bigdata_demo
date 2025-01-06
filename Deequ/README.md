# Deequ

Deequ is a library built on top of Apache Spark for defining "unit tests for data", which measure data quality in large datasets. 

## 1 Install

#### Put it under $SPARK_HOME/jars
https://repo1.maven.org/maven2/com/amazon/deequ/deequ/2.0.8-spark-3.5/deequ-2.0.8-spark-3.5.jar

## 2 Scenario

<a href='https://github.com/barneywill/bigdata_demo/blob/main/Deequ/DeequSparkTest.scala' target='_blank'>DeequSparkTest.scala</a>

### 2.1 Data Profiling
Deequ supports single-column profiling of such data and its implementation scales to large datasets with billions of rows. 
- completeness
- approximateNumDistinctValues
- dataType

### 2.2 Anomaly Detection
Check the change of the size of a dataset every day to ensure it does not change drastically.
- the number of rows on a given day should not be more than double of what we have seen on the day before.

### 2.3 Automatic Suggestion of Constraints
Automatic constraint suggestion first profiles the data and then applies a set of heuristic rules to suggest constraints.
- description: 'valuable' has less than 62% missing values
- codeForConstraint: .hasCompleteness("valuable", _ >= 0.38, Some("It should be above 0.38!"))

### 2.4 Storing Computed Metrics in a MetricsRepository
Deequ allows us to persist the metrics we computed on dataframes in a so-called MetricsRepository. 
- the ability to save the result and query it like a DataFrame

