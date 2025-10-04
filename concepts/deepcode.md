# 🤖 DeepCode: Open Agentic Coding

**DeepCode** is an open-source AI-powered development platform that automates code generation and implementation tasks using multi-agent systems. It transforms research papers, natural language descriptions, and requirements into production-ready code with comprehensive testing and documentation.

**[GitHub Repository](https://github.com/HKUDS/DeepCode)** — Open-source multi-agent coding platform from HKU Data Intelligence Lab.

**[PyPI Package](https://pypi.org/project/deepcode-hku/)** — Install with `pip install deepcode-hku`.

---

## 🚀 Key Capabilities

### Paper2Code: Research to Production

Automated implementation of complex algorithms from research papers into high-quality, production-ready code. Accelerates algorithm reproduction by handling the complex translation from academic concepts to working implementations.

### Text2Web: Natural Language to Frontend

Translates plain textual descriptions into fully functional, visually appealing front-end web code. Enables rapid interface creation from natural language requirements.

### Text2Backend: Requirements to Backend Systems

Generates efficient, scalable, and feature-rich back-end code from simple text inputs. Streamlines server-side development with automated architecture design and implementation.

## 🏗️ Multi-Agent Architecture

DeepCode employs a sophisticated multi-agent system with specialized roles:

### Core Agents

- **🎯 Central Orchestrating Agent**: Coordinates workflow execution and makes strategic decisions
- **📝 Intent Understanding Agent**: Performs deep semantic analysis of user requirements
- **📄 Document Parsing Agent**: Processes complex technical documents and research papers
- **🏗️ Code Planning Agent**: Performs architectural design and technology stack optimization
- **🔍 Code Reference Mining Agent**: Discovers relevant repositories and frameworks
- **📚 Code Indexing Agent**: Builds comprehensive knowledge graphs of codebases
- **🧬 Code Generation Agent**: Synthesizes information into executable implementations

### Intelligence Processing Flow

```mermaid
graph TD
    A[Input Layer] --> B[Central Orchestration]
    B --> C[Analysis Agents]
    C --> D[Planning]
    D --> E[Implementation]
    E --> F[Output Delivery]
    
    A --> G[Research Papers]
    A --> H[Natural Language]
    A --> I[URLs & Documents]
    A --> J[Files (PDF, DOCX)]
    
    B --> K[Strategic Decisions]
    B --> L[Agent Management]
    
    C --> M[Text/Document Processing]
    C --> N[Requirements Extraction]
    
    D --> O[Architecture Design]
    D --> P[Optimization]
    
    E --> Q[Code Generation]
    E --> R[Testing]
    E --> S[Documentation]
    
    F --> T[Complete Codebase]
    F --> U[Test Suite]
    F --> V[Documentation]
    F --> W[Deployment Ready]
```

## 🛠️ Technical Features

### MCP Integration

Powered by the Model Context Protocol (MCP) for standardized tool integration:

- **🔍 Brave Search**: Web search capabilities via Brave Search API
- **🌐 Bocha-MCP**: Alternative search with independent API access
- **📂 Filesystem**: Local file and directory management
- **🌐 Fetch**: Web content retrieval and extraction
- **📥 GitHub Downloader**: Repository cloning and analysis
- **📋 File Downloader**: Document processing (PDF, DOCX to Markdown)
- **⚡ Command Executor**: System command execution
- **🧬 Code Implementation**: Comprehensive code reproduction
- **📚 Code Reference Indexer**: Intelligent code repository search
- **📄 Document Segmentation**: Smart processing of large technical documents

### Advanced Capabilities

- **🧬 Research-to-Production Pipeline**: Multi-modal document analysis extracting algorithmic logic
- **🪄 Natural Language Code Synthesis**: Context-aware code generation with architectural consistency
- **⚡ Automated Prototyping**: Intelligent scaffolding with dependency analysis
- **💎 Quality Assurance**: Integrated testing, static analysis, and documentation synthesis
- **🔮 CodeRAG Integration**: Retrieval-augmented generation with semantic vector embeddings

## 🚀 Quick Start

### Installation

```bash
# Install DeepCode package
pip install deepcode-hku

# Download configuration files
curl -O https://raw.githubusercontent.com/HKUDS/DeepCode/main/mcp_agent.config.yaml
curl -O https://raw.githubusercontent.com/HKUDS/DeepCode/main/mcp_agent.secrets.yaml
```

### Configuration

1. **API Keys Setup**: Configure OpenAI/Anthropic API keys in `mcp_agent.secrets.yaml`
2. **Search Configuration**: Set up Brave Search or Bocha-MCP API keys (optional)
3. **Document Segmentation**: Configure intelligent document processing (optional)

### Launch Application

```bash
# Web Interface (Recommended)
deepcode
# Opens at http://localhost:8501

# CLI Interface (Advanced)
python cli/main_cli.py
```

## 🎯 Use Cases & Applications

### Academic Research Acceleration

- **Algorithm Implementation**: Convert complex research papers into working code
- **Reproducibility**: Automated reproduction of academic algorithms
- **Rapid Prototyping**: Quick implementation of novel research ideas

### Product Development

- **MVP Generation**: Transform concepts into testable prototypes
- **Full-Stack Development**: End-to-end application generation from requirements
- **Feature Implementation**: Automated implementation of product features

### Enterprise Solutions

- **Legacy System Migration**: Automated migration and modernization
- **API Development**: Rapid creation of RESTful services and integrations
- **Data Processing Pipelines**: Automated ETL and data transformation systems

## 💡 Examples & Demonstrations

### Paper2Code Workflow

1. **Input**: Upload research paper PDF or provide URL
2. **Analysis**: Multi-agent system extracts algorithms and methodologies
3. **Planning**: Architectural design and technology stack selection
4. **Implementation**: Generate production-ready code with tests
5. **Output**: Complete codebase with documentation and deployment scripts

### Text2Web Example

```python
# Input: "Create a modern dashboard for financial data visualization"
# Output: Complete React/Next.js application with:
# - Interactive charts and graphs
# - Real-time data updates
# - Responsive design
# - API integration endpoints
```

### Text2Backend Example

```python
# Input: "Build a user authentication system with JWT tokens"
# Output: Complete backend with:
# - User registration/login endpoints
# - JWT token management
# - Database models and migrations
# - Security middleware
# - API documentation
```

## 🔧 Advanced Configuration

### Document Segmentation

Handles large research papers exceeding LLM token limits:

```yaml
# mcp_agent.config.yaml
document_segmentation:
  enabled: true
  size_threshold_chars: 50000
  semantic_preservation: true
```

### Multi-Search Configuration

```yaml
# Choose search provider
default_search_server: "brave"  # or "bocha-mcp"

# API key configuration
brave:
  env:
    BRAVE_API_KEY: "your_api_key_here"
```

### Performance Optimization

- **Parallel Processing**: Multi-threaded agent coordination
- **Memory Management**: Efficient context handling for large codebases
- **Caching**: Intelligent caching of code patterns and dependencies

## 📊 Performance & Quality

### Quality Assurance Features

- **Automated Testing**: Comprehensive test suite generation
- **Static Analysis**: Code quality and security validation
- **Documentation**: Auto-generated API docs and usage guides
- **Type Safety**: Proper type annotations and validation

### Benchmarking

- **PaperBench**: Comprehensive evaluation suite for paper reproduction
- **Accuracy Metrics**: Performance comparison with state-of-the-art systems
- **Success Analytics**: Statistical analysis across paper categories

## 🌟 Unique Advantages

### Research Acceleration

- **Zero Implementation Time**: Convert papers to code in minutes
- **Academic Productivity**: Focus on research, not implementation
- **Reproducibility**: Consistent, automated algorithm reproduction

### Development Efficiency

- **Multi-Modal Input**: Support for papers, text, URLs, and documents
- **Full-Stack Generation**: Complete applications from single inputs
- **Production Ready**: Includes testing, documentation, and deployment

### Enterprise Scalability

- **MCP Integration**: Standardized tool ecosystem
- **Multi-Agent Orchestration**: Complex workflow automation
- **Quality Assurance**: Enterprise-grade code validation

## 📈 Community & Ecosystem

- **🏛️ HKU Data Intelligence Lab**: Developed by University of Hong Kong researchers
- **📚 Open Source**: MIT licensed with active community development
- **🌟 7.3K+ Stars**: Popular GitHub repository with growing adoption
- **🔄 Regular Updates**: Active development with new features and improvements

## 🎬 Getting Started Resources

- **[Introduction Video](https://youtu.be/PRgmP8pOI08)**: Complete platform overview and demonstrations
- **[Live Demos](https://github.com/HKUDS/DeepCode#live-demonstrations)**: Interactive examples and use cases
- **[Discord Community](https://discord.gg/yF2MmDJyGJ)**: Active user community and support
- **[Documentation](https://github.com/HKUDS/DeepCode#readme)**: Comprehensive setup and usage guides

---

*See also: [Amp: Agentic Coding Platform](./amp.md), [AI Agents](./ai-agents.md), [MCP (Model Context Protocol)](./mcp.md), [Vibe Coding](./vibe-coding.md)*
