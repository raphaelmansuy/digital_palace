# Context Engineering for Agents

Context engineering is the art and science of managing what information is included in the context window of large language models (LLMs) and AI agents at each step of their operation. As LLMs become more capable and agents more autonomous, effective context engineering is essential for performance, cost, and reliability.

---

## 🧠 Why Context Engineering Matters

- LLMs have limited context windows (like RAM for a CPU)
- Agents must decide what information to include, persist, or retrieve at each step
- Poor context management leads to degraded performance, hallucinations, or excessive costs

---

## 🚦 Core Strategies

### 1. Write Context
- Persist information outside the context window (e.g., scratchpads, memory systems)
- Enables agents to remember plans, facts, or feedback across steps or sessions

### 2. Select Context
- Retrieve and inject only the most relevant information into the context window
- Uses embeddings, knowledge graphs, or heuristics for selection

### 3. Compress Context
- Summarize or trim context to fit within window limits
- Techniques include LLM-based summarization, pruning, or hierarchical compression

### 4. Isolate Context
- Split context across sub-agents or environments
- Reduces token usage and enables parallelism or specialization

---

## ⚡ Practical Patterns & Pitfalls
- Use scratchpads and memory for long tasks
- Apply RAG and semantic search for relevant retrieval
- Summarize or prune aggressively for long-running agents
- Beware of context poisoning, distraction, confusion, and clash

---


## 📚 Further Reading & Resources

- **[Context Engineering for Agents (Lance Martin, 2025)](https://rlancemartin.github.io/2025/06/23/context_engineering/)** — In-depth guide to context engineering strategies for LLM agents: writing, selecting, compressing, and isolating context. Covers practical patterns, pitfalls, and state-of-the-art research.
- **[Context Engineering Tutorial (GitHub)](https://github.com/raphaelmansuy/tutorials/blob/main/32_context_engineering/README.md)** — Step-by-step tutorial on context engineering concepts and implementation patterns.
- **[Context Engineering Data Model (GitHub)](https://github.com/raphaelmansuy/tutorials/blob/main/35_context_engineering_context_datamodel.md)** — Data modeling for context management in agentic systems.
- [Context Management](./context-management.md) — Related strategies and frameworks
- [AI Agents](./ai-agents.md) — Memory and context in agent architectures
- [RAG (Retrieval-Augmented Generation)](./rag.md) — Retrieval techniques for context selection

---

> _This page is a living document. Suggestions and contributions are welcome!_
