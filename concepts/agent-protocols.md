# Agent Protocols



Agent protocols are standardized communication frameworks that enable AI agents to interact, collaborate, and coordinate effectively. These protocols define how agents exchange information, negotiate tasks, and maintain consistency across multi-agent systems.

---


**[Quickstart: Build an agent with the Agent Development Kit – Google Cloud Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-development-kit/quickstart)** 📝 — *Step-by-step official guide to building your first agent using Google’s Agent Development Kit (ADK). Covers project setup, ADK installation, agent creation, and testing in both web and CLI environments. Ideal for developers seeking a practical, hands-on introduction to agent development workflows on Vertex AI.*



**[Topic-based Memory for Long-term Conversational Agents (arXiv, 2024)](https://arxiv.org/pdf/2503.08026)** 🧑‍� — *The foundational research behind Vertex AI Memory Bank. Proposes a topic-based approach for extracting, storing, and retrieving persistent memories in conversational agents, enabling more natural, context-aware, and personalized AI interactions.*



**[A guide to Google ADK and MCP integration with an external server – Google Cloud Blog](https://cloud.google.com/blog/topics/developers-practitioners/use-google-adk-and-mcp-with-an-external-server)** 📝 — *Comprehensive walkthrough for connecting Google ADK agents to external Model Context Protocol (MCP) servers. Explains real-time communication using Server-Sent Events (SSE) and the new Streamable HTTP protocol, with practical code examples and security considerations. Essential for developers building robust, interoperable multi-agent systems that leverage external tools and data.*

**[How to build a simple multi-agentic system using Google’s ADK – Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/build-multi-agentic-systems-using-google-adk)** 📝 — *Step-by-step tutorial for building robust multi-agent workflows with ADK. Covers agent specialization, orchestration, parallel execution, and feedback loops. Ideal for practical multi-agent system design.*

---

---









- **[How to build a simple multi-agentic system using Google’s ADK – Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/build-multi-agentic-systems-using-google-adk)** 📝 — *Step-by-step tutorial for building robust multi-agent workflows with ADK. Covers agent specialization, orchestration, parallel execution, and feedback loops. Ideal for practical multi-agent system design.*

---

## 🛠️ Key Protocols & Tools

- [A2A Protocol](https://github.com/google/A2A/) — Google's agent-to-agent communication standard
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — AI application interfaces
- **[AG-UI Protocol](./ag-ui.md#ag-ui-cli-rapid-agent-interface-development)** 🆕 — Agent-user interaction protocol with create-ag-ui-app CLI for LangGraph integration
- [Microsandbox](https://github.com/microsandbox/microsandbox) — Secure, MCP-ready sandboxing for agent code execution (Python, JS, Rust, C, more). Open source, production-grade.
- [AutoGen](https://microsoft.github.io/autogen/) — Conversational multi-agent framework
- [CAMEL](../reference/techniques/camel/README.md) — Communicative agents for role-playing
- [CrewAI](https://github.com/joaomdmoura/crewAI) — Multi-agent collaboration platform

---

## 🧠 Core Concepts

- **Communication Standards:** [Agent Communication](./agent-communication.md), [MCP](./mcp.md)
- **Multi-Agent Systems:** [AI Agents](./ai-agents.md), [AutoGen Framework](../reference/techniques/autogen/README.md)
- **Protocol Design:** [A2A Protocol](https://github.com/google/A2A/), [2025 AI Updates](../reference/2025-ai-updates.md#agent-communication-protocols)
- **Orchestration:** [Agent Architecture Patterns](../guides/ai-agents.md#agent-architecture-patterns)

---

## 🚀 Best Practices & Next Steps

- Start with [Agent Communication Revolution](../reference/2025-ai-updates.md#1-agent-communication-revolution)
- Explore [A2A Protocol](https://github.com/google/A2A/) and [MCP](./mcp.md)
- See [AI Agents](./ai-agents.md) for implementation patterns
- Follow [Agent Development SOP](../guides/agent-development/sop_ai_agent.md)

[Back to Concepts Hub](./README.md)
