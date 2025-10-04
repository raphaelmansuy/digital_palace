# 🚀 GraphRAG: Graph-based Retrieval-Augmented Generation

**GraphRAG** is a modular graph-based Retrieval-Augmented Generation (RAG) system developed by Microsoft Research. It extracts meaningful, structured data from unstructured text using LLMs and leverages knowledge graph memory structures to enhance LLM outputs for better reasoning about private, narrative data.

## 🎯 Core Concepts

### Graph-Based RAG Architecture

- **Knowledge Graph Construction**: Automatically builds structured knowledge representations from text documents
- **Entity-Relationship Extraction**: Identifies entities, relationships, and claims from unstructured data
- **Hierarchical Graph Structures**: Creates community hierarchies and entity networks for comprehensive understanding
- **Multi-Scale Retrieval**: Combines local (entity-level) and global (community-level) information retrieval

### Key Advantages

- **Enhanced Reasoning**: Graph structures enable complex multi-hop reasoning and relationship traversal
- **Scalable Knowledge Discovery**: Handles large datasets with efficient graph-based indexing
- **Contextual Understanding**: Maintains semantic relationships for more accurate and coherent responses
- **Private Data Focus**: Optimized for enterprise and private data scenarios

## 🛠️ Key Features

### Data Pipeline Components

- **Indexing Pipeline**: Processes documents into knowledge graphs with entities, relationships, and claims
- **Query Processing**: Supports local, global, and hybrid query modes
- **Community Detection**: Automatically identifies and summarizes knowledge communities
- **Claim Extraction**: Extracts factual claims and relationships from text

### LLM Integration

- **OpenAI Compatible**: Works with GPT models and other OpenAI-compatible APIs
- **Custom LLM Support**: Extensible architecture for custom language models
- **Prompt Tuning**: Advanced prompt engineering for optimal performance
- **Responsible AI**: Built-in safety and transparency features

### Storage and Deployment

- **Flexible Storage**: Supports various storage backends for graphs and vectors
- **Cloud-Native**: Designed for scalable cloud deployment
- **Command-Line Interface**: Comprehensive CLI for indexing and querying
- **API Endpoints**: RESTful APIs for integration with applications

### Advanced Capabilities

- **Multi-Hop Reasoning**: Traverse complex relationship chains
- **Temporal Analysis**: Handle time-based relationships and events
- **Claim Verification**: Cross-reference and validate extracted information
- **Visualization**: Graph visualization and exploration tools

## 📦 Installation & Setup

### Prerequisites

- Python 3.10+
- OpenAI API key (for LLM operations)
- Sufficient compute resources (indexing can be expensive)

### Install GraphRAG

```bash
# Install from PyPI
pip install graphrag

# Or install from source
git clone https://github.com/microsoft/graphrag.git
cd graphrag
pip install -e .
```

### Initialize Project

```bash
# Create new GraphRAG project
graphrag init --root ./my-project

# This creates the necessary configuration files and directories
```

### Configuration

Edit the `settings.yaml` file to configure:

- LLM endpoints and API keys
- Storage backends
- Indexing parameters
- Query settings

## 🚀 Quick Start

### Basic Workflow

```python
import pandas as pd
from graphrag.api import QueryApi
from graphrag.config import load_config

# Load configuration
config = load_config("./settings.yaml")

# Initialize API
api = QueryApi(config)

# Index documents (run once)
documents = pd.DataFrame([
    {"id": "doc1", "text": "Your document text here..."},
    {"id": "doc2", "text": "More document content..."}
])

# Build knowledge graph
await api.build_index_async(documents)

# Query the system
response = await api.query_async(
    "What are the key relationships in the data?",
    query_type="global"
)
print(response)
```

### Command Line Usage

```bash
# Index documents
graphrag index --root ./my-project

# Run a global query
graphrag query --root ./my-project --query "Summarize the main themes"

# Run a local query
graphrag query --root ./my-project --query "What does document X say about Y?" --method local
```

### Query Types

- `global`: Synthesize answers across the entire dataset using community summaries
- `local`: Answer questions using specific entity information and relationships
- `hybrid`: Combine global and local approaches for comprehensive answers

