# Mastering Typesense: A Comprehensive, Example-Driven Tutorial for the Impatient

## Table of Contents

1. [Introduction to Typesense](#introduction-to-typesense)
2. [Setting Up Typesense](#setting-up-typesense)
3. [Basic Operations](#basic-operations)
4. [Advanced Searching](#advanced-searching)
5. [Faceted Search](#faceted-search)
6. [Geosearch](#geosearch)
7. [Sorting and Ranking](#sorting-and-ranking)
8. [Synonyms and Typo Tolerance](#synonyms-and-typo-tolerance)
9. [Curation and Merchandising](#curation-and-merchandising)
10. [Performance Optimization](#performance-optimization)
11. [Scaling and High Availability](#scaling-and-high-availability)
12. [Security and Access Control](#security-and-access-control)
13. [Monitoring and Analytics](#monitoring-and-analytics)
14. [Integrations and Extensions](#integrations-and-extensions)
15. [Conclusion](#conclusion)

## Introduction to Typesense

Typesense is a fast, typo-tolerant search engine designed for easy setup and use. It's an open-source alternative to Algolia and a modern alternative to ElasticSearch.

Key features:
- Typo tolerance
- Fast (millisecond) searches
- Sorting and faceting
- Geosearch

Let's dive right into the code!

## Setting Up Typesense

First, install Typesense using Docker:

```bash
docker run -p 8108:8108 -v/tmp/data:/data typesense/typesense:0.24.1 \
  --data-dir /data --api-key=xyz
```

Now, let's set up a TypeScript project and install the Typesense client:

```bash
npm init -y
npm install typesense
npm install -D typescript @types/node
```

Create a `tsconfig.json` file:

```json
{
  "compilerOptions": {
    "target": "es6",
    "module": "commonjs",
    "outDir": "./dist",
    "strict": true,
    "esModuleInterop": true
  }
}
```

## Basic Operations

Let's start with basic CRUD operations:

```typescript
import Typesense from 'typesense';

const client = new Typesense.Client({
  nodes: [{ host: 'localhost', port: 8108, protocol: 'http' }],
  apiKey: 'xyz',
});

// Create a collection
async function createCollection() {
  const schema = {
    name: 'books',
    fields: [
      { name: 'title', type: 'string' },
      { name: 'author', type: 'string' },
      { name: 'year', type: 'int32' },
    ],
    default_sorting_field: 'year',
  };

  await client.collections().create(schema);
}

// Index a document
async function indexDocument() {
  const document = {
    title: 'The Catcher in the Rye',
    author: 'J.D. Salinger',
    year: 1951,
  };

  await client.collections('books').documents().create(document);
}

// Search for documents
async function searchDocuments() {
  const searchParameters = {
    q: 'catcher',
    query_by: 'title',
  };

  const searchResult = await client.collections('books').documents().search(searchParameters);
  console.log(searchResult);
}

// Update a document
async function updateDocument() {
  const updatedDocument = {
    title: 'The Catcher in the Rye',
    author: 'Jerome David Salinger',
    year: 1951,
  };

  await client.collections('books').documents('document_id').update(updatedDocument);
}

// Delete a document
async function deleteDocument() {
  await client.collections('books').documents('document_id').delete();
}

// Run the functions
(async () => {
  await createCollection();
  await indexDocument();
  await searchDocuments();
  await updateDocument();
  await deleteDocument();
})();
```

## Advanced Searching

Typesense offers powerful search capabilities. Let's explore some advanced features:

```typescript
async function advancedSearch() {
  const searchParameters = {
    q: 'science fiction',
    query_by: 'title,author,tags',
    filter_by: 'year:>2000',
    sort_by: 'year:desc',
    prefix: true,
    num_typos: 2,
    page: 1,
    per_page: 10,
  };

  const searchResult = await client.collections('books').documents().search(searchParameters);
  console.log(searchResult);
}
```

This search query demonstrates:
- Multi-field search
- Filtering
- Sorting
- Prefix matching
- Typo tolerance
- Pagination

## Faceted Search

Faceted search allows users to narrow down search results by categories:

```typescript
async function facetedSearch() {
  const searchParameters = {
    q: 'fiction',
    query_by: 'title,author,tags',
    facet_by: 'tags,year',
    max_facet_values: 10,
  };

  const searchResult = await client.collections('books').documents().search(searchParameters);
  console.log(searchResult.facet_counts);
}
```

## Geosearch

Typesense supports geosearch for location-based queries:

```typescript
async function geoSearch() {
  const searchParameters = {
    q: '*',
    query_by: 'title',
    filter_by: 'location:(45.4723, -75.7014, 100 km)',
    sort_by: 'location(45.4723, -75.7014):asc',
  };

  const searchResult = await client.collections('locations').documents().search(searchParameters);
  console.log(searchResult);
}
```

## Sorting and Ranking

Customize result ranking with field-specific boosts:

```typescript
async function customRanking() {
  const searchParameters = {
    q: 'bestseller',
    query_by: 'title,author',
    sort_by: '_text_match:desc,year:desc',
    query_by_weights: '2,1',
  };

  const searchResult = await client.collections('books').documents().search(searchParameters);
  console.log(searchResult);
}
```

## Synonyms and Typo Tolerance

Improve search relevance with synonyms and typo tolerance:

```typescript
async function setupSynonyms() {
  const synonyms = {
    smartphone: ['iphone', 'android', 'mobile phone'],
  };

  await client.collections('products').synonyms().upsert('smartphone-synonyms', synonyms);
}

async function searchWithSynonyms() {
  const searchParameters = {
    q: 'smartphone',
    query_by: 'name,description',
    use_synonyms: true,
    num_typos: 2,
  };

  const searchResult = await client.collections('products').documents().search(searchParameters);
  console.log(searchResult);
}
```

## Curation and Merchandising

Boost specific products or pin results:

```typescript
async function curatedSearch() {
  const searchParameters = {
    q: 'phone',
    query_by: 'name,description',
    pinned_hits: '512,768,1024',
    hidden_hits: '256,384',
  };

  const searchResult = await client.collections('products').documents().search(searchParameters);
  console.log(searchResult);
}
```

## Performance Optimization

Optimize search performance with caching and query suggestions:

```typescript
async function cachingAndSuggestions() {
  // Enable result caching
  await client.collections('products').update({
    enable_nested_fields: true,
    cache_search_results_for_2_seconds: true,
  });

  // Generate query suggestions
  const suggestions = await client.collections('products').documents().search({
    q: 'iph',
    query_by: 'name',
    prefix: true,
    max_hits: 0,
    suggest_for_single_word_queries: 'always',
  });

  console.log(suggestions);
}
```

## Scaling and High Availability

Set up a Typesense cluster for high availability:

```typescript
const client = new Typesense.Client({
  nodes: [
    { host: 'node1.example.com', port: 8108, protocol: 'https' },
    { host: 'node2.example.com', port: 8108, protocol: 'https' },
    { host: 'node3.example.com', port: 8108, protocol: 'https' },
  ],
  apiKey: 'xyz',
  numRetries: 3,
  connectionTimeoutSeconds: 10,
});
```

## Security and Access Control

Implement API key-based access control:

```typescript
async function createSearchOnlyKey() {
  const searchOnlyKey = await client.keys().create({
    description: 'Search-only key',
    actions: ['documents:search'],
    collections: ['products'],
  });

  console.log('Search-only API Key:', searchOnlyKey.value);
}
```

## Monitoring and Analytics

Monitor Typesense performance:

```typescript
async function getStats() {
  const stats = await client.metrics.json;
  console.log('Typesense Stats:', stats);
}
```

## Integrations and Extensions

Integrate Typesense with popular frameworks:

```typescript
// Example: Integrating with Express.js
import express from 'express';
const app = express();

app.get('/search', async (req, res) => {
  const { q } = req.query;
  const searchResult = await client.collections('products').documents().search({
    q: q as string,
    query_by: 'name,description',
  });
  res.json(searchResult);
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

## Conclusion

This tutorial has covered the essential concepts of Typesense, from basic operations to advanced features and best practices. By following these examples and experimenting with your own data, you'll be well on your way to becoming a proficient Typesense developer.

Remember to consult the [official Typesense documentation](https://typesense.org/docs/) for the most up-to-date information and advanced topics not covered in this tutorial.

Happy searching!