# 🚀 MiniRAG: Towards Extremely Simple Retrieval-Augmented Generation

**MiniRAG** is a lightweight Retrieval-Augmented Generation (RAG) framework specifically designed for small language models (SLMs). Developed by researchers at HKUDS, it enables efficient RAG performance through heterogeneous graph indexing and topology-enhanced retrieval, requiring only 25% of the storage space compared to traditional methods.

## 🎯 Core Concepts

### Heterogeneous Graph Indexing

- **Unified Structure**: Combines text chunks and named entities in a single graph representation
- **Semantic-Aware Design**: Reduces reliance on complex semantic understanding from SLMs
- **Efficient Storage**: Optimized data structures for resource-constrained environments
- **Entity-Relationship Integration**: Captures both textual content and semantic relationships

### Topology-Enhanced Retrieval

- **Graph-Based Discovery**: Leverages graph structures for efficient knowledge retrieval
- **Lightweight Processing**: Minimal computational requirements for on-device deployment
- **Context Preservation**: Maintains relationship context during retrieval operations
- **Multi-Hop Reasoning**: Supports complex query patterns through graph traversal

### Key Advantages

- **SLM Optimization**: Specifically designed for small language models with limited capabilities
- **Resource Efficiency**: 25% storage reduction compared to LLM-based approaches
- **On-Device Ready**: Optimized for deployment in resource-constrained scenarios
- **Performance Parity**: Achieves comparable results to complex RAG systems

## 🛠️ Key Features

### Graph Database Support

- **Neo4j**: Enterprise-grade graph database integration
- **PostgreSQL**: Relational database with graph extensions
- **TiDB**: Distributed SQL database with graph capabilities
- **NetworkX**: Lightweight in-memory graph processing
- **10+ Database Options**: Comprehensive support for various graph storage backends

### Model Compatibility

- **Small Language Models**: Optimized for Phi-3.5-mini, GLM-Edge-1.5B, Qwen2.5-3B, MiniCPM3-4B
- **API Deployment**: RESTful API endpoints for easy integration
- **Docker Support**: Containerized deployment with docker-compose
- **Local Execution**: No external API dependencies required

### Benchmark Dataset

- **LiHua-World**: Comprehensive dataset with one year of chat records
- **Query Types**: Single-hop, multi-hop, and summary questions
- **Realistic Scenarios**: Designed for on-device RAG evaluation
- **Manual Annotations**: Ground truth answers with supporting documents

### Advanced Capabilities

- **Citation Support**: Source attribution for retrieved information
- **Graph Visualization**: Interactive exploration of knowledge structures
- **Batch Processing**: Efficient handling of multiple queries
- **Incremental Updates**: Real-time knowledge graph modifications

## 📊 Performance Metrics

### LiHua-World Benchmark Results

| Model | Single-Hop Acc | Single-Hop Err | Multi-Hop Acc | Multi-Hop Err | Summary Acc | Summary Err |
|-------|----------------|----------------|---------------|----------------|--------------|----------------|
| **Phi-3.5-mini-instruct** | 41.22% | 23.20% | / | / | 39.81% | 25.39% |
| **GLM-Edge-1.5B-Chat** | 42.79% | 24.76% | / | / | 35.74% | 25.86% |
| **Qwen2.5-3B-Instruct** | 43.73% | 24.14% | / | / | 39.18% | 28.68% |
| **MiniCPM3-4B** | 43.42% | 17.08% | / | / | 35.42% | 21.94% |
| **gpt-4o-mini** | 46.55% | 19.12% | 35.27% | 37.77% | 56.90% | 20.85% |

**Note**: "/" indicates methods that struggle to generate effective responses

### MultiHop-RAG Benchmark Results