## 🏗️ Advanced Configuration

### Storage Backends

- **Azure Storage**: For cloud-native deployments
- **Local Files**: JSON and parquet files for development
- **Custom Storage**: Extensible storage interfaces

### LLM Configuration

```yaml
llm:
  type: openai
  model: gpt-4
  api_key: ${GRAPHRAG_API_KEY}
  max_tokens: 4000
  temperature: 0.0
```

### Indexing Parameters

```yaml
indexing:
  chunk_size: 1200
  chunk_overlap: 100
  n_subset_max: 1000
  k: 10
```

## 📊 Performance & Evaluation

GraphRAG demonstrates significant improvements in reasoning capabilities compared to traditional RAG approaches:

- **Multi-hop Reasoning**: Better performance on complex relationship queries
- **Scalability**: Handles datasets from thousands to millions of documents
- **Accuracy**: Reduced hallucinations through structured knowledge grounding
- **Efficiency**: Optimized indexing and query pipelines

Based on Microsoft Research evaluations and community benchmarks.

## 🔗 Integration Examples

### With Azure OpenAI

```python
from graphrag.config import GraphRagConfig
from graphrag.api import QueryApi

config = GraphRagConfig(
    llm={
        "type": "azure_openai",
        "model": "gpt-4",
        "azure_endpoint": "https://your-endpoint.openai.azure.com/",
        "azure_deployment": "gpt-4",
        "api_key": "${AZURE_OPENAI_API_KEY}",
    },
    storage={
        "type": "azure_blob",
        "container_name": "graphrag-data",
        "connection_string": "${AZURE_STORAGE_CONNECTION_STRING}",
    }
)

api = QueryApi(config)
```

### Custom Data Sources

```python
import pandas as pd
from graphrag.indexing import build_index

# Load data from various sources
documents = []

# From CSV
df = pd.read_csv("data.csv")
for _, row in df.iterrows():
    documents.append({
        "id": row["id"],
        "text": row["content"],
        "title": row["title"]
    })

# From JSON
import json
with open("data.json", "r") as f:
    data = json.load(f)
    for item in data:
        documents.append(item)

# Build index
build_index(documents, config)
```

## 🌟 Use Cases

- **Enterprise Knowledge Management**: Structured analysis of large document corpora
- **Research Intelligence**: Extract insights from academic papers and research data
- **Business Intelligence**: Analyze market reports, financial data, and industry trends
- **Legal Document Analysis**: Process contracts, case law, and regulatory documents
- **Healthcare Data Mining**: Extract relationships from medical records and research

## 📚 Related Projects

- **[LightRAG](./lightrag.md)**: Simple and fast knowledge graph RAG
- **[RAG-Anything](./rag-anything.md)**: Multimodal document processing
- **[Knowledge Graphs](./knowledge-graphs.md)**: Graph-based knowledge representation

## 🔗 Learn More

- **[GitHub Repository](https://github.com/microsoft/graphrag)**: Source code and documentation
- **[Official Documentation](https://microsoft.github.io/graphrag/)**: Complete guides and API reference
- **[Microsoft Research Blog](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/)**: Technical overview and research insights
- **[ArXiv Paper](https://arxiv.org/pdf/2404.16130)**: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
- **[Responsible AI FAQ](https://github.com/microsoft/graphrag/blob/main/RAI_TRANSPARENCY.md)**: Transparency and safety information

## 🧠 Related Concepts

- **[RAG](./rag.md)**: Retrieval-Augmented Generation fundamentals
- **[Knowledge Graphs](./knowledge-graphs.md)**: Graph-based knowledge representation
- **[Knowledge Management](./knowledge-management.md)**: Organizing and leveraging information
- **[Embeddings](./embeddings.md)**: Vector representations for similarity search
- **[LLMs](./llms.md)**: Large Language Models integration

---

### 🔗 Navigation

- [← Back to Concepts Hub](./README.md)
- [RAG →](./rag.md)
- [LightRAG →](./lightrag.md)
- [Knowledge Graphs →](./knowledge-graphs.md)
