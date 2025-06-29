# 🛠️ AI Tools Master Directory

> The complete catalog of AI tools, frameworks, and platforms - organized by purpose and expertise level

## 🎯 **Quick Tool Finder**

| I need to... | Best Tool Category | Recommended For |
|-------------|-------------------|-----------------|
| **Start with AI** | [Beginner Tools](#-beginner-tools) | First-time users |
| **Build applications** | [Development Frameworks](#-development-frameworks) | Developers |
| **Serve models** | [Model Serving](#-model-serving--inference) | Production teams |
| **Create AI agents** | [Agent Frameworks](#-ai-agent-frameworks) | Advanced developers |
| **Work with data** | [RAG & Data Tools](#-rag--data-tools) | Data-focused projects |
| **Generate code** | [AI Coding Tools](#-ai-coding-tools) | Development teams |
| **Deploy at scale** | [Production Tools](#-production--research-tools) | Infrastructure teams |
| **Fine-tune models** | [Training & Fine-tuning](#-model-training--fine-tuning) | ML Engineers |
| **Work with voice** | [Voice & Speech](#-voice--speech-technologies) | Audio applications |
| **Use latest 2025 tools** | [2025 Breakthroughs](#-2025-breakthrough-tools) | Early adopters |

### 🔗 **Quick Navigation**
- 👉 **Beginner**: [Getting Started Tools](#-beginner-tools)
- 🟡 **Intermediate**: [Development Frameworks](#-development-frameworks)  
- 👉 **Advanced**: [Production & Research Tools](#-production--research-tools)
- 🆕 **Latest**: [2025 AI Breakthroughs](#-2025-breakthrough-tools)

---

## 🌱 Beginner-Friendly Tools

### Local AI Runtime
| Tool | Purpose | Best For |
|------|---------|----------|
| [Ollama](https://ollama.com/) | Run models locally | First-time users, offline development |
| [LM Studio](https://lmstudio.ai/) | GUI for local models | Non-technical users |
| [Jan](https://github.com/janhq/jan) | ChatGPT alternative | Privacy-focused local chat |

### Getting Started Frameworks
| Tool | Purpose | Learning Curve |
|------|---------|----------------|
| [LangChain](https://langchain.com/) | LLM application framework | 🟡 Moderate |
| [instructor](https://jxnl.github.io/instructor/) | Structured outputs | 🟢 Easy |
| [QLLM](https://github.com/quantalogic/qllm) | CLI for multiple LLMs | 🟢 Easy |

---

## 💻 Development Frameworks

### Core Application Frameworks

#### **LangChain Ecosystem** 🦜
- **[LangChain](https://www.langchain.com/)** - The most popular LLM framework
  - **Use for**: General LLM applications, prototyping
  - **Strength**: Extensive ecosystem, lots of examples
  - **Documentation**: [Getting Started](https://python.langchain.com/docs/get_started/introduction)

#### **LlamaIndex Ecosystem** 🦙
- **[LlamaIndex](https://www.llamaindex.ai/)** - Data-focused LLM applications
  - **Use for**: RAG systems, document processing
  - **Strength**: Excellent for enterprise data integration
  - **Best fit**: When working with proprietary data

#### **Modern Alternatives**
- **[ell](https://docs.ell.so/)** - Language model programming framework
  - **Use for**: Clean, type-safe LLM programming
  - **Strength**: Modern Python patterns, excellent DX
  
- **[marvin](https://www.askmarvin.ai/)** - AI toolkit for natural language interfaces
  - **Use for**: Reliable, scalable AI interfaces
  - **Strength**: Production-ready patterns

### Structured Output Tools

| Tool | Purpose | Status | Best For |
|------|---------|--------|----------|
| [instructor](https://jxnl.github.io/instructor/) | JSON from LLMs | ⭐ **Recommended** | Data extraction, API responses |
| [BAML](https://github.com/BoundaryML/baml) | Structured data from LLMs | 🆕 **New** | Multi-language projects |
| [Guidance](https://github.com/guidance-ai/guidance) | Controlled generation | 🔧 **Advanced** | Precise output control |

---

## 🤖 AI Agent Frameworks

### Production-Grade Agents

#### **[Quantalogic](https://github.com/quantalogic/quantalogic)** ⭐
- **Purpose**: Powerful agentic framework
- **Best for**: Complex automation, code generation
- **Status**: Production-ready

#### **[Pydantic Agents](https://ai.pydantic.dev/agents/)**
- **Purpose**: Production-grade agent framework  
- **Best for**: Type-safe agent development
- **Status**: Enterprise-ready

#### **[CrewAI](https://github.com/joaomdmoura/crewAI)**
- **Purpose**: Multi-agent collaboration
- **Best for**: Team-based AI workflows
- **Status**: Popular choice

### Specialized Agent Tools

#### Computer Control
| Tool | Capability | Use Case |
|------|------------|----------|
| [Open Interpreter](https://github.com/KillianLucas/open-interpreter/) | Natural language computer interface | General automation |
| [Screen Agents](https://github.com/niuzaisheng/ScreenAgent) | Visual computer control | GUI automation |
| [SWE Agents](https://github.com/princeton-nlp/SWE-agent) | Software engineering | Code-related tasks |

#### Memory & Learning
| Tool | Purpose | Integration |
|------|---------|-------------|
| [MemGPT](https://memgpt.ai/) | Long-term memory | Enterprise applications |
| [Cognee](https://github.com/topoteretes/cognee) | Memory for AI apps | Python applications |
| [Zep](https://github.com/getzep/zep) | Memory for assistants | Multi-platform |

---

## 🚀 Model Serving & Inference

### High-Performance Servers

#### **[vLLM](https://github.com/vllm-project/vllm)** ⭐
- **Purpose**: High-throughput LLM serving
- **Best for**: Production deployments
- **Performance**: Industry standard for speed
- **Documentation**: [vLLM Docs](https://docs.vllm.ai/en/latest/)

#### **[Ollama](https://github.com/ollama/ollama)**
- **Purpose**: Simple local deployment
- **Best for**: Development, small deployments
- **Advantage**: Zero-config setup

### Specialized Solutions

#### Rust-Based Performance
| Tool | Purpose | Performance Target |
|------|---------|-------------------|
| [Candle](https://github.com/huggingface/candle) | Minimalist ML in Rust | Production speed |
| [luminal](https://github.com/jafioti/luminal) | Deep learning in Rust | M1 Pro: 50+ tok/s |

#### Apple Silicon Optimized
| Tool | Purpose | Platform |
|------|---------|----------|
| [MLX Omni Server](https://github.com/madroidmaq/mlx-omni-server) | MLX-powered inference | Apple Silicon |
| [MLX Server](https://www.mlxserver.com/) | Easy MLX development | macOS |

### Cloud & Distributed

#### **[SkyPilot](https://skypilot.readthedocs.io/en/latest/)**
- **Purpose**: Multi-cloud deployment
- **Best for**: Cost optimization, availability
- **Features**: Auto-scaling, spot instances

#### **[LoraX](https://github.com/predibase/lorax)**
- **Purpose**: Multi-LoRA inference server
- **Best for**: Serving 1000s of fine-tuned models
- **Documentation**: [LoraX Docs](https://loraexchange.ai/)

---

## 🔍 Data & RAG Tools

### RAG Frameworks

#### **[RagFlow](https://github.com/infiniflow/ragflow)** ⭐
- **Purpose**: RAG engine with deep document understanding
- **Strength**: Advanced document processing
- **Best for**: Complex document workflows

#### **[LightRAG](https://github.com/HKUDS/LightRAG)**
- **Purpose**: Knowledge graph RAG
- **Strength**: Relationship understanding
- **Best for**: Connected knowledge systems

### Vector Databases & Search
| Tool | Purpose | Scale |
|------|---------|-------|
| [pgvectorscale](https://github.com/timescale/pgvectorscale/) | High-performance vector search | Enterprise |
| [byaldi](https://github.com/AnswerDotAI/byaldi) | Multi-modal search | Research |

### Document Processing
| Tool | Purpose | Input Types |
|------|---------|-------------|
| [zerox](https://github.com/getomni-ai/zerox) | OCR & extraction | PDFs, images |
| [FireCrawl](https://github.com/mendableai/firecrawl) | Website to markdown | Web pages |
| [lumentis](https://github.com/hrishioa/lumentis) | Docs from transcripts | Audio, video |

---

## 🎨 Specialized Applications

### Voice & Audio
| Tool | Capability | Quality |
|------|------------|---------|
| [whisper](https://github.com/openai/whisper) | Speech recognition | ⭐ Industry standard |
| [MeloTTS](https://github.com/myshell-ai/MeloTTS) | Text-to-speech | High quality, multilingual |
| [VoiceCraft](https://github.com/jasonppy/VoiceCraft) | Speech editing | Zero-shot editing |

### UI & Interface Tools
| Tool | Purpose | Output |
|------|---------|--------|
| [OpenUI](https://github.com/wandb/openui) | Natural language to UI | Live rendering |
| [Screenshot to Code](https://github.com/abi/screenshot-to-code) | Design to code | HTML/React/Vue |
| [Vercel AI SDK](https://vercel.com/blog/ai-sdk-3-generative-ui) | Stream React components | React UIs |

---

## 🔧 Development Utilities

### Command Line Tools
| Tool | Purpose | Workflow Integration |
|------|---------|---------------------|
| [llm](https://llm.datasette.io/en/stable/) | CLI for multiple LLMs | Terminal workflows |
| [Code2prompt](https://github.com/raphaelmansuy/code2prompt) | Codebase to AI prompt | Code analysis |
| [plock](https://github.com/jasonjmcghee/plock) | Query LLM from anywhere | System integration |

### AI-Assisted Development
| Tool | Purpose | Integration |
|------|---------|-------------|
| [Aider](https://github.com/paul-gauthier/aider) | AI pair programming | Terminal |
| [Plandex](https://github.com/plandex-ai/plandex) | AI coding engine | Complex tasks |
| [AutoDev](https://github.com/unit-mesh/auto-dev) | AI coding wizard | Multi-language |

---

## 🏗️ Model Training & Optimization

### Fine-Tuning Frameworks
| Tool | Speed Improvement | Memory Reduction | Best For |
|------|------------------|------------------|----------|
| [unsloth](https://github.com/unslothai/unsloth) | 5x faster | 60% less | Quick experiments |
| [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | Unified platform | Varies | 100+ LLMs |
| [Torchtune](https://github.com/pytorch/torchtune) | Native PyTorch | Optimized | PyTorch users |

### Quantization & Optimization
| Tool | Purpose | Target |
|------|---------|--------|
| [hqq](https://github.com/mobiusml/hqq) | Half-quadratic quantization | 4-minute Llama2-70B |
| [AICI](https://github.com/microsoft/AICI) | Controlled generation | Precise outputs |

---

## 📊 Tool Selection Guide

### Choose by Project Type

#### **Building a Chatbot?**
1. **Beginner**: Ollama + LangChain
2. **Production**: vLLM + instructor + memory system
3. **Enterprise**: MemGPT + structured outputs

#### **Working with Documents?**
1. **Simple RAG**: LlamaIndex + pgvectorscale
2. **Advanced RAG**: RagFlow + knowledge graphs
3. **Document AI**: zerox + structured extraction

#### **Need AI Agents?**
1. **Code Generation**: Quantalogic
2. **Multi-agent**: CrewAI
3. **Computer Control**: Open Interpreter

#### **Production Deployment?**
1. **High Performance**: vLLM + SkyPilot
2. **Multi-model**: LoraX
3. **Edge Deployment**: Ollama + optimization

---

## 🚀 Getting Started Recommendations

### Week 1: Foundation
- Install: Ollama, Jupyter, LangChain
- Build: Simple chatbot
- Learn: Basic prompting

### Week 2: Data Integration  
- Try: LlamaIndex for RAG
- Experiment: Document processing
- Add: Vector database

### Week 3: Advanced Features
- Explore: Agent frameworks
- Add: Memory systems
- Try: Structured outputs

### Week 4: Production Prep
- Deploy: Using vLLM or similar
- Monitor: Output quality
- Scale: Based on needs

---

## 🆕 **2025 Breakthrough Tools**
*The latest AI innovations reshaping the landscape*

### **Revolutionary AI Code Editors**
- **[Cursor AI](https://cursor.sh/)** - AI-powered code editor with contextual understanding and codebase analysis
- **[Windsurf](https://codeium.com/windsurf)** - AI-first IDE with collaborative editing capabilities  
- **[GitHub Copilot Workspace](https://github.com/features/copilot)** - AI-powered development environments
- **[Replit Agent](https://replit.com/)** - Complete app development from natural language descriptions

### **Revolutionary UI Generation**
- **[v0 by Vercel](https://v0.dev/)** - Generate React components and full applications from text prompts
- **[Claude Engineer](https://github.com/Doriandarko/claude-engineer)** - Advanced AI coding assistant with file system operations
- **[Screenshot to Code](https://github.com/abi/screenshot-to-code)** - Drop in a screenshot and convert it to clean code
- **[OpenUI](https://github.com/wandb/openui)** - Describe UI using your imagination, then see it rendered live

### **Next-Generation Agent Platforms**
- **[Dify](https://github.com/langgenius/dify)** - Production-ready platform for agentic workflow development (22k+ stars)
- **[Anything LLM](https://github.com/Mintplex-Labs/anything-llm)** - All-in-one desktop AI with built-in agents, MCP compatibility
- **[Google ADK Python](https://github.com/google/adk-python)** - Google's toolkit for building sophisticated AI agents
- **[OpenAI Swarm](https://github.com/openai/swarm)** - Multi-agent orchestration framework

### **Computer Control & Browser Automation**
- **[Browser Use](https://github.com/browser-use/browser-use)** - Make websites accessible for AI agents (6k+ stars, actively maintained)
- **[OpenHands](https://github.com/All-Hands-AI/OpenHands)** - Code Less, Make More with autonomous development agents
- **[Nanobrowser](https://github.com/nanobrowser/nanobrowser)** - Chrome extension for AI-powered web automation
- **[Anthropic Computer Use](https://docs.anthropic.com/en/docs/computer-use)** - AI that can control computers directly

### **Model Context Protocol (MCP) Ecosystem**
- **[Model Context Protocol](https://modelcontextprotocol.io/)** - Standardized AI application interfaces
- **[MCP Tools](https://github.com/f/mcptools)** - Swiss Army Knife for MCP Servers
- **[Active Pieces](https://github.com/activepieces/activepieces)** - AI Agents & MCPs & AI Workflow Automation with 280+ MCP servers
- **[MCP Agent](https://github.com/lastmile-ai/mcp-agent)** - Build effective agents using Model Context Protocol

### **Revolutionary Voice AI Models - Kyutai Labs**
- **[Moshi](https://github.com/kyutai-labs/moshi)** - Real-time full-duplex voice conversation AI
  - **Latency**: 160ms theoretical (200ms practical on L4 GPU)
  - **Live Demo**: [moshi.chat](https://moshi.chat)
- **[Delayed Streams Modeling](https://github.com/kyutai-labs/delayed-streams-modeling)** - Advanced streaming speech processing
- **[Unmute](https://unmute.sh/)** - Production speech processing platform

### **Advanced Fine-Tuning & Model Optimization**
- **[Unsloth](https://github.com/unslothai/unsloth)** - 2x faster fine-tuning for Qwen3, Llama 4, DeepSeek-R1, Gemma 3 (Updated continuously)
- **[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)** - Unified efficient fine-tuning of 100+ LLMs & VLMs (ACL 2024)
- **[vLLM](https://github.com/vllm-project/vllm)** - High-throughput LLM serving (Updated hourly)

### **2025 Model Breakthroughs**
- **[OpenAI o3 & o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/)** - Advanced reasoning with "thinking with images" capability
- **[Claude 4 (Opus 4 & Sonnet 4)](https://anthropic.com/claude/opus)** - Anthropic's most powerful models for coding and AI agents
- **[DeepSeek R1](https://deepseek.com/)** - Open-source reasoning model challenging proprietary alternatives
- **[Tencent Hunyuan A13B](https://huggingface.co/tencent/Hunyuan-A13B-Instruct)** - 13B parameter instruction-following model

### **Advanced RAG & Knowledge Systems**
- **[RAGFlow](https://github.com/infiniflow/ragflow)** - Open-source RAG engine based on deep document understanding
- **[LightRAG](https://github.com/HKUDS/LightRAG)** - Knowledge graph RAG with entity relationship understanding
- **[Quivr](https://github.com/QuivrHQ/quivr)** - Opinionated RAG for integrating GenAI in your apps
- **[FireCrawl](https://github.com/mendableai/firecrawl)** - Turn entire websites into LLM-ready markdown (Updated daily)

---
*Last updated: {{ date }}*
*Tools count: 50+ curated selections*
