# Malloy: A Composable Query Language for Nested Data

Malloy is an experimental query language designed to address the limitations of SQL, especially when working with nested, non-rectangular data. Unlike SQL, which was built for flat, tabular data and prioritizes natural language-like syntax over composability, Malloy is built from the ground up for composability and flexibility.

## Key Features
- **Queries nested data structures easily**: Directly query nested data without reshaping into tables.
- **Compiles to efficient SQL**: Malloy queries are compiled down to performant SQL for execution on modern databases.
- **Reusable data sources**: Define joins, measures, and logic once and reuse them across queries.
- **Integrated with DuckDB, BigQuery, Postgres**: Works with popular data engines.
- **VSCode extension**: Developer tooling for a better experience.

## Composability in Malloy
Malloy is designed for composability, making it easy to build complex queries from simple, reusable components:
- **Everything is a reusable component**: Queries, aggregates, and measures can be nested and combined.
- **Explicit relationships**: Define relationships between entities once and reuse them.
- **Dimensional flexibility**: Compute aggregates at multiple levels of granularity in a single query.
- **Nested queries**: Compose logic by nesting queries recursively.
- **Separation of measure and dimension**: Measures are independent from grouping/filtering, making them highly reusable.
- **Parameterization**: Any part of a query can be parameterized for reuse.

### Example: Composable Malloy Query
```malloy
// Reusable measure
revenue = sum(order.amount)

// Query to get revenue by category
q1 = group by order.category {
  category_revenue = revenue
}

// Reuse q1 in a larger query
q2 = group by customer.state {
  state_revenue = revenue
  by_category = group by order.category {
    category_revenue = revenue
  }
  top_categories = top(q1, 3, category_revenue)
}
```

## SQL vs. Malloy
While SQL is powerful, it is less composable:
- Queries are monolithic and hard to break into reusable units.
- Join logic must be repeated in every query.
- Aggregates often require reshaping data with `GROUP BY`.
- Parameters are limited to values, not query components.
- Analytics functions are not easily reusable.

Malloy overcomes these limitations by making all logic modular and composable.

## Getting Started
1. **Install DuckDB and Malloy DuckDB plugin:**
   ```sh
   pip install duckdb
   pip install malloy-duckdb
   ```
2. **Run a simple Malloy query:**
   ```malloy
   run: duckdb.table('data.csv') -> {
     select: name, age
   }
   ```

## Resources
- [Malloy Documentation](https://docs.malloydata.dev/documentation)
- VSCode Extension for Malloy
- Community integrations: DBT, Airflow, Spark, and more

Malloy is a powerful tool for incrementally building complex data logic, especially when working with modern, nested data sources.
