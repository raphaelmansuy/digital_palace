# TIL: How to Deduplicate a DeltaTable in Scala (2024-03-05)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Efficient Delta Lake deduplication in Scala** – Use a custom function to remove duplicate rows from Delta tables using Spark SQL and DeltaTable API.

---

## The Pain Point

Duplicate rows in Delta tables cause data inconsistencies and slow down analytics. Manual deduplication is error-prone and inefficient. This function automates deduplication using Spark and Delta Lake APIs.

---

## Step-by-Step Guide

### Function Summary

The `deleteDuplicateRows` function removes duplicate rows from a Delta table in Scala. It takes the path to the Delta table, a sequence of column names used to identify duplicates, and an optional column name for the last update timestamp.

### Usage Example

```scala
import org.apache.spark.sql.SparkSession

implicit val spark: SparkSession = SparkSession.builder()
  .appName("DeltaTableDuplicateRemoval")
  .master("local")
  .getOrCreate()

val deltaTablePath = "/path/to/delta/table"
val keys = Seq("id", "name")
val updatedAtColumn = Some("updated_at")

val cleanedDF = deleteDuplicateRows(deltaTablePath, keys, updatedAtColumn)
cleanedDF.show()
```

---

## Implementation

```scala
import io.delta.tables._
import org.apache.spark.sql.{SparkSession, DataFrame}
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

---

## Troubleshooting

- If duplicates remain, check your key columns and ensure `updatedAtColumn` is correct.
- For merge errors, verify Delta support is enabled in Spark.
- See [Delta Lake documentation](https://docs.delta.io/latest/delta-batch.html) for advanced usage.

---

## Security Considerations

- Never run merge/delete operations on production tables without backups.
- Limit permissions for users running Spark SQL commands.
- Review DataFrame contents before sharing or exporting sensitive data.

---

## Related Resources

- [Delta Lake Documentation](https://docs.delta.io/latest/delta-batch.html)
- [Spark SQL Documentation](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [DeltaTable API Reference](https://docs.delta.io/latest/api/scala/io/delta/tables/DeltaTable.html)
- [Original Gist](https://gist.github.com/raphaelmansuy/4590176b9ff05c781f95d9a853e1d2d4)

---

*⚡ Pro tip: Use the `updatedAt` column to keep only the latest version of each record for robust deduplication!*
