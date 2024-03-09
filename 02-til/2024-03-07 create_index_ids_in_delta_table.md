https://gist.github.com/raphaelmansuy/0de7dd411cc04d2d912d6b4bf11002e9

## Function: create_index_delta

This function is designed to create and update a Delta table by processing JSON files stored in Amazon S3. It performs several steps to filter the files based on their size, construct S3 paths, process the JSON files in chunks, and append the results to the Delta table.

### Problem

When dealing with a large number of JSON files stored in Amazon S3, it can be challenging to efficiently process and update a Delta table with the data from these files. The `create_index_delta` function solves this problem by providing a scalable and optimized approach to filter, process, and append JSON data to a Delta table.

### Approach

1. **File Size Filtering**: The function filters the input `filesDataFrame` to exclude files with a file size less than or equal to zero. This ensures that only valid files are processed.

2. **Construct S3 Paths**: Using the filtered file information, the function constructs S3 paths for each file by concatenating the bucket and key information.

3. **JSON File Processing**: The function builds a Spark schema based on the provided keys. It then reads the JSON files from the constructed S3 paths in chunks without collecting them on the driver. The function uses a chunk size of 100,000 for efficient processing.

4. **Delta Table Initialization**: The function checks if the Delta table at `s3PathDeltaTableOut` exists. If it does not exist, it initializes the Delta table with an empty DataFrame using the provided schema.

5. **Delta Table Processing**: The function initializes a DeltaTable object for the `s3PathDeltaTableOut` and iterates over the chunks of S3 paths. For each chunk, it reads the JSON files using the provided schema and appends the processed data to the Delta table using the "append" mode.

6. **Completion Message**: After processing all the chunks, the function prints a completion message indicating the total number of processed chunks.

### Usage

```scala
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.DataFrame

// Example usage
val spark = SparkSession.builder().appName("MyApp").getOrCreate()

val filesDataFrame: DataFrame = // Provide your DataFrame of file information
val keys: Seq[String] = // Provide the keys used to construct the schema
val s3PathDeltaTableOut: String = // Provide the output path for the Delta table

create_index_delta(filesDataFrame, keys, s3PathDeltaTableOut)(spark)
```

Note: The function assumes that the necessary Spark and Delta libraries are already imported and available in the environment.

```scala
import org.apache.spark.sql.{DataFrame, SparkSession, Dataset, Row}

import org.apache.spark.sql.functions.{col, input_file_name}

import org.apache.spark.sql.types.{StringType, StructField, StructType}

import scala.collection.JavaConverters._

import io.delta.tables._

  

// Define a case class to represent the FileInfo after filtering

case class FileInfo(file_size: BigInt, bucket: String, key: String)

  

def create_index_delta(filesDataFrame: DataFrame, keys: Seq[String], s3PathDeltaTableOut: String)(implicit spark: SparkSession = spark): Unit = {

import spark.implicits._

  

// Step 1: File Size Filtering

val fileInfoDS: Dataset[FileInfo] = filesDataFrame

.filter(col("file_size") > 0)

.as[FileInfo]

  

// Step 2: Construct S3 paths from FileInfo

val s3Paths = fileInfoDS.map(fileInfo => s"s3://${fileInfo.bucket}/${fileInfo.key}")

  

// Step 3: JSON File Processing

// Build a Spark Schema using only the keys

val fields = keys.map { key =>

key.split("\\.").foldRight[StructType](new StructType()) {

(name, struct) => new StructType().add(StructField(name, StringType))

}.fields.head

}

// Add the source_file_name field to the schema

val schema = StructType(fields :+ StructField("input_file_name", StringType))

  

// Step 4: Read the JSON files from the constructed S3 paths in chunks without collecting them on the driver

val chunkSize = 100000

// Convert the Dataset to an Iterator and then to a Scala Iterator

val s3PathsIterator = s3Paths.toLocalIterator.asScala

val s3PathsChunks = s3PathsIterator.grouped(chunkSize)

  

// Check if the Delta table exists and initialize it if it does not

val deltaTableExists = DeltaTable.isDeltaTable(spark, s3PathDeltaTableOut)

if (!deltaTableExists) {

// Initialize the Delta table with an empty DataFrame

val emptyDf = spark.createDataFrame(spark.sparkContext.emptyRDD[Row], schema)

emptyDf.write.format("delta").mode("overwrite").save(s3PathDeltaTableOut)

}

  

// Reinitialize the Delta Table for each call

val deltaTable = DeltaTable.forPath(spark, s3PathDeltaTableOut)

  

// Initialize a counter for chunk progression

var chunkCounter = 0

  

// Process each chunk and append to the Delta Table

s3PathsChunks.foreach { pathsChunk =>

// Increment and print the chunk counter

chunkCounter += 1

println(s"Processing chunk $chunkCounter...")

  

val chunkDf = spark.read.schema(schema).json(pathsChunk.toSeq: _*).withColumn("input_file_name", input_file_name())

// Append the result to the Delta Table

chunkDf.write.format("delta").mode("append").save(s3PathDeltaTableOut)

}

  

// Print completion message

println(s"Completed processing ${chunkCounter} chunks.")

}
	```

https://gist.github.com/raphaelmansuy/0de7dd411cc04d2d912d6b4bf11002e9
