# 🚀 RAG-Anything: All-in-One Multimodal RAG Framework

**RAG-Anything** is a comprehensive multimodal Retrieval-Augmented Generation (RAG) framework that extends LightRAG to handle diverse document types including text, images, tables, and mathematical equations. Developed by HKUDS, it provides unified processing and querying capabilities across all content modalities within a single integrated system.

## 🎯 Core Concepts

### **Multimodal RAG Architecture**

- **Unified Framework**: Single system for processing and querying multimodal documents
- **End-to-End Pipeline**: Complete workflow from document ingestion to intelligent multimodal query answering
- **Knowledge Graph Integration**: Builds structured semantic representations across modalities
- **Cross-Modal Relationships**: Establishes connections between textual and visual content

### **Key Advantages**

- **Universal Document Support**: Handles PDFs, Office documents, images, and text files
- **Specialized Content Analysis**: Dedicated processors for images, tables, equations, and heterogeneous content
- **Adaptive Processing**: Flexible parsing modes (MinerU-based or direct content injection)
- **Contextual Understanding**: Preserves document hierarchy and inter-element relationships

## 🛠️ Key Features

### **Document Processing**

- **MinerU Integration**: High-fidelity document structure extraction with OCR capabilities
- **Docling Support**: Optimized parsing for Office documents and HTML files
- **Universal Format Support**: PDFs, DOC/DOCX, PPT/PPTX, XLS/XLSX, images, text files
- **Concurrent Pipelines**: Parallel processing of textual and multimodal content

### **Multimodal Analysis**

- **Visual Content Analyzer**: Image analysis with context-aware caption generation
- **Structured Data Interpreter**: Table interpretation with statistical pattern recognition
- **Mathematical Expression Parser**: LaTeX formula parsing with semantic mapping
- **Extensible Modality Handler**: Plugin architecture for custom content types

### **Query Capabilities**

- **Pure Text Queries**: Traditional knowledge base search
- **VLM Enhanced Queries**: Vision-Language Model integration for image analysis
- **Multimodal Queries**: Enhanced queries with specific multimodal content
- **Modality-Aware Retrieval**: Intelligent ranking based on content type relevance

### **Advanced Features**

- **Direct Content Injection**: Bypass parsing by inserting pre-processed content lists
- **Batch Processing**: Handle multiple documents with configurable workers
- **Context Configuration**: Intelligent integration of relevant contextual information
- **Citation Support**: Source attribution for retrieved content

## 📦 Installation & Setup

### **Install from PyPI**

```bash
# Basic installation
pip install raganything

# With all optional features
pip install 'raganything[all]'

# Specific features
pip install 'raganything[image]'    # Extended image formats
pip install 'raganything[text]'     # Text file processing
```

### **Install from Source**

```bash
git clone https://github.com/HKUDS/RAG-Anything.git
cd RAG-Anything
pip install -e .
```

### **Requirements**

- **LibreOffice**: Required for Office document processing
- **MinerU**: Automatic installation or manual setup for document parsing
- **Optional Dependencies**: Pillow for images, ReportLab for text processing

## 🚀 Quick Start

### **Basic Usage Example**

```python
import asyncio
from raganything import RAGAnything, RAGAnythingConfig
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from lightrag.utils import EmbeddingFunc

async def main():
    # Configure RAG-Anything
    config = RAGAnythingConfig(
        working_dir="./rag_storage",
        parser="mineru",
        enable_image_processing=True,
        enable_table_processing=True,
        enable_equation_processing=True,
    )

    # Initialize with OpenAI
    rag = RAGAnything(
        config=config,
        llm_model_func=lambda prompt, **kwargs: openai_complete_if_cache(
            "gpt-4o-mini", prompt, api_key="your-api-key", **kwargs
        ),
        embedding_func=EmbeddingFunc(
            embedding_dim=3072,
            func=lambda texts: openai_embed(texts, model="text-embedding-3-large")
        ),
    )

    # Process a document
    await rag.process_document_complete(
        file_path="document.pdf",
        output_dir="./output"
    )

    # Query with different modes
    text_result = await rag.aquery("Summarize the key findings", mode="hybrid")
    multimodal_result = await rag.aquery_with_multimodal(
        "Analyze the charts and tables",
        multimodal_content=[{"type": "table", "table_data": "..."}]
    )

    print(text_result)
    print(multimodal_result)

asyncio.run(main())
```

### **Direct Content Processing**

```python
# Process multimodal content directly
from raganything.modalprocessors import ImageModalProcessor

image_processor = ImageModalProcessor(lightrag=rag)
description, entity_info = await image_processor.process_multimodal_content(
    modal_content={
        "img_path": "path/to/image.jpg",
        "image_caption": ["Figure 1"],
        "image_footnote": ["Source data"]
    },
    content_type="image",
    file_path="document.pdf",
    entity_name="Analysis Figure"
)
```

## � Context-Aware Processing

RAG-Anything features an advanced context-aware processing module that automatically extracts and provides surrounding text content when analyzing multimodal elements. This enhances accuracy by giving AI models additional contextual information about document structure and content relationships.

