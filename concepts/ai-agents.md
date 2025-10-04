# AI Agents

AI agents are autonomous systems that perceive their environment, reason, and take actions to achieve specific goals. They are foundational to modern AI, enabling automation, decision-making, and interaction with users or other systems.

---





## � Related Concepts

- **[Agent Communication](./agent-communication.md)** — Protocols and patterns for agent interaction
- **[Agent Deployment Patterns](./agent-deployment-patterns.md)** — Production deployment strategies
- **[Agent-Native Cloud Platforms](./agent-native-cloud.md)** — Specialized cloud platforms for agent deployment
- **[MCP (Model Context Protocol)](./mcp.md)** — Standard for agent tool connectivity
- **[Stateless Agent Design](./stateless-agent-design.md)** — Scalable architecture patterns
- **[Human-in-the-Loop](./human-in-the-loop.md)** — Human oversight in agent systems
- **[Production Deployment](./production-deployment.md)** — Deployment strategies and patterns
- **[Tool Use](./tool-use.md)** — External tool integration patterns
- **[Context Management](./context-management.md)** — Information flow management

---


## 🛠️ Key Frameworks & Tools

- [Google ADK (Agent Development Kit)](https://google.github.io/adk-docs/) — Production-ready, multi-agent, model-agnostic
- [Quantalogic](https://github.com/quantalogic/quantalogic) — Advanced planning and orchestration
- [CrewAI](https://github.com/joaomdmoura/crewAI) — Multi-agent collaboration
- [Pydantic AI](https://ai.pydantic.dev/agents/) — Type-safe agent development
- [AutoGen](https://microsoft.github.io/autogen/) — Conversational multi-agent framework
- [MemGPT](https://memgpt.ai/) — Long-term memory for agents
- [Open Interpreter](https://github.com/KillianLucas/open-interpreter/) — Natural language computer interface
- [Trae Agent](https://github.com/bytedance/trae-agent) — Open-source, modular LLM agent for software engineering. Multi-LLM support (OpenAI, Anthropic, Gemini, etc.), rich tool ecosystem, CLI, and research-friendly design. Ideal for agentic coding and workflow automation.
- [Qwen Code](./qwen-code.md) — Command-line agentic coding tool for Qwen3-Coder and Gemini CLI workflows
- [Crush](./crush.md) — Multi-model, extensible, open-source AI coding agent for your terminal. Supports LLMs, MCP, LSP, and custom workflows.
- [Eigent](./eigent.md) — Multi-agent workforce desktop platform. 100% open-source, privacy-first, supports MCP, human-in-the-loop, and enterprise features. See [concept page](./eigent.md).
- [Motia](./motia.md) — Unified backend framework for APIs, jobs, and agentic workflows. Polyglot, event-driven, open-source, supports TypeScript, Python, and more. Built-in state management, observability, and automation.
- [Agent Development Kit (ADK) & MCP Toolbox](https://google.github.io/adk-docs/tools/) — Advanced agentic assistant framework supporting function tools, built-in tools, third-party integrations (LangChain, StackOverflow, Google Search), and MCP protocol for secure, scalable orchestration. See [Software Bug Assistant sample](https://github.com/google/adk-samples/tree/main/python/agents/software-bug-assistant) and [Travel Agent Codelab](https://codelabs.developers.google.com/travel-agent-mcp-toolbox-adk#0) for real-world deployments. Learn how to [deploy MCP servers to Cloud Run](https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-google-cloud-run-in-under-10-minutes).
- [VideoSDK AI Agents](https://github.com/videosdk-live/agents) — Open-source Python framework for real-time multimodal conversational AI agents. Supports voice/video, SIP telephony, avatars, multi-model pipelines, MCP & A2A protocol integration, and extensible function tools. See [Documentation](https://docs.videosdk.live/ai_agents/introduction) and [Examples](https://github.com/videosdk-live/agents/blob/main/examples).
- [Arrakis](https://github.com/abshkbh/arrakis) — Secure sandboxing platform for AI agents with MicroVM isolation, snapshot-and-restore capabilities for backtracking, and MCP server support. Enables safe code execution and computer use in multi-step agent workflows.

---


## 🧠 Core Concepts

- **Agent Architectures:** [See patterns](../reference/techniques/dessign_patterns_for_llm_applications/README.md#agent-patterns), [Agent Architecture Guide](../guides/ai-agents.md#🏗️-agent-architecture-patterns)
- **Goal-Oriented Behavior:** [Planning-based agents](../guides/ai-agents.md#2-planning-based-agents)
- **Memory & Context:** [ContextFlow framework](../reference/technical-articles/2025-06-29-context-management-llm-agents.md), [MemGPT](https://memgpt.ai/)
- **Communication Protocols:** [A2A Protocol](https://github.com/google/A2A/), [MCP](https://modelcontextprotocol.io/), [Agent Communication](../reference/2025-ai-updates.md#1-agent-communication-revolution)
- **Practical Frameworks:** [VideoSDK AI Agents](https://github.com/videosdk-live/agents) — Real-time multimodal agent framework with protocol integration (MCP, A2A), extensible tools, and production-ready voice/video capabilities. See [Documentation](https://docs.videosdk.live/ai_agents/introduction).
- **Use Cases:** [Chatbots](../reference/techniques/dessign_patterns_for_llm_applications/README.md#chatbot-agent), [Automation](../guides/ai-agents.md#build-ai-apps), [Orchestration](../guides/ai-agents.md#multi-agent-orchestration)
- **AI Consciousness & Desire:** [The Consciousness Question: When AI Systems Start Wanting Things](../personal/reflexions/2025-07-10-ai-and-desire.md)

---

## 🚀 Best Practices & Next Steps

- Start with [AI Agents Guide](../guides/ai-agents.md)
- Follow [Agent SOP](../guides/agent-development/sop_ai_agent.md) for robust development
- Explore [production deployment](../guides/deployment.md)
- See [Learning Pathways](../learning/README.md#developer-path) for skill progression

[Back to Concepts Hub](./README.md)
