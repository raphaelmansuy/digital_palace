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

### ✅ Best Practices

- **Use scratchpads and memory** for long tasks and cross-session persistence
- **Apply RAG and semantic search** for relevant retrieval from large knowledge bases
- **Implement hierarchical summarization** for long-running agent trajectories
- **Use state objects** to isolate context and provide fine-grained control
- **Apply tool selection via RAG** when working with large tool collections (3x accuracy improvement)

### ⚠️ Common Pitfalls

- **Context Poisoning**: When hallucinations contaminate the context window
- **Context Distraction**: When excessive context overwhelms the model's training
- **Context Confusion**: When superfluous information influences responses inappropriately
- **Context Clash**: When different parts of the context contradict each other
- **Memory Selection Issues**: Unwanted or irrelevant memories being retrieved automatically

### 🔧 Advanced Techniques (2025)

- **Provence (ICLR 2025)**: State-of-the-art trained context pruners for Question-Answering tasks with dynamic pruning detection
- **MELODI (Google DeepMind)**: Advanced memory compression techniques for long contexts in transformer architectures
- **Auto-compact**: Automatic summarization when approaching context limits (e.g., Claude Code at 95%)
- **Knowledge Graphs**: Enhanced memory indexing using graph-based relationships for better context selection
- **Multi-modal Context**: Managing context across text, images, audio, and video in unified frameworks
- **Sandbox Isolation**: Using environments like E2B for token-heavy object storage and context isolation
- **Hierarchical Summarization**: Multi-level context compression for long-running agent workflows
- **CodeAgent Patterns**: Context isolation through executable code environments (HuggingFace Deep Research approach)
- **State Object Design**: Fine-grained context control through structured state schemas
- **Context Quarantine**: Isolating potentially problematic context segments for validation
- **Dynamic Tool Loading**: Just-in-time tool selection based on task requirements
- **Recursive Summarization**: Multi-pass summarization for complex agent trajectories
- **Embedding-based Memory**: Semantic memory storage and retrieval using vector databases

### 🐛 Debugging & Troubleshooting

- **Context Overflow Detection**: Monitoring for approaching context limits
- **Hallucination Tracking**: Identifying and preventing context poisoning
- **Memory Leak Prevention**: Cleaning up unused context and memory references
- **Context Validation**: Ensuring context coherence and consistency
- **Performance Profiling**: Analyzing context engineering impact on speed and cost
- **Multi-Agent Coordination**: Debugging context hand-offs between agents
- **Tool Selection Debugging**: Analyzing why specific tools are or aren't selected
- **Context Visualization**: Tools for visualizing context flow and usage patterns
- **A/B Testing**: Comparing different context engineering strategies

---

## 📚 Further Reading & Examples

### 🎯 Real-World Applications

