# 🚀 LightRAG: Simple and Fast Retrieval-Augmented Generation

**LightRAG** is an open-source Retrieval-Augmented Generation (RAG) framework that leverages knowledge graphs to enhance information retrieval and generation. Developed by researchers at HKUDS, it provides a simple yet powerful approach to building RAG systems with graph-based indexing and dual-level retrieval mechanisms.

## 🎯 Core Concepts

### Graph-Based RAG Architecture

- **Knowledge Graph Construction**: Automatically extracts entities and relationships from documents to build structured knowledge representations
- **Dual-Level Retrieval**: Combines low-level (chunk-based) and high-level (entity-relationship) retrieval for comprehensive context gathering
- **Vector + Graph Integration**: Uses both vector embeddings and graph structures for efficient similarity search and relationship traversal
- **Incremental Updates**: Supports real-time knowledge graph updates without full re-indexing

### Key Advantages

- **Improved Accuracy**: Graph structures capture complex inter-dependencies that flat representations miss
- **Faster Retrieval**: Optimized graph traversal algorithms provide quick access to related information
- **Contextual Awareness**: Maintains relationships between entities for more coherent responses
- **Scalability**: Efficient storage and retrieval mechanisms for large knowledge bases

## 🛠️ Key Features

### Multi-Modal Support

- Text document processing
- Integration with [RAG-Anything](./rag-anything.md) for images, tables, and formulas
- PDF, DOC, PPT, CSV file support via textract

### LLM Integration

- OpenAI API compatible models
- Hugging Face transformers
- Ollama local models
- Custom LLM providers

### Storage Backends

- **Vector Storage**: NanoVector (default), Faiss, Milvus, Qdrant, PostgreSQL, MongoDB
- **Graph Storage**: NetworkX (default), Neo4J, PostgreSQL AGE, Memgraph
- **KV Storage**: JSON files, Redis, PostgreSQL, MongoDB
- **Document Status**: JSON files, PostgreSQL, MongoDB

### Advanced Capabilities

- Citation functionality for source attribution
- Graph visualization and exploration
- Entity and relationship editing
- Batch operations and data export
- Token usage tracking
- Multi-workspace support for data isolation

## 📦 Installation & Setup

### Install LightRAG Core

```bash
# From PyPI
pip install lightrag-hku

# From source (recommended)
git clone https://github.com/HKUDS/LightRAG.git
cd LightRAG
pip install -e .
```

### Install LightRAG Server (with Web UI)

```bash
pip install "lightrag-hku[api]"
# Configure environment
cp env.example .env
lightrag-server
```

### Docker Deployment

```bash
git clone https://github.com/HKUDS/LightRAG.git
cd LightRAG
cp env.example .env
docker compose up
```

## 🚀 Quick Start

### Basic Usage Example

```python
import asyncio
from lightrag import LightRAG
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed

async def main():
    # Initialize RAG with OpenAI
    rag = LightRAG(
        working_dir="./rag_storage",
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete
    )
    
    # Initialize storages (required)
    await rag.initialize_storages()
    await initialize_pipeline_status()
    
    # Insert documents
    await rag.ainsert("Your document text here...")
    
    # Query with different modes
    response = await rag.aquery(
        "What are the key concepts?",
        param=QueryParam(mode="hybrid")
    )
    print(response)
    
    # Cleanup
    await rag.finalize_storages()

asyncio.run(main())
```

### Query Modes

- `local`: Context-dependent information
- `global`: Global knowledge utilization  
- `hybrid`: Combined local and global retrieval
- `naive`: Basic search without advanced techniques
- `mix`: Knowledge graph + vector retrieval
- `bypass`: Direct LLM response

## 🏗️ Advanced Configuration

### LLM Requirements

- Minimum 32B parameters recommended
- 32K+ context length (64K preferred)
- Avoid reasoning models for indexing stage

### Embedding Models

- BAAI/bge-m3 (recommended)
- text-embedding-3-large
- Other high-performance multilingual models

### Reranker Integration

- BAAI/bge-reranker-v2-m3
- Jina AI rerankers
- Cohere rerankers

## 📊 Performance & Evaluation

Based on experimental results, LightRAG shows significant improvements over traditional RAG approaches:

| Metric | LightRAG | NaiveRAG | GraphRAG |
|--------|----------|----------|----------|
| Comprehensiveness | 67.6% | 32.4% | 54.4% |
| Diversity | 76.4% | 23.6% | 77.2% |
| Overall | 67.6% | 32.4% | 54.8% |

*Results from UltraDomain dataset evaluation*

## 🔗 Integration Examples

### With Neo4J Storage

```python
from lightrag.kg.neo4j_impl import Neo4JStorage

rag = LightRAG(
    working_dir="./neo4j_storage",
    graph_storage=Neo4JStorage(
        host="localhost",
        port=7687,
        user="neo4j",
        password="password"
    )
)
```

### With PostgreSQL

```python
from lightrag.kg.postgres_impl import PGGraphStorage

rag = LightRAG(
    graph_storage=PGGraphStorage(
        host="localhost",
        port=5432,
        database="rag_db",
        user="user",
        password="password"
    )
)
```

## 🌟 Use Cases

- **Enterprise Knowledge Management**: Structured document indexing and retrieval
- **Research Assistant**: Academic paper analysis with citation tracking
- **Customer Support**: Context-aware response generation from knowledge bases
- **Content Creation**: Enhanced writing with factual verification
- **Educational Tools**: Interactive learning with comprehensive explanations

## 📚 Related Projects

- **[RAG-Anything](./rag-anything.md)**: Multimodal document processing
- **[VideoRAG](./videorag.md)**: Long-context video understanding
- **[MiniRAG](./minirag.md)**: Lightweight RAG for small language models

## 🔗 Learn More

- **[GitHub Repository](https://github.com/HKUDS/LightRAG)**: Source code and documentation
- **[Paper](https://arxiv.org/abs/2410.05779)**: "LightRAG: Simple and Fast Retrieval-Augmented Generation"
- **[LightRAG Server Docs](https://github.com/HKUDS/LightRAG/blob/main/lightrag/api/README.md)**: API and Web UI guide
- **[Discord Community](https://discord.gg/yF2MmDJyGJ)**: Discussion and support

## 🧠 Related Concepts

- **[RAG](./rag.md)**: Retrieval-Augmented Generation fundamentals
- **[RAG-Anything](./rag-anything.md)**: Multimodal extension of LightRAG
- **[Knowledge Graphs](./knowledge-graphs.md)**: Graph-based knowledge representation
- **[Embeddings](./embeddings.md)**: Vector representations for similarity search
- **[LLMs](./llms.md)**: Large Language Models integration

---

**🔗 Navigation**
- [← Back to Concepts Hub](./README.md)
- [RAG →](./rag.md)
- [RAG-Anything →](./rag-anything.md)
- [VideoRAG →](./videorag.md)
- [MiniRAG →](./minirag.md)
- [GraphRAG →](./graphrag.md)
</content>
<parameter name="filePath">/Users/raphaelmansuy/Github/00-obsidian/digital_palace/concepts/lightrag.md