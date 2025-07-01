# 🧠 Core AI Technologies Reference

> Comprehensive technical guide to AI frameworks, models, and implementation details

## 📚 **Quick Reference Navigation**

| Technology Category | Focus Area | Best For |
|---------------------|------------|----------|
| [Large Language Models](#-large-language-models-llms) | Model architecture & implementation | Understanding AI foundations |
| [Model Serving](#-model-serving--inference) | Deployment & scaling | Production teams |
| [Model Training](#-model-training--fine-tuning) | Customization & optimization | ML Engineers |
| [Embeddings & Vectors](#-embeddings--vector-operations) | Semantic understanding | Data scientists |
| [Prompt Engineering](#-prompt-engineering) | Input optimization | All AI developers |
| [RAG Systems](#-rag--knowledge-systems) | Knowledge integration | Enterprise applications |
| [Voice & Speech](#-voice--speech-technologies) | Audio processing | Multimodal applications |

---

## 🤖 **Large Language Models (LLMs)**

### **LLM Implementation**

**Building LLMs from Scratch**
- **[LLMs from scratch](https://github.com/rasbt/LLMs-from-scratch)** - Implementing a ChatGPT-like LLM step by step by Sebastian Raschka

**Core Concepts & Architecture**
- [Generative AI Business Use Cases](../01-articles/2024-03-12_genai_business_use_cases.md)
- [Comprehensive Guide to Large Language Model Engineering](../11-genai/README.md)
- [Design and Architecture Patterns for LLM Applications](../01-articles/dessign_patterns_for_llm_applications/README.md)
- [Frameworks for Building LLM Applications](../01-articles/framework_for_llm_applications/README.md)
- [Mastering the Art of Training Large Language Models from Scratch](../01-articles/2024-03-12_training_an_llm.md)

---

## 🚀 **Model Serving & Inference**

### **High-Performance Servers**

**Industry Standards**
- **[vLLM](https://github.com/vllm-project/vllm)** - Easy, fast, and cheap LLM serving for everyone
  - **Documentation**: [vLLM Docs](https://docs.vllm.ai/en/latest/)
  - **Use Case**: Production deployments requiring high throughput
  - **Performance**: Industry standard for speed and efficiency

- **[llamaC++](https://github.com/ggerganov/llama.cpp)** - LLM inference in C/C++
  - **Strength**: Low-level optimization, cross-platform compatibility
  - **Best For**: Edge deployment, resource-constrained environments

- **[Ollama](https://github.com/ollama/ollama)** - Go program that encapsulates llama.cpp
  - **Documentation**: [Ollama Docs](https://ollama.com/)
  - **Strength**: Zero-config setup, beginner-friendly
  - **Best For**: Local development, rapid prototyping

### **Specialized Solutions**

**Rust-Based Performance**
- **[Candle](https://github.com/huggingface/candle)** - Minimalist ML framework for Rust
  - **Advantage**: Memory safety, excellent performance
  - **Use Case**: Production systems requiring reliability

- **[ZML](https://github.com/zml/zml)** - High performance AI inference stack built for production
  - **Architecture**: [@ziglang](https://github.com/ziglang) / [@openxla](https://github.com/openxla) / MLIR / [@bazelbuild](https://github.com/bazelbuild)
  - **Focus**: Production-grade deployment infrastructure

- **[luminal](https://github.com/jafioti/luminal)** - Deep learning at the speed of light in Rust
  - **Target**: SOTA performance on M1 Pro (50+ tok/s), near SOTA on single NVIDIA GPUs (>100 tok/s)

**Apple Silicon Optimized**
- **[MLX Omni Server](https://github.com/madroidmaq/mlx-omni-server)** - Local inference server powered by Apple's MLX framework
  - **Features**: OpenAI-compatible API endpoints, optimized for M-series chips
  - **Use Case**: Local development on Apple Silicon

- **[MLX Server](https://www.mlxserver.com/)** - Easiest way to begin building on Apple's MLX framework
  - **Advantage**: Native Apple Silicon optimization

**Specialized Inference**
- **[LLamafile](https://github.com/Mozilla-Ocho/llamafile)** - Turn LLM models into multiplatform executables
  - **Benefit**: Single-file deployment, no dependencies

- **[Jan](https://github.com/janhq/jan)** - Open source alternative to ChatGPT that runs 100% offline
  - **Focus**: Privacy, offline operation

- **[fastassert](https://github.com/phospho-app/fastassert)** - Dockerized LLM inference server with constrained output (JSON mode)
  - **Built on**: vLLM and outlines
  - **Use Case**: Structured output requirements

- **[nm-vllm](https://github.com/neuralmagic/nm-vllm)** - High-throughput and memory-efficient inference with sparse compression

### **Cloud & Distributed Deployment**

**Multi-Cloud Solutions**
- **[SkyPilot](https://skypilot.readthedocs.io/en/latest/)** - Run LLMs and AI on any cloud
  - **Features**: Cost optimization, auto-scaling, spot instances
  - **Documentation**: [SkyPilot Docs](https://skypilot.readthedocs.io/en/latest/)

- **[LoraX](https://github.com/predibase/lorax)** - Multi-LoRA inference server that scales to 1000s of fine-tuned LLMs
  - **Documentation**: [LoraX Docs](https://loraexchange.ai/)
  - **Use Case**: Serving multiple fine-tuned models efficiently

**Python Bindings**
- **[LLama Cpp Python Binding](https://llama-cpp-python.readthedocs.io/en/latest/)** - OpenAI compatible web server

**Resource Collections**
- **[List of tools that serve AI locally](https://github.com/janhq/awesome-local-ai)** - Comprehensive repository of local AI tools

---

## 🎓 **Model Training & Fine-Tuning**

### **Fine-Tuning Frameworks**

**High-Performance Training**
- **[unsloth](https://github.com/unslothai/unsloth)** - 5X faster, 60% less memory QLoRA fine-tuning
  - **Documentation**: [Unsloth Docs](https://github.com/unslothai/unsloth/tree/main#-documentation)
  - **Performance**: 2x faster fine-tuning for Qwen3, Llama 4, DeepSeek-R1, Gemma 3

- **[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)** - Unified efficient fine-tuning of 100+ LLMs & VLMs
  - **Recognition**: ACL 2024
  - **Coverage**: Supports vast range of models

**Specialized Training Tools**
- **[peft](https://github.com/huggingface/peft)** - 🤗 PEFT: State-of-the-art Parameter-Efficient Fine-Tuning
  - **Method**: Parameter-efficient approaches
  - **Integration**: HuggingFace ecosystem

- **[Torchtune](https://github.com/pytorch/torchtune)** - Native-PyTorch library for LLM fine-tuning
  - **Advantage**: Pure PyTorch implementation

- **[LLMTuner](https://github.com/promptslab/LLMTuner)** - Tune LLM in few lines of code
  - **Focus**: Simplicity and ease of use

- **[LMFlow](https://github.com/OptimalScale/LMFlow)** - Extensible toolkit for finetuning and inference of large foundation models
  - **Features**: Includes Lisa Finetuning
  - **Motto**: Large Models for All

### **Training Infrastructure**

**Research Platforms**
- **[OLMo](https://github.com/allenai/OLMo)** - Modeling, training, eval, and inference code for [OLMo](https://allenai.org/olmo)
  - **Source**: Allen Institute for AI
  - **Focus**: Open research in language modeling

- **[Lightning Thunder](https://github.com/Lightning-AI/lightning-thunder)** - Source to source compiler for PyTorch
  - **Benefit**: Makes PyTorch programs faster on single accelerators and distributed

- **[Oumi](https://github.com/oumi-ai/oumi)** - Everything you need to build state-of-the-art foundation models, end-to-end

### **Training Resources & Guides**

**Educational Materials**
- **[Documentation from Premai about Finetuning](https://book.premai.io/state-of-open-source-ai/fine-tuning/)**
- **[Efficient finetuning of Llama 3 with FSDP QDoRA](https://www.answer.ai/posts/2024-04-26-fsdp-qdora-llama3.html)** - Blog article explaining state-of-the-art QDoRA fine-tuning method

---

## 🔧 **Model Optimization**

### **Quantization Techniques**

**Advanced Quantization**
- **[Aimet](https://github.com/quic/aimet)** - Advanced quantization and compression techniques for trained neural network models
  - **Source**: Qualcomm Innovation Center
  - **Focus**: Production-ready optimization

- **[hqq](https://github.com/mobiusml/hqq)** - Official implementation of Half-Quadratic Quantization (HQQ)
  - **Performance**: Fast and accurate model quantizer that skips calibration data
  - **Speed**: Can quantize Llama2-70B model in only 4 minutes! 🚀
  - **Implementation**: Super simple (just a few lines of code)

### **Inference Control & Optimization**

**Controlled Generation**
- **[Guidance](https://github.com/guidance-ai/guidance)** - A guidance language for controlling large language models
  - **Purpose**: Precise control over model outputs
  - **Use Case**: Structured generation workflows

- **[AICI](https://github.com/microsoft/AICI)** - AICI: Prompts as (Wasm) Programs
  - **Innovation**: Controlling inference using Wasm programs
  - **Source**: Microsoft Research
  - **Advantage**: Programmable inference control

**Advanced Techniques**
- **[Transformer Head](https://github.com/center-for-humans-and-machines/transformer-heads)** - Toolkit for attaching, training, saving and loading of new heads for transformer models

- **[Representation Engineering](https://vgel.me/posts/representation-engineering/)** - Representation Engineering Mistral-7B an Acid Trip 💊

---

## 📊 **Embeddings & Vector Operations**

### **Core Concepts & Theory**

**Fundamental Understanding**
- **[What are embeddings and how do they work?](https://vickiboykis.com/what_are_embeddings/)** - Comprehensive book by Vicki Boykis
  - **[GitHub Repository](https://github.com/veekaybee/what_are_embeddings)**
  - **[PDF Version](https://raw.githubusercontent.com/veekaybee/what_are_embeddings/main/embeddings.pdf)**

**Advanced Research**
- **[Fine-tuning language models improves performance by enhancing existing mechanisms](https://finetuning.baulab.info/)** - Evidence of consistent circuit functionality in entity tracking tasks
- **[Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka)** - HuggingFace guide to efficient embeddings
- **[Binary Embeddings Cohere](https://txt.cohere.com/int8-binary-embeddings/)** - Efficient embedding representations

### **Vector Database Solutions**

**High-Performance Databases**
- **[pgvectorscale](https://github.com/timescale/pgvectorscale/)** - A complement to pgvector for high performance, cost efficient vector search on large workloads
  - **Focus**: Enterprise-scale vector operations
  - **Integration**: PostgreSQL ecosystem

---

## ✍️ **Prompt Engineering**

### **Techniques & Patterns**

**Core Methodologies**
- [Summoning the Magic of Prompts: A Deep Dive into Prompt Engineering Patterns](../01-articles/prompt_engineering_patterns/README.md)
- [Mastering the art of prompt engineering (English)](../01-articles/2024-05-29_mastering-prompt-engineering_us.md)
- [Mastering the art of prompt engineering (French)](../01-articles/2024-05-29_mastering_prompt_engineering_fr.md)

**Comprehensive Resources**
- **[A list of prompt engineering techniques](https://aman.ai/primers/ai/prompt-engineering/)** - Comprehensive collection by Aman.ai

### **Advanced Frameworks**

**Production Libraries**
- **[Claude Anthropic Prompts Library](https://docs.anthropic.com/claude/page/prompts)** - Explore optimized prompts for business and personal tasks
- **[Navigating the Prompt Engineering Landscape: A Comprehensive Survey for NLP Practitioners](https://arxiv.org/pdf/2407.12994)** - Academic survey of prompt engineering

**Optimization Tools**
- **[Sammo](https://github.com/microsoft/sammo)** - Structure-aware Multi-Objective Metaprompt Optimization
  - **Source**: Microsoft Research
  - **Purpose**: Automated prompt optimization

---

## 🔍 **RAG & Knowledge Systems**

### **Advanced RAG Frameworks**

**Next-Generation Systems**
- **[RAGFlow](https://github.com/infiniflow/ragflow)** - Open-source RAG engine based on deep document understanding
  - **Strength**: Advanced document processing capabilities
  - **Focus**: Complex document workflows

- **[LightRAG](https://github.com/HKUDS/LightRAG)** - Knowledge graph RAG with entity relationship understanding
  - **Innovation**: Combines knowledge graphs with RAG
  - **Use Case**: Connected knowledge systems

- **[Quivr](https://github.com/QuivrHQ/quivr)** - Opinionated RAG for integrating GenAI in your apps
  - **Focus**: Production-ready integration

**Core Framework**
- **[LlamaIndex](https://www.llamaindex.ai/)** - Turn your enterprise data into production-ready LLM applications 🦙
  - **Ecosystem**: [LlamaHub](https://llamahub.ai/) for data connectors
  - **Parsing**: [LlamaParse](https://cloud.llamaindex.ai/) for advanced document processing

### **Vector & Search Technologies**

**High-Performance Search**
- **[pgvectorscale](https://github.com/timescale/pgvectorscale/)** - High-performance vector search for large workloads
- **[byaldi](https://github.com/AnswerDotAI/byaldi)** - Late-interaction multi-modal models (ColPali) for document search
- **[Weaviate](https://weaviate.io/)** - Vector database with hybrid search capabilities
- **[Qdrant](https://qdrant.tech/)** - High-performance vector similarity search engine

### **Document Processing**

**Advanced Extraction**
- **[zerox](https://github.com/getomni-ai/zerox)** - OCR & document extraction using vision models
- **[FireCrawl](https://github.com/mendableai/firecrawl)** - Turn entire websites into LLM-ready markdown
- **[lumentis](https://github.com/hrishioa/lumentis)** - Generate beautiful docs from transcripts and unstructured information
- **[Unstructured](https://unstructured.io/)** - Transform documents for LLM applications

### **Knowledge Graph Integration**

**Graph-Enhanced RAG**
- **[MindGraph](https://github.com/yoheinakajima/MindGraph)** - AI-powered knowledge graph generation and querying
- **[Neo4j Vector Index](https://neo4j.com/docs/cypher-manual/current/indexes-for-vector-search/)** - Graph database with vector search
- **[Microsoft GraphRAG](https://github.com/microsoft/graphrag)** - Knowledge graph enhanced RAG
- **[LangChain Graph](https://python.langchain.com/docs/use_cases/graph/)** - Graph-based question answering

---

## 🔊 **Voice & Speech Technologies**

### **Revolutionary Speech AI Models**

**Kyutai Labs Breakthroughs**
- **[Moshi](https://github.com/kyutai-labs/moshi)** - Real-time full-duplex speech-text foundation model
  - **Latency**: 160ms theoretical (200ms practical on L4 GPU)
  - **Architecture**: 7B parameter temporal transformer + depth transformer
  - **Capabilities**: Bidirectional conversation with inner monologue
  - **Platforms**: PyTorch, MLX (Apple Silicon), Rust, Swift
  - **Live Demo**: [moshi.chat](https://moshi.chat)

- **[Delayed Streams Modeling](https://github.com/kyutai-labs/delayed-streams-modeling)** - Advanced streaming STT
  - **kyutai/stt-2.6b-en**: English-only, 2.6B params, 2.5s delay
  - **kyutai/stt-1b-en_fr**: English/French, 1B params, 0.5s delay + semantic VAD
  - **Performance**: Real-time streaming with word-level timestamps
  - **Scale**: Production servers handle 64 simultaneous connections at 3x real-time

- **[Unmute](https://unmute.sh/)** - Advanced real-time speech processing and enhancement platform
  - **Features**: Real-time speech enhancement and processing
  - **Deployment**: Production deployment of Kyutai models

### **Mimi Neural Audio Codec**

**Technical Specifications**
- **Input**: 24 kHz audio
- **Output**: 12.5 Hz representation  
- **Bandwidth**: 1.1 kbps with 80ms latency
- **Architecture**: Transformer-enhanced encoder/decoder
- **Performance**: Outperforms SpeechTokenizer and SemantiCodec

**Key Features**
- Fully causal and streaming
- Matches WavLM representations without delays
- Adversarial training with feature matching
- Multiple implementation backends

### **Traditional Speech Tools**

**Production-Ready Tools**
- **[whisper](https://github.com/openai/whisper)** - General-purpose speech recognition model
  - **Capabilities**: Multilingual speech recognition, translation, language identification
  - **Training**: Large dataset of diverse audio

- **[MeloTTS](https://github.com/myshell-ai/MeloTTS)** - High-quality text-to-speech
- **[VoiceCraft](https://github.com/jasonppy/VoiceCraft)** - Zero-shot speech editing

### **Specialized Audio Frameworks**

**Privacy-Focused Solutions**
- **[Flowneum](https://github.com/floneum/floneum)** - A toolkit for controllable, private AI on consumer hardware in Rust
- **[Kalosm](https://floneum.com/kalosm/)** - Open source framework for private language, audio, and image models in Rust

---

## 🌐 **Model Context Protocol (MCP)**

### **What is Model Context Protocol?**
The Model Context Protocol (MCP) is an emerging standard that enables AI applications to securely connect to data sources and tools. It provides a unified way for AI systems to interact with external resources while maintaining security and consistency.

### **Core MCP Tools**
- **[Model Context Protocol](https://modelcontextprotocol.io/)** - Standardized AI application interfaces
- **[MCP Tools](https://github.com/f/mcptools)** - Swiss Army Knife for MCP Servers
- **[Active Pieces](https://github.com/activepieces/activepieces)** - AI Agents & MCPs & AI Workflow Automation with 280+ MCP servers
- **[MCP Agent](https://github.com/lastmile-ai/mcp-agent)** - Build effective agents using Model Context Protocol

### **Popular MCP Servers**
- **File System Server** - Access local files and directories
- **Database Server** - Connect to SQL databases
- **Git Server** - Interact with Git repositories  
- **Web Search Server** - Perform web searches
- **Calendar Server** - Access calendar data
- **Slack Server** - Integrate with Slack workspaces
- **GitHub Server** - Repository management and CI/CD integration
- **Jira Server** - Issue tracking and project management
- **Docker Server** - Container management and deployment
- **AWS Server** - Cloud resource management and automation

### **MCP Integration Examples**

#### **With AI Coding Assistants**
- **[Cline](https://github.com/cline/cline)** - VS Code extension with native MCP server support for enhanced development workflows
- **[Continue](https://continue.dev/)** - Open-source autopilot with MCP integrations
- **[Cursor Directory](https://cursor.directory/)** - Discover MCP servers optimized for Cursor AI

#### **Popular MCP Server Implementations**
- **[MCP Server SQLite](https://github.com/modelcontextprotocol/sqlite)** - Database operations and schema management
- **[MCP Server Filesystem](https://github.com/modelcontextprotocol/servers)** - File operations with safety controls
- **[MCP Server Git](https://github.com/modelcontextprotocol/git)** - Version control operations
- **[MCP Server Brave Search](https://github.com/modelcontextprotocol/brave-search)** - Web search capabilities
- **[MCP Server Puppeteer](https://github.com/modelcontextprotocol/puppeteer)** - Browser automation and web scraping

### **MCP Benefits**
- **Standardized Integration** - Consistent way to connect AI to external data
- **Security First** - Built-in permission and access controls
- **Tool Reusability** - Write once, use across multiple AI applications
- **Ecosystem Growth** - Growing library of pre-built servers

---

## 📚 **Additional Learning Resources**

### **Key Articles & Concepts**
- [Demystifying Classifiers and Embeddings](../01-articles/embeddings/README.md)
- [Bridging the Gap Between Thinking and Doing: FaR Framework](../01-articles/far/README.md)  
- [Beyond Prompt Engineering: DSPy for Modular LM Programs](../01-articles/dspy/README.md)

### **Application Use Cases**
- [What are the common use cases of LLM Applications?](../01-articles/llm_applications_use_cases/README.md)

### **Latest Updates**
- [2025 AI Landscape Updates](./2025-ai-updates.md) - Latest breakthroughs and technologies

---

**🔗 Navigation**
- [← Back to Reference Hub](./README.md)
- [2025 Updates →](./2025-ai-updates.md)
- [Tools Directory →](../tools/README.md)
