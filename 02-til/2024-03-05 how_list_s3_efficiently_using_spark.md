
# How to list AWS S3 files efficiently using Spark

[GIST](https://gist.github.com/raphaelmansuy/83c7ffb52c76f66fc8d235483f782f07)


```scala
import scala.collection.JavaConverters._

import com.amazonaws.services.s3.AmazonS3ClientBuilder

import com.amazonaws.services.s3.model.{ListObjectsV2Request, ListObjectsV2Result, S3ObjectSummary}

import org.apache.spark.sql.{DataFrame, SparkSession}

import org.apache.spark.sql.types.{StructType, StructField, StringType, TimestampType,LongType}

import org.apache.spark.sql.Row

  

/**

* Lists files from an S3 bucket and returns the results as a DataFrame.

* This function recursively lists all files under a specified S3 path prefix and constructs a DataFrame

* with details about each file, including the bucket name, ETag, file size, key, and last modified timestamp.

*

* @param s3Path The S3 path from which files will be listed. Expected format: "s3://bucket_name/path".

* @param awsRegion The AWS region where the S3 bucket is located. Defaults to "eu-west-1".

* @param spark Implicit SparkSession to be used for creating the DataFrame. Defaults to `spark`.

* @return DataFrame with columns for bucket name, ETag, file size, key, and last modified timestamp.

*

* Example of usage:

*

* ```scala

* import org.apache.spark.sql.SparkSession

*

* implicit val spark: SparkSession = SparkSession.builder()

* .appName("S3FileLister")

* .master("local")

* .getOrCreate()

*

* val s3Path = "s3://my-bucket/data"

* val awsRegion = "eu-west-1"

*

* // Call the function to list files from S3 and create a DataFrame

* val filesDF = listFiles(s3Path, awsRegion)

*

* // Show the result DataFrame

* filesDF.show()

* ```

*

* Note: This function requires AWS SDK for Java and SparkSession with appropriate configurations.

* Ensure that the AWS credentials are correctly configured in the environment.

*/

def listFiles(s3Path: String, awsRegion: String = "eu-west-1")(implicit spark: SparkSession = spark): DataFrame = {

// Extract the bucket name and prefix from the S3 path

val (bucket, prefix) = s3Path.replace("s3://", "").split("/", 2) match {

case Array(bucket, key @ _*) => (bucket, key.mkString("/"))

case _ => throw new IllegalArgumentException("Invalid S3 path format. Expected: s3://bucket_name/path")

}

  

// Initialize the S3 client

val s3Client = AmazonS3ClientBuilder.standard().withRegion(awsRegion).build()

  

// Schema for the dataframe

val schema = StructType(List(

StructField("bucket", StringType, nullable = false),

StructField("e_tag", StringType, nullable = false),

StructField("file_size",LongType, nullable = false),

StructField("key", StringType, nullable = false),

StructField("last_modified", TimestampType, nullable = false)

))

  

// Recursive function to list all files under a prefix

def listAllFiles(bucket: String, currentPrefix: String): Seq[Row] = {

val request = new ListObjectsV2Request()

.withBucketName(bucket)

.withPrefix(currentPrefix)

.withDelimiter("/")

.withMaxKeys(1000)

val files = scala.collection.mutable.Buffer[Row]()

  

var result: ListObjectsV2Result = null

do {

result = s3Client.listObjectsV2(request)

for (summary <- result.getObjectSummaries.asScala) {

files += Row(

bucket,

summary.getETag,

summary.getSize,

summary.getKey,

new java.sql.Timestamp(summary.getLastModified.getTime)

)

}

for (prefix <- result.getCommonPrefixes.asScala) {

files ++= listAllFiles(bucket, prefix)

}

request.setContinuationToken(result.getNextContinuationToken)

} while (result.isTruncated)

  

files

}

  

// Start the recursive listing at the initial prefix

val fileList = listAllFiles(bucket, prefix)

  

// Create a DataFrame from the list of Rows and the schema

val dataFrame = spark.createDataFrame(spark.sparkContext.parallelize(fileList), schema)

  

dataFrame

}
```
