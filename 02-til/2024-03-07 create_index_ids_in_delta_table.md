https://gist.github.com/raphaelmansuy/0de7dd411cc04d2d912d6b4bf11002e9


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
