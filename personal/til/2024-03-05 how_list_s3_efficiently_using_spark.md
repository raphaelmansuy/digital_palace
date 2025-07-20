# TIL: How to List AWS S3 Files Efficiently Using Spark (2024-03-05)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Efficient S3 file listing with Spark** – Use a custom Scala function to recursively list S3 files and return a Spark DataFrame for analysis.

---

## The Pain Point

Listing files in large S3 buckets is slow and error-prone with standard tools. Manual iteration and pagination are complex. This Spark-based approach is fast, scalable, and integrates with DataFrames for further analysis.

---

## Step-by-Step Guide

### Function Summary

The `listFiles` function efficiently lists files from an AWS S3 bucket and returns the results as a DataFrame using Apache Spark. It recursively lists all files under a specified S3 path prefix and provides details about each file, including the bucket name, ETag, file size, key, and last modified timestamp.

### Parameters

- `s3Path`: The S3 path from which files will be listed. Format: `s3://bucket_name/path`.
- `awsRegion` (optional): The AWS region where the S3 bucket is located. Defaults to `eu-west-1`.
- `spark` (implicit): Implicit SparkSession for creating the DataFrame.

### Usage Example

```scala
import org.apache.spark.sql.SparkSession

implicit val spark: SparkSession = SparkSession.builder()
  .appName("S3FileLister")
  .master("local")
  .getOrCreate()

val s3Path = "s3://my-bucket/data"
val awsRegion = "eu-west-1"

val filesDF = listFiles(s3Path, awsRegion)
filesDF.show()
```

### Notes

- Requires AWS SDK for Java and SparkSession with appropriate configurations.
- Ensure AWS credentials are correctly configured in the environment.

---

## Implementation

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

---

## Troubleshooting

- If no files are returned, check your AWS credentials and bucket permissions.
- For performance issues, increase `maxKeys` or run on a cluster.
- See [AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/) and [Spark documentation](https://spark.apache.org/docs/latest/) for advanced usage.

---

## Security Considerations

- Never hardcode AWS credentials; use environment variables or IAM roles.
- Limit S3 bucket permissions to least privilege.
- Review DataFrame contents before sharing or exporting sensitive data.

---

## Related Resources

- [AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/)
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Scala AWS S3 Examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3)

---

*⚡ Pro tip: Use Spark DataFrames for downstream analytics and automate S3 file listing in ETL pipelines!*