| Model | Single-Hop Acc | Single-Hop Err | Multi-Hop Acc | Multi-Hop Err | Summary Acc | Summary Err |
|-------|----------------|----------------|---------------|----------------|--------------|----------------|
| **Phi-3.5-mini-instruct** | 42.72% | 31.34% | / | / | 27.03% | 11.78% |
| **GLM-Edge-1.5B-Chat** | 44.44% | 24.26% | / | / | / | / |
| **Qwen2.5-3B-Instruct** | 39.48% | 31.69% | / | / | 21.91% | 13.73% |
| **MiniCPM3-4B** | 39.24% | 31.42% | / | / | 19.48% | 10.41% |
| **gpt-4o-mini** | 53.60% | 27.19% | 60.92% | 16.86% | 64.91% | 19.37% |

## 🚀 Installation

### From Source (Recommended)

```bash
cd MiniRAG
pip install -e .
```

### From PyPI

```bash
pip install lightrag-hku
```

### Docker Deployment

```bash
docker-compose up -d
```

## 💡 Usage Examples

### Basic Initialization

```python
from minirag import MiniRAG

# Initialize with default settings
rag = MiniRAG()

# Insert documents
rag.insert("Your knowledge base content here...")

# Query with retrieval-augmented generation
response = rag.query("What is the capital of France?")
```

### Custom Configuration

```python
from minirag import MiniRAG

# Configure for specific use case
rag = MiniRAG(
    llm_model="phi-3.5-mini-instruct",
    graph_db="neo4j",
    embedding_model="sentence-transformers"
)

# Index documents
documents = ["Document 1 content...", "Document 2 content..."]
rag.insert(documents)
```

### API Deployment

```python
from minirag.api import MiniRAGAPI

# Start API server
api = MiniRAGAPI(rag_instance)
api.run(host="0.0.0.0", port=8000)
```

## 🏗️ Architecture Components

### Indexing Pipeline

1. **Document Processing**: Text chunking and entity extraction
2. **Graph Construction**: Building heterogeneous knowledge graph
3. **Embedding Generation**: Vector representations for similarity search
4. **Storage Optimization**: Efficient persistence of graph structures

### Retrieval Pipeline

1. **Query Analysis**: Understanding user intent and requirements
2. **Graph Traversal**: Topology-enhanced knowledge discovery
3. **Context Assembly**: Combining relevant information chunks
4. **Response Generation**: SLM-powered answer synthesis

## 📈 Use Cases

- **Edge Computing**: On-device RAG applications with limited resources
- **Mobile Applications**: Lightweight knowledge assistants for smartphones
- **IoT Devices**: Embedded systems with conversational capabilities
- **Offline Scenarios**: Local deployment without internet connectivity
- **Resource-Constrained Environments**: Small-scale deployments and prototypes

## 📚 Related Projects

- **[LightRAG](./lightrag.md)**: Full-featured RAG with advanced graph capabilities
- **[RAG-Anything](./rag-anything.md)**: Multimodal document processing
- **[VideoRAG](./videorag.md)**: Long-context video understanding

## 🔗 Learn More

- **[GitHub Repository](https://github.com/HKUDS/MiniRAG)**: Source code and documentation
- **[Paper](https://arxiv.org/abs/2501.06713)**: "MiniRAG: Towards Extremely Simple Retrieval-Augmented Generation"
- **[API Documentation](https://github.com/HKUDS/MiniRAG/blob/main/minirag/api/README.md)**: RESTful API and deployment guide
- **[LiHua-World Dataset](https://github.com/HKUDS/MiniRAG/blob/main/dataset/LiHua-World/README.md)**: Benchmark dataset documentation

## 🧠 Related Concepts

- **[RAG](./rag.md)**: Retrieval-Augmented Generation fundamentals
- **[LightRAG](./lightrag.md)**: Advanced graph-based RAG framework
- **[Knowledge Graphs](./knowledge-graphs.md)**: Graph-based knowledge representation
- **[Embeddings](./embeddings.md)**: Vector representations for similarity search
- **[LLMs](./llms.md)**: Large Language Models integration

---

## 🔗 Navigation

- [← Back to Concepts Hub](./README.md)
- [RAG →](./rag.md)
- [LightRAG →](./lightrag.md)
- [RAG-Anything →](./rag-anything.md)
- [VideoRAG →](./videorag.md)
