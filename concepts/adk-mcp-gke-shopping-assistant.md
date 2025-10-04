# ADK + MCP Integration: AI Shopping Assistant on GKE

Practical implementation of an AI-powered shopping assistant built on Google Kubernetes Engine (GKE) using Google Agent Development Kit (ADK) and Model Context Protocol (MCP) to enhance the Online Boutique microservices demo.

---

**[How I Built an AI Shopping Assistant on GKE with Google ADK + MCP (GKE Hackathon)](https://medium.com/google-cloud/how-i-built-an-ai-shopping-assistant-on-gke-with-google-adk-mcp-gke-hackathon-0c8675d8aa6b)** 🛒 — *Complete hackathon submission demonstrating practical ADK + MCP integration. Builds a conversational AI layer on top of Google's Online Boutique microservices using Gemini 2.0 Flash, with full GKE deployment. Includes MCP server implementation exposing gRPC services as tools, ADK agent development, and production deployment patterns.*

---

## 🏗️ System Architecture

### Core Components

- **ADK Web Interface**: User-facing chat interface for conversational shopping assistance
- **ADK Agent (Gemini 2.0 Flash)**: LLM-powered agent handling natural language queries and function calling
- **MCP Toolset**: Protocol layer exposing microservice functions as callable tools
- **gRPC Microservices**: Original Online Boutique services (catalog, cart, checkout, shipping, payment, etc.)
- **GKE Cluster**: Kubernetes orchestration for all components

### Data Flow

1. User interacts via ADK Web chat interface
2. ADK Agent interprets queries using Gemini 2.0 Flash
3. Agent triggers function calls through MCP Toolset
4. MCP Server makes gRPC calls to Online Boutique microservices
5. Results aggregated and returned through conversational interface

## 🔧 Implementation Steps

### 1. gRPC and Protobuf Setup

- Use `hipstershop.proto` from Online Boutique repository
- Generate Python gRPC stubs with `grpc_tools.protoc`
- Creates message classes and service stubs for all microservices

### 2. MCP Server Development

- Wrap gRPC clients in MCP tools
- Support both HTTP and STDIO modes
- Expose catalog, cart, checkout, shipping, payment, email, ads, and currency services

### 3. MCP Server Packaging

- Published to PyPI as `ai-boutique-assit-mcp`
- Enables easy installation and reuse
- Supports both standalone HTTP server and ADK-integrated STDIO modes

### 4. ADK Agent Creation

- Simple agent configuration using Google ADK
- Integrates MCP Toolset for function calling
- Uses Gemini 2.0 Flash for intelligent query processing

### 5. GKE Deployment

- Containerize all components
- Deploy microservices, MCP server, and ADK agent
- Configure Kubernetes services and ingress
- Enable inter-service communication within cluster

## 📦 Key Resources

- **[MCP Server Repository](https://github.com/arjunprabhulal/ai-boutique-assit-mcp)** — Complete MCP server implementation exposing Online Boutique microservices
- **[ADK Client Repository](https://github.com/arjunprabhulal/ai-boutique-assit-mcp-client)** — ADK agent with MCP integration
- **[PyPI Package](https://pypi.org/project/ai-boutique-assit-mcp/)** — Published MCP server for easy installation
- **[Online Boutique Demo](https://github.com/GoogleCloudPlatform/microservices-demo)** — Base microservices application
- **[GKE Turns 10 Hackathon](https://gketurns10.devpost.com/)** — Original hackathon context

## 🚀 Getting Started

### Local Development

```bash
# Install MCP server
pip install ai-boutique-assit-mcp

# Or from source
git clone https://github.com/arjunprabhulal/ai-boutique-assit-mcp
cd ai-boutique-assit-mcp
pip install -e .
```

### GKE Deployment

1. Deploy Online Boutique microservices to GKE
2. Deploy MCP server as Kubernetes deployment
3. Deploy ADK agent with MCP Toolset integration
4. Configure ingress for ADK Web interface

## 🎯 Key Features Demonstrated

- **Conversational Commerce**: Natural language shopping assistance
- **Function Calling**: MCP-enabled tool integration with microservices
- **Multi-Modal Responses**: Text, product images, cart updates, recommendations
- **Production Deployment**: Full GKE orchestration and scaling
- **Protocol Integration**: ADK + MCP interoperability

## 📈 Impact & Learnings

- Successfully layered AI capabilities onto existing microservices without code changes
- Demonstrated practical ADK + MCP integration patterns
- Showed conversational AI enhancement of traditional e-commerce
- Provided reusable MCP server implementation for similar projects

---

*See also: [MCP (Model Context Protocol)](./mcp.md), [Google A2A and ADK Multi-Agent Architecture](./google-a2a-adk-multi-agent.md), [Agent Protocols](./agent-protocols.md)*