- **[SkyReels-V2: Infinite-Length Film Generative Model](./skyreels-v2.md)** — Example of context engineering in long-form, controllable video generation using autoregressive diffusion forcing.
- **[ChatGPT Memory](https://help.openai.com/en/articles/8590148-memory-faq)** — Auto-generated long-term memories that persist across sessions
- **[Cursor Rules](https://docs.cursor.com/context/rules)** & **[Windsurf](https://docs.windsurf.com/windsurf/cascade/memories)** — Context management in code editors
- **[Anthropic's Multi-Agent Research System](https://www.anthropic.com/engineering/built-multi-agent-research-system)** — Context isolation across hundreds of agent turns
- **[Claude Code Auto-Compact](https://docs.anthropic.com/en/docs/claude-code/costs)** — Real-world context compression at 95% context window utilization
- **[Anthropic's Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)** — Practical patterns for agent context management
- **[Cognition AI's SWE-bench Agent](https://www.anthropic.com/research/swe-bench-sonnet)** — Context engineering for autonomous code generation and debugging
- **[HuggingFace Deep Research](https://huggingface.co/blog/open-deep-research)** — Context isolation using CodeAgent patterns and sandboxes
- **[LangChain's Open Deep Research](https://github.com/langchain-ai/open_deep_research)** — Open-source multi-agent research system with context engineering
- **[Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)** — Tool selection evaluation showing context confusion challenges


### 📖 Foundational Articles (2025)
- **[Provence: Efficient and Robust Context Pruning for RAG (ICLR 2025)](https://arxiv.org/abs/2501.16214)** — Breakthrough research on dynamic context pruning with sequence labeling and unified reranking capabilities.

### 💬 External Insights
- **[Notes on Context Engineering with Walden Yan](./walden-yan-context-engineering.md)** - Key principles from a discussion with Walden Yan.

### 🗣️ Key Endorsements

- **[Karpathy on "Context Engineering" (X, 2025)](https://x.com/karpathy/status/1937902205765607626)** — Key endorsement and amplification of the term by Andrej Karpathy.
- **[Tobi Lutke (Shopify CEO) on Context Engineering](https://twitter.com/tobi/status/1935533422589399127)** — "It describes the core skill better: the art of providing all the context for the task to be plausibly solvable by the LLM."

### 🛠️ Technical Resources

**[Context Engineering: A First-Principles Handbook (davidkimai)](https://github.com/davidkimai/Context-Engineering)** — Comprehensive, frontier handbook for moving beyond prompt engineering to context design, orchestration, and optimization. Features progressive learning from atomic prompts to neural field theory, with hands-on tutorials, reusable templates, and research evidence from top institutions.
**[Announcing Vertex AI Agent Engine Memory Bank (Google Cloud Blog)](https://cloud.google.com/blog/products/ai-machine-learning/vertex-ai-memory-bank-in-public-preview)** — Official announcement and deep dive on Vertex AI's managed Memory Bank service for agents. Explains persistent, contextual, and personalized memory for conversational agents, with guides, diagrams, and integration examples for ADK, LangGraph, and CrewAI.
- **[Context Engineering Tutorial (GitHub)](https://github.com/raphaelmansuy/tutorials/blob/main/32_context_engineering/README.md)** — Step-by-step tutorial on context engineering concepts and implementation patterns.
- **[Context Engineering Data Model (GitHub)](https://github.com/raphaelmansuy/tutorials/blob/main/35_context_engineering_context_datamodel.md)** — Data modeling for context management in agentic systems.
**[Context Engineering: A First-Principles Handbook (davidkimai)](https://github.com/davidkimai/Context-Engineering)** — Comprehensive, frontier handbook for moving beyond prompt engineering to context design, orchestration, and optimization. Features progressive learning from atomic prompts to neural field theory, with hands-on tutorials, reusable templates, and research evidence from top institutions.
**[Announcing Vertex AI Agent Engine Memory Bank (Google Cloud Blog)](https://cloud.google.com/blog/products/ai-machine-learning/vertex-ai-memory-bank-in-public-preview)** — Official announcement and deep dive on Vertex AI's managed Memory Bank service for agents. Explains persistent, contextual, and personalized memory for conversational agents, with guides, diagrams, and integration examples for ADK, LangGraph, and CrewAI.
- **[LangGraph BigTool](https://github.com/langchain-ai/langgraph-bigtool)** — Tool selection using semantic search over tool descriptions.
- **[Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)** — Benchmarking tool-use performance with context engineering insights.
- **[LangMem: Memory Management for Agents](https://github.com/langchain-ai/langmem)** — Memory management utilities for long-term context storage.
- **[E2B Sandbox](https://e2b.dev/)** — Code execution environments for context isolation.
- **[OpenAI Swarm](https://github.com/openai/swarm)** — Multi-agent framework for context separation and isolation.
- **[Anthropic's Claude Think Tool](https://www.anthropic.com/engineering/claude-think-tool)** — Scratchpad implementation for context persistence.
- **[MCP (Model Context Protocol)](https://github.com/modelcontextprotocol/servers)** — Standardized protocol for connecting tools to language models.
- **[MELODI Research Paper](https://arxiv.org/abs/2410.03156)** — Technical implementation details for hierarchical memory compression.
- **[Provence Context Pruning](https://arxiv.org/abs/2501.16214)** — Sequence labeling approach for robust context pruning in RAG systems.

### 📊 Industry Impact & Statistics (2025)

- **Cognition AI**: "Context engineering is effectively the #1 job of engineers building AI agents"
- **Anthropic**: Multi-agent systems can use up to **15× more tokens** than single-agent chat
- **Tool Selection**: RAG-based tool selection improves accuracy by **3-fold** in large tool collections
- **Context Window Usage**: Claude Code auto-compacts at **95%** context window utilization
- **Memory Systems**: ChatGPT, Cursor, and Windsurf all implement auto-generated long-term memories
- **OpenAI o3/o4**: New reasoning models with advanced context management for multi-step problem solving
- **LangGraph Platform**: Now generally available for deploying context-aware agents at scale
- **Google DeepMind MELODI**: Breakthrough memory compression reducing context size by up to **80%** while maintaining performance
- **Berkeley Function-Calling Leaderboard**: All models perform worse with multiple tools, highlighting context confusion challenges
- **Distraction Ceiling**: Models start misbehaving around 32k tokens (Llama 3.1 405B) due to context distraction
- **Context Clash Impact**: Sharded prompts cause average performance drop of **39%** across models
- **Production Deployment**: Context engineering reduces agent hallucination rates by **60%** in production systems

### 🔬 Evaluation & Metrics

- **Token Efficiency**: Measuring tokens per successful task completion
- **Context Window Utilization**: Tracking context usage patterns and overflow rates
- **Memory Precision/Recall**: Evaluating memory selection accuracy
- **Context Coherence**: Assessing internal consistency of assembled contexts
- **Failure Mode Analysis**: Tracking poisoning, distraction, confusion, and clash incidents
- **Multi-Turn Performance**: Measuring degradation over long agent conversations
- **Cost Optimization**: Balancing context quality with computational expense
- **Latency Impact**: Context engineering effects on response times
- **LangSmith Observability**: Using LangSmith for context engineering monitoring and evaluation

## 🌟 Latest Trends & Developments (2025)

### 🔬 Research Breakthroughs

- **[Provence (ICLR 2025)](https://arxiv.org/abs/2501.16214)**: Revolutionary context pruning that dynamically detects optimal pruning amounts using sequence labeling approach
- **[MELODI (Google DeepMind)](https://deepmind.google/research/publications/121073/)**: Memory compression achieving 80% context reduction with minimal performance loss ([arXiv:2410.03156](https://arxiv.org/abs/2410.03156))
- **[Sequence Labeling for Context](https://arxiv.org/abs/2507.01414)**: New paradigm treating context management as a sequence labeling problem for in-context learning

### 🏢 Industry Adoption

- **OpenAI o3/o4 Models**: Next-generation reasoning models with sophisticated context engineering
- **LangGraph Platform GA**: Production-ready infrastructure for context-aware agent deployment
- **HuggingFace Deep Research**: CodeAgent patterns for context isolation through executable environments
- **Microsoft Research**: Advanced multimodal context management for enterprise applications

### 🛠️ Tool Evolution

- **Training Cluster as a Service**: NVIDIA collaboration for large-scale context engineering research
- **Sparse Embedding Models**: New Sentence Transformers v5 with improved context selection
- **Agentic Workflows**: Enhanced context management in robotics and autonomous systems

### 📈 Performance Metrics (Latest Data)

- **Context Compression**: Up to **80% reduction** with MELODI while maintaining accuracy
- **Pruning Efficiency**: Provence enables **negligible performance drop** across diverse domains
- **Multi-Agent Scaling**: Anthropic reports **15× token usage** but improved task completion rates
- **Production Deployment**: LangGraph Platform supports **hundreds of agent turns** with efficient context management

### 🏭 Enterprise & Production Considerations

- **Cost Management**: Context engineering strategies for optimizing token usage (e.g., Claude Code auto-compact at 95%)
- **Observability**: LangSmith integration for context monitoring and tracing across agent workflows
- **Security**: Context isolation patterns for sensitive data handling in enterprise environments
- **Compliance**: GDPR/CCPA considerations for context storage and memory management
- **Scalability**: Rainbow deployments for updating context-aware agent systems without disruption
- **Error Handling**: Graceful degradation strategies when context windows are exceeded
- **Multi-Tenant**: Context isolation strategies for SaaS applications with multiple customers
- **Latency Optimization**: Balancing context richness with response speed requirements

---

## 🎯 Why "Context Engineering" vs "Prompt Engineering"

The shift from "prompt engineering" to "context engineering" reflects the evolution of the field:

- **Prompt Engineering**: Associated with simple task descriptions for day-to-day LLM use
- **Context Engineering**: Captures the industrial-strength complexity of managing context windows
- **Scope**: Context engineering encompasses prompts, memories, few-shot examples, RAG, multimodal data, tools, state, and history management
- **Complexity**: Requires both science (systematic approaches) and art (intuitive understanding of LLM psychology)

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." — Andrej Karpathy

---

> _This page is a living document. Suggestions and contributions are welcome!_
