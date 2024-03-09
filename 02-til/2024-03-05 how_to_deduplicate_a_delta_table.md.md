# How to deduplicate a DeltaTable in scala

## Function: deleteDuplicateRows

The `deleteDuplicateRows` function is designed to remove duplicate rows from a Delta table in Scala. It takes the path to the Delta table, a sequence of column names used to identify duplicates, and an optional column name that contains the timestamp of the last update.

### Problem

Duplicate rows in a Delta table can lead to data inconsistencies and inefficiencies. It is important to identify and remove these duplicate rows to maintain data integrity and optimize data processing.

### Approach

The `deleteDuplicateRows` function uses the DeltaTable API and Spark SQL to perform the deduplication process. Here is a high-level overview of the approach:

1. Load the Delta table using the provided path.
2. Construct the merge condition by comparing the specified keys between the target and source tables.
3. If an `updatedAtColumn` is provided, find the latest updated timestamp for each set of duplicate keys using Spark SQL aggregation.
4. Register the resulting DataFrame as a temporary view.
5. Construct the full SQL command for the merge operation, specifying the target table, source table, merge condition, and delete action for matched rows.
6. Execute the merge operation using Spark SQL.
7. Clean up the temporary view.
8. Return the resulting DataFrame representing the Delta table after duplicate rows have been deleted.

### Usage Example

Here is an example of how to use the `deleteDuplicateRows` function:

```scala
import org.apache.spark.sql.SparkSession

implicit val spark: SparkSession = SparkSession.builder()
  .appName("DeltaTableDuplicateRemoval")
  .master("local")
  .getOrCreate()

val deltaTablePath = "/path/to/delta/table"
val keys = Seq("id", "name")
val updatedAtColumn = Some("updated_at")

// Call the function to delete duplicate rows
val cleanedDF = deleteDuplicateRows(deltaTablePath, keys, updatedAtColumn)

// Show the result DataFrame
cleanedDF.show()
```

Note that this function requires a Delta table and a SparkSession with Delta support enabled.

For more details, you can refer to the [original Gist](https://gist.github.com/raphaelmansuy/4590176b9ff05c781f95d9a853e1d2d4).



```scala
import io.delta.tables._

import org.apache.spark.sql.{SparkSession,DataFrame}

import org.apache.spark.sql.functions._

  
  

/**

* Deletes duplicate rows from a Delta table based on specified keys and an optional `updatedAt` column.

* This function identifies duplicates by matching rows on the specified keys. If an `updatedAtColumn` is provided,

* it retains only the most recent row for each set of duplicate keys based on the `updatedAt` timestamp.

*

* @param deltaTablePath The path to the Delta table from which duplicates will be removed.

* @param keys A sequence of strings representing the column names used to identify duplicates.

* @param updatedAtColumn An optional string specifying the column name that contains the timestamp of the last update.

* If provided, the function uses this column to determine the most recent row among duplicates.

* @param spark Implicit SparkSession to be used for executing Spark SQL commands. Defaults to `spark`.

* @return DataFrame representing the Delta table after duplicate rows have been deleted.

*

* Example of usage:

*

* ```scala

* import org.apache.spark.sql.SparkSession

*

* implicit val spark: SparkSession = SparkSession.builder()

* .appName("DeltaTableDuplicateRemoval")

* .master("local")

* .getOrCreate()

*

* val deltaTablePath = "/path/to/delta/table"

* val keys = Seq("id", "name")

* val updatedAtColumn = Some("updated_at")

*

* // Call the function to delete duplicate rows

* val cleanedDF = deleteDuplicateRows(deltaTablePath, keys, updatedAtColumn)

*

* // Show the result DataFrame

* cleanedDF.show()

* ```

*

* Note: This function requires a Delta table and SparkSession with Delta support enabled.

*/

def deleteDuplicateRows(deltaTablePath: String, keys: Seq[String], updatedAtColumn: Option[String])(implicit spark: SparkSession = spark): DataFrame = {

  

// Load the Delta table as a DeltaTable

val deltaTable = DeltaTable.forPath(spark, deltaTablePath)

  

// Construct the merge condition

val matchCondition = keys.map(key => s"target.$key = source.$key").mkString(" AND ")

val conditionWithUpdated = updatedAtColumn.map(colName => s" AND target.$colName < source.latest_updated_at").getOrElse("")

  

// Use Spark SQL to find the latest updated_at for each composite key if provided

val latestUpdatesDF = updatedAtColumn match {

case Some(columnName) =>

deltaTable.toDF

.groupBy(keys.map(col): _*)

.agg(max(col(columnName)).alias("latest_updated_at"))

case None =>

deltaTable.toDF

}

  

// Register the DataFrame as a temporary view

latestUpdatesDF.createOrReplaceTempView("latest_updates")

  

// Construct the full SQL command for the merge operation

val sqlMergeCmd = s"""

MERGE INTO delta.`$deltaTablePath` AS target

USING latest_updates AS source

ON $matchCondition$conditionWithUpdated

WHEN MATCHED THEN DELETE

"""

  

// Execute the merge operation

spark.sql(sqlMergeCmd)

  

// Clean up temporary view

spark.catalog.dropTempView("latest_updates")

  

deltaTable.toDF

  

}
```


https://gist.github.com/raphaelmansuy/4590176b9ff05c781f95d9a853e1d2d4
