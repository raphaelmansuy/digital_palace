# Google A2A and ADK: Multi-Agent System Architecture

Comprehensive guide to architecting collaborative AI agent systems using Google's Agent-to-Agent (A2A) protocol and Agent Development Kit (ADK), demonstrated through a practical trading simulator example.

---

**[Architecting a Multi-Agent System with Google A2A and ADK (Google Cloud Blog)](https://medium.com/google-cloud/architecting-a-multi-agent-system-with-google-a2a-and-adk-4ced4502c86a)** 📚 — *In-depth architectural exploration of building multi-agent systems using Google's A2A protocol and ADK toolkit. Uses an Agentic Trading Simulator as a practical example, demonstrating how specialized agents (trading strategist and risk compliance officer) collaborate through standardized communication. Covers ADK components (BaseAgent, tools, events, runners) and A2A concepts (servers, clients, tasks, messages). Includes code examples, sequence diagrams, and deployment options for both local and Cloud Run environments.*

---

## 🏗️ Core Architecture Components

### Agentic Trading Simulator Overview

- **Simulator UI (Conductor)**: Orchestrates simulation loop, delegates thinking to specialized agents
- **AlphaBot ADK Agent (Trading Strategist)**: Analyzes market/portfolio data, determines trade actions using SMA crossover strategy
- **RiskGuard ADK Agent (Compliance Officer)**: Evaluates proposed trades against risk rules (position size, concentration limits)

### Google ADK (Agent Development Kit) Components

- **BaseAgent**: Core business logic class for agent reasoning (trading strategy in AlphaBot, risk evaluation in RiskGuard)
- **InvocationContext**: Passes input data (market data, portfolio state) into agent run method
- **BaseTool**: Enables external interactions (AlphaBot's A2ARiskCheckTool for communicating with RiskGuard)
- **Event**: Signals agent outputs, actions, or state updates back to the system
- **Runner**: Orchestrates agent lifecycle, handles events, invokes tools, manages flow
- **SessionService**: Provides state management across invocations (InMemorySessionService for AlphaBot's trading posture)

### A2A (Agent-to-Agent) Protocol Components

- **A2A Server**: Agent's public endpoint, validates JSON-RPC requests, routes to agent logic
- **A2A Client**: Initiates conversations via HTTP POST with JSON-RPC payloads
- **Agent Card**: Metadata for discovery (name, description, endpoint URL, capabilities)
- **Task**: Unit of work (tasks/send for request-response, tasks/sendSubscribe for streaming)
- **Message & Parts**: Data exchange using structured Parts (TextPart, FilePart, DataPart)
- **Artifact**: Returns complex results attached to task responses

## 🔗 Key Resources

- **[Agentic Trading Demo Repository](https://github.com/kweinmeister/agentic-trading)** — Complete implementation with AlphaBot, RiskGuard, and Simulator UI
- **[A2A Protocol Specification](https://github.com/google/A2A)** — Official GitHub repository with protocol details and samples
- **[Google ADK Documentation](https://google.github.io/adk-docs/)** — Comprehensive toolkit documentation
- **[A2A Samples Repository](https://github.com/google/A2A/tree/main/samples/python/common)** — Client/server code and additional examples

## 🚀 Getting Started

### Local Deployment

```bash
# Clone and run the demo locally
git clone https://github.com/kweinmeister/agentic-trading
cd agentic-trading
./deploy_local.sh
```

### Cloud Run Deployment

```bash
# Deploy to Google Cloud Run
./deploy_cloud_run.sh
```

## 📈 Next Steps & Enhancements

- Add new agents (sentiment analysis, market data feeds)
- Integrate dynamic agent discovery via Agent Cards
- Implement streaming and asynchronous task handling
- Scale with Vertex AI Agent Engine for production deployment

---

*See also: [Agent Protocols](./agent-protocols.md), [Agent Communication](./agent-communication.md), [ADK to A2A Integration Guide](../guides/agent-development/adk-to-a2a-guide.md)*
