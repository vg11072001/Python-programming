## Spark

### Pyspark Optimization Techniques
* [Apache Spark Cache and Persist](https://medium.com/@deepa.account/apache-spark-cache-and-persist-e2ea83c47d2f)
Lazy evaluation is a programming concept in Apache Spark that delays the evaluation of expressions until their results are needed. This technique is used to optimize data processing pipelines by minimizing unnecessary computations, improving resource utilization, and enhancing overall performance. 
In PySpark, lazy evaluation is used for transformations such as filter, map, and groupBy. When a transformation is called on a DataFrame or RDD, Spark records the transformation in a Directed Acyclic Graph (DAG) and only executes it when an action is called. For example, if you run a transformation to filter your dataframe (df.filter()) but Spark won't actually filter it until you run an action, such as showing your dataframe (df.show()). 
Lazy evaluation is especially useful for wide transformations, where the data required to be computed for a single partition may exist in multiple partitions. It can also reduce memory usage and provide more flexible computation

* [Spark Transformations, Actions and Lazy Evaluation.](https://www.linkedin.com/pulse/spark-transformations-actions-lazy-evaluation-mohammad-younus-jameel/)
* [How does PySpark work? — step by step (with pictures)](https://medium.com/analytics-vidhya/how-does-pyspark-work-step-by-step-with-pictures-c011402ccd57)
* 

### Spark Architecture, [Intro](https://blog.devgenius.io/setup-pyspark-locally-build-your-first-etl-pipeline-with-pyspark-91c3060c6133)
![image](https://github.com/vg11072001/Python-programming/assets/67424390/eef3adfe-4268-4fd2-ba44-6ebfe330078f)

![image](https://github.com/vg11072001/Python-programming/assets/67424390/62030424-afba-40e1-b52c-cab98442a94b)

Spark is written in Scala, but it provides APIs for other mainstream languages such as Java, Python and R — PySpark is the Python API. 
It also supports other tools and languages including Spark SQL for SQL, pandas API on Spark for pandas workloads, and Structured Streaming for incremental computation and stream processing.


## Pyspark


### PySpark Architecture 

Apache Spark has a master/slave architecture where the master is called the “Driver” and slaves are called “Workers”.

![image](https://github.com/vg11072001/Python-programming/assets/67424390/e18c335b-361a-42a4-97f6-f632f3211061)


### Concept and Structure
* Application: propgram built using APIs, driver & excutor
* SparkSession: Crete spark driver, intitaes sesssion and during it own spark objects (Driver is part of spark shell)
* Job: parallel comptutaion, it gets distributed
* Stage
* Task: Single unit of work

![image](https://github.com/vg11072001/Python-programming/assets/67424390/f6a8778b-9c95-47ca-b1c8-0d7f9c4e6c62)

###### Application to Mutiple job using Driver 

![image](https://github.com/vg11072001/Python-programming/assets/67424390/28ca126e-62ad-4440-87e0-15208bb27b39)

### PySpark Features
* In-memory computation
* Distributed processing using parallelize
* Can be used with many cluster managers (Spark, Yarn, Mesos e.t.c)
* Fault-tolerant
* Immutable
* Lazy evaluation
* Cache & persistence
* Inbuild-optimization when using DataFrames
* Supports ANSI SQL

###### Tranforms, Actions and Lazy Evaluation

![image](https://github.com/vg11072001/Python-programming/assets/67424390/3794cc6a-ee9e-4540-a5d2-d43ee25ea63a)

![image](https://github.com/vg11072001/Python-programming/assets/67424390/3ec26e8f-88f7-4a3a-9eab-6ae5eb52afcd)

### PySpark Modules & Packages
* PySpark RDD (pyspark.RDD)
* PySpark DataFrame and SQL (pyspark.sql)
* PySpark Streaming (pyspark.streaming)
* PySpark MLib (pyspark.ml, pyspark.mllib)
* PySpark GraphFrames (GraphFrames)
* PySpark Resource (pyspark.resource) It’s new in PySpark 3.0

#### Spark UI (holistic view of your applications, to easliy monitor)
* List of scheduler stages and tasks
* Summary of RDD sizes and memory usage
* Information about the environment
* Information about the running executors
* All Spark SQL queries

#### RDD (Resilient Distributed Datasets)


![image](https://github.com/vg11072001/Python-programming/assets/67424390/a5133bc8-a941-4c58-a80f-ba880409183f)


### Pandas vs Pyspark

Below are the few considerations when to choose PySpark over Pandas:
* If your data is huge and grows significantly over the years and you wanted to improve your processing time.
* If you want fault-tolerant.
* ANSI SQL compatibility.
* Language to choose (Spark supports Python, Scala, Java & R)
* When you want Machine-learning capability.
* Would like to read Parquet, Avro, Hive, Casandra, Snowflake e.t.c
* If you wanted to stream the data and process it real-time.

### Code 

#### 1 start

SparkAPP

![image](https://github.com/vg11072001/Python-programming/assets/67424390/ea57f370-0a3c-489a-86a3-df52837172c2)
![image](https://github.com/vg11072001/Python-programming/assets/67424390/588a3c5c-47b6-4c4e-86c1-911dc78c99c4)



## Reference:
* [Latest Spark- From/to pandas and PySpark DataFrames](https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/pandas_pyspark.html)
* [PySpark vs Pandas: Performance, Memory Consumption and Use Cases](https://www.codeconquest.com/blog/pyspark-vs-pandas-performance-memory-consumption-and-use-cases/)
* [Pandas vs PySpark..!](https://medium.com/geekculture/pandas-vs-pyspark-fe110c266e5c)
* [PySpark UDF (User Defined Function)](https://sparkbyexamples.com/pyspark/pyspark-udf-user-defined-function/)
* [Spark SQL Built-in Standard Functions](https://sparkbyexamples.com/spark/spark-sql-functions/)
* https://github.com/hnawaz007/pythondataanalysis/tree/main
* 
