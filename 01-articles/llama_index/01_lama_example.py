"""
This module provides an example of using the llama_index library to load and query documents.
"""
from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Load in data as Document objects, either manually or through a data loader
documents = SimpleDirectoryReader('data').load_data()

# Parse Document objects into Node objects to represent chunks of data
index = VectorStoreIndex.from_documents(documents)


# Build an index over the Documents or Nodes
query_engine = index.as_query_engine()

# The response is a Response object containing the text response and source Nodes
summary = query_engine.query("What is the text about")
print("What is the data about:")
print(summary)

person = query_engine.query(
    "Extract all the person in the content, format as JSON with a lastname"
    " and first_name property")
print(person)


location = query_engine.query(
    "Extract all the location in the content, format as JSON with a name"
    " and the country")
print(location)