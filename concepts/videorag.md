# 🎥 VideoRAG: Retrieval-Augmented Generation with Extreme Long-Context Videos

**VideoRAG** is a cutting-edge framework for understanding and analyzing extremely long-context videos using retrieval-augmented generation techniques. Developed by HKUDS, it introduces a dual-channel architecture that combines graph-driven knowledge indexing with hierarchical context encoding to process videos ranging from short clips to hundreds of hours in length.

## 🎯 Core Concepts

### **VideoRAG Architecture**

- **Dual-Channel Processing**: Combines graph-driven knowledge indexing with hierarchical context encoding
- **Multi-Modal Integration**: Aligns textual queries with visual and audio content
- **Extreme Long-Context**: Handles videos up to hundreds of hours efficiently
- **Structured Indexing**: Distills long videos into concise knowledge representations

### **Key Advantages**

- **No Length Limits**: Process everything from 30-second clips to 100+ hour documentaries
- **Deep Understanding**: Combines visual content, audio, and context for comprehensive answers
- **Efficient Processing**: Single GPU capability (RTX 3090) for hundreds of hours
- **Scalable Architecture**: Handles multiple videos simultaneously with cross-video understanding

## 🛠️ Key Features

### **Vimo Desktop Application**

- **Drag & Drop Upload**: Simply drag video files into the interface
- **Smart Conversations**: Ask questions in natural language
- **Multi-Format Support**: Works with MP4, MKV, AVI, and more
- **Cross-Platform**: Available on macOS, Windows, and Linux

### **Advanced Capabilities**

- **Multi-Video Analysis**: Compare and analyze multiple videos simultaneously
- **Precise Retrieval**: Find specific moments and scenes with high accuracy
- **Export Features**: Save insights and references for later use
- **Benchmark Performance**: Evaluated on 134+ hours across diverse content types

### **Technical Features**

- **Graph-Driven Indexing**: Multi-modal knowledge graphs for structured understanding
- **Hierarchical Encoding**: Preserves spatiotemporal visual patterns
- **Adaptive Retrieval**: Dynamic mechanisms optimized for video content
- **Cross-Video Relationships**: Semantic modeling across multiple videos

## 📦 Installation & Setup

### **Vimo Desktop App**

```bash
# Clone the repository
git clone https://github.com/HKUDS/VideoRAG.git
cd VideoRAG

# Follow setup instructions in Vimo-desktop directory
cd Vimo-desktop
# See README for detailed installation steps
```

### **VideoRAG Algorithm (Development)**

```bash
# Set up conda environment
cd VideoRAG-algorithm
conda env create -f environment.yml
conda activate videorag

# Download model checkpoints and install dependencies
# Follow the detailed setup in VideoRAG-algorithm/README.md
```

## 🚀 Quick Start

### **Using Vimo Desktop**

1. **Download/Setup**: Get Vimo from releases or build from source
2. **Launch Application**: Start the desktop app
3. **Upload Videos**: Drag and drop video files
4. **Start Chatting**: Ask questions in natural language

### **Basic Usage Example**

```python
# VideoRAG algorithm usage (from development setup)
from videorag import VideoRAG

# Initialize with video file
rag = VideoRAG(
    video_path="path/to/video.mp4",
    model_config="path/to/config.json"
)

# Process video and build knowledge graph
rag.process_video()

# Query the processed video
response = rag.query("What are the main topics discussed in this lecture?")
print(response)
```

## 🏗️ Architecture Overview

### **Dual-Channel Processing**

1. **Graph-Driven Knowledge Indexing**: 
   - Multi-modal knowledge graphs
   - Structured video understanding
   - Entity and relationship extraction

2. **Hierarchical Context Encoding**:
   - Preserves spatiotemporal patterns
   - Long-sequence context handling
   - Temporal relationship modeling

### **Retrieval Mechanisms**

- **Multi-Modal Alignment**: Textual queries matched with visual/audio content
- **Temporal Localization**: Precise moment identification in long videos
- **Cross-Video Analysis**: Semantic relationships across multiple videos
- **Adaptive Ranking**: Content-type specific relevance scoring

## 📊 Performance & Benchmarks

### **LongerVideos Benchmark**

VideoRAG is evaluated on the LongerVideos benchmark featuring:

| Category | Videos | Hours | Questions | Duration |
|----------|--------|-------|-----------|----------|
| Lectures | 12 | 135 | 376 | ~64.3 hours |
| Documentaries | 5 | 12 | 114 | ~28.5 hours |
| Entertainment | 5 | 17 | 112 | ~41.9 hours |
| **Total** | **22** | **164** | **602** | **~134.6 hours** |

### **Performance Comparison**

VideoRAG significantly outperforms existing methods in long-context video understanding, with superior accuracy and efficiency on the benchmark dataset.

## 🌟 Use Cases

- **Educational Content**: Analyze lengthy lecture series and courses
- **Documentary Analysis**: Process long-form documentary films
- **Research Videos**: Extract insights from scientific presentations
- **Entertainment Analysis**: Understand complex movie plots and character arcs
- **Training Materials**: Process corporate training videos and tutorials

## 🔗 Integration with Other Frameworks

VideoRAG builds upon and integrates with:

- **LightRAG**: Graph-based retrieval foundations
- **ImageBind**: Multi-modal representation learning
- **Nano-GraphRAG**: Lightweight graph processing

## 📚 Related Projects

- **[LightRAG](./lightrag.md)**: Core RAG framework foundation
- **[RAG-Anything](./rag-anything.md)**: Multimodal document processing
- **[MiniRAG](./minirag.md)**: Lightweight RAG for small language models

## 🔗 Learn More

- **[GitHub Repository](https://github.com/HKUDS/VideoRAG)**: Source code and documentation
- **[Paper](https://arxiv.org/abs/2502.01549)**: "VideoRAG: Retrieval-Augmented Generation with Extreme Long-Context Videos"
- **[Vimo Desktop](https://github.com/HKUDS/VideoRAG/blob/main/Vimo-desktop)**: Desktop application setup
- **[VideoRAG Algorithm](https://github.com/HKUDS/VideoRAG/blob/main/VideoRAG-algorithm)**: Core algorithm implementation
- **[Demo Video](https://www.youtube.com/watch?v=D5vsxcp4QZI)**: Vimo introduction video

## 🧠 Related Concepts

- **[RAG](./rag.md)**: Retrieval-Augmented Generation fundamentals
- **[Multimodal AI](./multimodal-ai.md)**: Multi-modal AI concepts
- **[LightRAG](./lightrag.md)**: Graph-based RAG framework
- **[RAG-Anything](./rag-anything.md)**: Multimodal document processing

---

**🔗 Navigation**
- [← Back to Concepts Hub](./README.md)
- [RAG →](./rag.md)
- [LightRAG →](./lightrag.md)
- [RAG-Anything →](./rag-anything.md)
- [MiniRAG →](./minirag.md)</content>
<parameter name="filePath">/Users/raphaelmansuy/Github/00-obsidian/digital_palace/concepts/videorag.md