# Google ADK (Agent Development Kit)

Google ADK (Agent Development Kit) is a flexible, modular framework for building and deploying AI agents. Optimized for Gemini and the Google ecosystem, it is model-agnostic and supports multi-agent architectures, tool integration, and production deployment.

---

**[Google ADK Crash Course (GitHub)](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course)** — *Comprehensive, hands-on tutorial series for learning Google ADK from basics to advanced agentic workflows. Includes code, step-by-step guides, and real-world use cases.*

**[Official Documentation](https://google.github.io/adk-docs/)** — *Reference docs, API, and deployment guides.*

**[Gemini API Reference](https://ai.google.dev/docs)** — *API docs for Gemini models, including text, image, and video generation.*

**[Google AI Studio](https://aistudio.google.com/)** — *Platform for building and testing with Gemini and ADK.*

**[Pydantic Documentation](https://docs.pydantic.dev/)** — *Used for type-safe, structured outputs in ADK agents.*

---

## 🧩 Key Features

- **Flexible Orchestration**: Define agent workflows (sequential, parallel, loop, LLM-driven)
- **Multi-Agent Architecture**: Compose modular, specialized agents
- **Rich Tool Ecosystem**: Built-in, custom, and 3rd-party tool integration (LangChain, CrewAI, MCP, etc.)
- **Deployment Ready**: Containerize and deploy anywhere (local, GKE, Vertex AI, Cloud Run)
- **Built-in Evaluation**: Systematic agent performance assessment
- **Safety & Security**: Patterns for trustworthy, safe agents

## 🚀 Learning Path & Tutorials

- [Starter Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/ai_agent_framework_crash_course/google_adk_crash_course/1_starter_agent/README.md) — Basic agent creation
- [Model-Agnostic Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/ai_agent_framework_crash_course/google_adk_crash_course/2_model_agnostic_agent/README.md) — OpenAI, Claude, Gemini integration
- [Structured Output Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/ai_agent_framework_crash_course/google_adk_crash_course/3_structured_output_agent/README.md) — Type-safe, Pydantic-based responses
- [Tool-Using Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/README.md) — Built-in, function, 3rd-party, and MCP tools
- [Memory Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/ai_agent_framework_crash_course/google_adk_crash_course/5_memory_agent/README.md) — In-memory and persistent session management
- [Callbacks](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/ai_agent_framework_crash_course/google_adk_crash_course/6_callbacks/README.md) — Agent lifecycle and tool execution monitoring
- [Plugins](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/ai_agent_framework_crash_course/google_adk_crash_course/7_plugins/README.md) — Cross-cutting concerns, analytics, error handling
- [Simple Multi-Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/ai_agent_framework_crash_course/google_adk_crash_course/8_simple_multi_agent/README.md) — Multi-agent orchestration
- [Multi-Agent Patterns](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/ai_agent_framework_crash_course/google_adk_crash_course/9_multi_agent_patterns/README.md) — Sequential, loop, and parallel agent workflows

---

## 🛠️ Prerequisites

- Python 3.11+
- Google AI API Key ([Google AI Studio](https://aistudio.google.com/))
- Basic Python and API knowledge



## 📦 Additional Resources

- [Sample Agents](https://github.com/google/adk-samples)
- [ADK Python SDK](https://github.com/google/adk-python)
- [ADK Java SDK](https://github.com/google/adk-java)
- [CopilotKit ADK Integration](./adk-ag-ui-integration.md)
- [ADK + MCP Integration](./adk-mcp-gke-shopping-assistant.md)
- [Google A2A and ADK Multi-Agent Architecture](./google-a2a-adk-multi-agent.md)


---

*See also: [AI Agents](./ai-agents.md), [Agent Protocols](./agent-protocols.md), [MCP (Model Context Protocol)](./mcp.md), [AG-UI](./ag-ui.md)*

Last updated: 2025-10-06