### **Key Benefits**

- **Enhanced Accuracy**: Context helps AI understand the purpose and meaning of multimodal content
- **Semantic Coherence**: Generated descriptions align with document terminology and structure
- **Automated Integration**: Context extraction is automatically enabled during document processing
- **Flexible Configuration**: Multiple extraction modes and filtering options

### **Configuration Options**

```python
config = RAGAnythingConfig(
    context_window=2,                    # Context window size (pages/chunks)
    context_mode="page",                 # "page" or "chunk" based extraction
    max_context_tokens=3000,             # Maximum context tokens
    include_headers=True,                # Include document headers
    include_captions=True,               # Include image/table captions
    context_filter_content_types=["text", "image"],  # Content types to include
    content_format="minerU"              # Content format for extraction
)
```

### **Context Modes**

- **Page-Based Context**: Extracts context based on page boundaries using `page_idx` field
- **Chunk-Based Context**: Extracts context based on sequential position in content list

### **Context-Aware Features**

- **Smart Token Management**: Uses actual tokenizer for precise token counting and truncation
- **Boundary Preservation**: Truncates at sentence/paragraph boundaries to maintain semantic integrity
- **Content Filtering**: Configurable filtering of content types to reduce noise
- **Runtime Updates**: Dynamic configuration updates without restarting

### **Usage Example**

```python
# Context is automatically enabled during document processing
await rag.process_document_complete("document.pdf")

# Manual context configuration for custom content
rag.set_content_source_for_context(content_list, "minerU")

# Update context settings at runtime
rag.update_context_config(
    context_window=1,
    max_context_tokens=1500,
    include_captions=False
)
```

## �🏗️ Architecture Overview

### **Document Parsing Stage**

1. **Adaptive Content Decomposition**: Segments documents into coherent elements
2. **Concurrent Processing**: Parallel pipelines for text and multimodal content
3. **Hierarchy Preservation**: Maintains original document structure and relationships

### **Multimodal Analysis Engine**

- **Content Categorization**: Automatic identification and routing of content types
- **Specialized Analyzers**: Dedicated processing for images, tables, and equations
- **Knowledge Graph Construction**: Structured semantic representations across modalities

### **Modality-Aware Retrieval**

- **Vector-Graph Fusion**: Combines vector similarity with graph traversal
- **Modality-Aware Ranking**: Content-type specific relevance scoring
- **Relational Coherence**: Maintains semantic connections between retrieved elements

## 🌟 Use Cases

- **Academic Research**: Process research papers with figures, tables, and equations
- **Technical Documentation**: Handle manuals with diagrams and specifications
- **Financial Reports**: Analyze documents with charts, tables, and complex data
- **Enterprise Knowledge Management**: Unified processing of mixed-content documents
- **Educational Materials**: Interactive learning with multimodal content

## 🔗 Integration with LightRAG

RAG-Anything is built on top of LightRAG and extends its capabilities:

- **Seamless Integration**: Works with existing LightRAG instances
- **Enhanced Querying**: Adds multimodal query capabilities to LightRAG
- **Shared Storage**: Uses LightRAG's storage backends and knowledge graphs
- **Backward Compatibility**: Can load and extend existing LightRAG knowledge bases

## 📚 Related Projects

- **[LightRAG](./lightrag.md)**: Core RAG framework that RAG-Anything extends
- **[VideoRAG](./videorag.md)**: Long-context video understanding
- **[MinerU](https://github.com/opendatalab/MinerU)**: Document parsing engine
- **[Docling](https://github.com/DS4SD/docling)**: Alternative document parser

## 🔗 Learn More

- **[GitHub Repository](https://github.com/HKUDS/RAG-Anything)**: Source code and documentation
- **[Context-Aware Processing](https://github.com/HKUDS/RAG-Anything/blob/main/docs/context_aware_processing.md)**: Detailed context extraction documentation
- **[LightRAG Paper](https://arxiv.org/abs/2410.05779)**: Research foundation
- **[MinerU Documentation](https://github.com/opendatalab/MinerU)**: Document parsing details
- **[Discord Community](https://discord.gg/yF2MmDJyGJ)**: Discussion and support

## 🧠 Related Concepts

- **[RAG](./rag.md)**: Retrieval-Augmented Generation fundamentals
- **[LightRAG](./lightrag.md)**: Core framework that RAG-Anything extends
- **[Multimodal AI](./multimodal-ai.md)**: Broader multimodal AI concepts
- **[Knowledge Graphs](./knowledge-graphs.md)**: Graph-based knowledge representation
- **[Embeddings](./embeddings.md)**: Vector representations for similarity search

---

**🔗 Navigation**
- [← Back to Concepts Hub](./README.md)
- [RAG →](./rag.md)
- [LightRAG →](./lightrag.md)
- [VideoRAG →](./videorag.md)
- [Multimodal AI →](./multimodal-ai.md)</content>
<parameter name="filePath">/Users/raphaelmansuy/Github/00-obsidian/digital_palace/concepts/rag-anything.md