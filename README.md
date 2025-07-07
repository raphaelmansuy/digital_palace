# 🏛️ Digital Palace

> **Your AI Knowledge Hub** - From concepts to production in minutes, not months

[![Last Updated](https://img.shields.io/badge/Last%20Updated-June%202025-brightgreen?style=for-the-badge)](./reference/2025-ai-updates.md)
[![AI Tools](https://img.shields.io/badge/AI%20Tools-158+-blue?style=for-the-badge)](./tools/ai-tools-master-directory.md)
[![Community](https://img.shields.io/badge/Community-Join%20Us-success?style=for-the-badge&logo=users)](https://github.com/raphaelmansuy/digital_palace/discussions)

**🎯 Cut through AI complexity. Get to results faster.**  
**🆕 June 2025** - OpenAI o3, Claude 4, Computer Use & Production-Ready Agents

## 🚀 Start Here - Choose Your Path

| 🎯 **I want to...**         | ⚡ **Go to**                                                               | 🕒 **Time** | 💡 **Result**      |
| --------------------------- | -------------------------------------------------------------------------- | ----------- | ------------------ |
| **🧠 Understand AI**        | [Concepts Hub](./concepts/README.md)                                       | 15 min      | Clear foundation   |
| **👥 Meet AI Leaders**      | [People Hub](./people/README.md)                                           | 5 min       | Key figures & bios |
| **🤖 Try AI Tools**         | [Best Tools](./tools/ai-tools-master-directory.md#beginner-friendly-tools) | 30 sec      | Working AI now     |
| **💻 Build an App**         | [Zero-to-App](./guides/goal-oriented-guides.md#getting-started)            | 5 min       | Live application   |
| **📚 Learn Systematically** | [Learning Path](./learning/README.md#interactive-learning-navigator)       | 10 min      | Structured roadmap |
| **🛠️ Find Right Tool**      | [Tool Finder](./tools/ai-tools-master-directory.md#quick-tool-finder)      | 2 min       | Perfect match      |



## 🔥 What's Hot Right Now

- **[OpenAI o3 & Claude 4](./reference/2025-ai-updates.md)** - Revolutionary reasoning models
- **[Computer Use Agents](./concepts/computer-use.md)** - AI that controls your screen
- **[Voice AI Breakthrough](./concepts/voice-ai.md)** - Real-time conversation
- **[AI Legal Compliance](./concepts/ai-legal-regulatory.md)** - EU AI Act & GDPR guide
- **[Today I Learned](./personal/til/README.md)** - Daily AI discoveries & insights
- **[SkyReels-V2: Infinite-Length Video Generation](./concepts/skyreels-v2.md)** - SOTA open-source autoregressive diffusion model for long-form, high-quality video generation
- **[The State of AI Agents (June 2025) – Lance Martin](https://rlancemartin.github.io/2025/06/10/aie/)** - In-depth analysis of ambient agents, agent UX, tools, and training
- **[Vibe Coding & Benchmark (April 2025) – Lance Martin](https://rlancemartin.github.io/2025/04/03/vibe-code/)** - How context and retrieval methods shape agent coding performance

---

## 🌐 Curated Blogs & Recommended Reading

Stay ahead with these high-quality, technical blog posts and deep dives from the AI community:

- **[Context Kills VRAM: How to Run LLMs on consumer GPUs](https://medium.com/@lyx_62906/context-kills-vram-how-to-run-llms-on-consumer-gpus-a785e8035632)**  
  A practical guide to optimizing context size and memory usage for running large language models on consumer-grade GPUs. Covers real-world benchmarks, trade-offs, and actionable tips for maximizing VRAM efficiency.

- **[Training a Rust 1.5B Coder LM with Reinforcement Learning (GRPO)](https://www.oxen.ai/blog/training-a-rust-1-5b-coder-lm-with-reinforcement-learning-grpo)**  
  An in-depth look at building a 1.5B parameter code LLM in Rust, using reinforcement learning and the GRPO algorithm. Explains the training pipeline, challenges, and lessons learned for open-source code models.

- **[Getafix: How Facebook tools learn to fix bugs automatically](https://ai.facebook.com/blog/getafix-how-facebook-tools-learn-to-fix-bugs-automatically/)**  
  Facebook's Getafix system uses machine learning to suggest and apply bug fixes at scale. This post details the approach, real-world impact, and how AI is transforming software maintenance.

- **[A Visual Guide to Quantization](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization)**  
  A clear, illustrated walkthrough of quantization techniques for neural networks. Great for understanding how quantization reduces model size and speeds up inference, with visuals and code examples.


- **[Block's Playbook for Designing MCP Servers](https://engineering.block.xyz/blog/blocks-playbook-for-designing-mcp-servers)**  
  A detailed engineering guide from Block on building robust Model Context Protocol (MCP) servers. 
  
  **Key takeaways:**
  - **Design Principles:** Emphasizes modularity, statelessness, and separation of concerns for scalable MCP server architecture. See: [Agent Protocols](./concepts/agent-protocols.md), [MCP](./concepts/mcp.md)
  - **Scalability Patterns:** Async APIs, load balancing, and horizontal scaling for high-throughput. See: [Production Deployment Guide](./guides/deployment.md)
  - **Security & Observability:** Best practices for authentication, authorization, and monitoring. See: [Observability](./concepts/observability.md)
  - **Real-World Lessons:** Managing context size, optimizing latency, and supporting multiple client types. Example: Truncate or summarize old messages for long-running agent sessions.
  - **Open Source & Community:** Encourages open standards and community-driven development for MCP infrastructure.
  
  **Example (Python/FastAPI):**
  ```python
  from fastapi import FastAPI, Request
  import uvicorn

  app = FastAPI()

  @app.post("/mcp/context")
  async def handle_context(request: Request):
      data = await request.json()
      # Validate and store context
      # ...
      return {"status": "ok"}

  if __name__ == "__main__":
      uvicorn.run(app, host="0.0.0.0", port=8000)
  ```
  
  For more, see the [TIL summary](./personal/til/2025-07-07-blocks-mcp-server-playbook.md) and [Curated Blogs & Recommended Reading](#curated-blogs--recommended-reading).

For more author-centric and community blog links, see [External Blogs](./community/external-blogs/blogs.md).

## 🧩 Concepts Hub - Your Knowledge Foundation

**The core of Digital Palace** - Master AI concepts with intelligent cross-linking.

**Why Start Here?**

- **🧠 Build Understanding**: 70+ concepts from basics to cutting-edge
- **🔗 Smart Navigation**: Every concept connects to related areas
- **🛠️ Tool Integration**: Direct links to relevant tools and guides
- **⚡ Quick Reference**: Fast lookup for definitions and examples

**[🚀 Explore the Concepts Hub →](./concepts/README.md)**

---

## 🔍 **How to Search This Repository**

**Finding what you need quickly:**

1. **🔍 Use GitHub Search**: Press `/` and search across all files
2. **📁 Browse by Category**: Use the directory structure below
3. **🏷️ Filter by Tags**: Look for difficulty levels (🟢🟡🔴) and categories
4. **🔗 Follow Cross-Links**: Each section links to related materials
5. **📊 Check Popular Content**: See most-viewed resources above

**Search Tips:**

- Use specific terms: "RAG system", "LangChain setup", "production deployment"
- Look for emoji indicators: 🟢 Beginner, 🟡 Intermediate, 🔴 Advanced
- Check the "Quick Access" tables in each section
- Use browser search (Ctrl+F) within any README file
- **Browse [Curated X Accounts](./reference/curated-x-accounts.md) for top AI voices and news**

---

## 🚀 Getting Started

### Pick Your Level

#### 🌱 New to AI

**[Start Here](./learning/README.md#complete-beginner-path)** → **[Try Tools](./tools/ai-tools-master-directory.md#beginner-friendly-tools)** → **[First Project](./guides/getting-started.md)**  
_Time: 2-4 weeks → Working AI app_

#### 🔧 Can Code

**[Developer Path](./learning/README.md#developer-path)** → **[Build Apps](./guides/goal-oriented-guides.md#building-conversational-ai)** → **[Production](./guides/goal-oriented-guides.md#production-deployment)**  
_Time: 1-2 weeks → Production system_

#### 🧠 AI Expert

**[2025 Updates](./reference/2025-ai-updates.md)** → **[Cutting-Edge Tools](./tools/ai-tools-master-directory.md#2025-breakthrough-tools)** → **[Advanced Agents](./guides/goal-oriented-guides.md#ai-agents-automation)**  
_Time: Ongoing → Frontier knowledge_

### 📚 Core Resources

| Type            | Link                                              | Purpose                   |
| --------------- | ------------------------------------------------- | ------------------------- |
| **🧩 Concepts** | [Concepts Hub](./concepts/README.md)              | Knowledge foundation      |
| **� People**    | [People Hub](./people/README.md)                  | AI/ML influential figures |
| **�🛠️ Tools**   | [AI Tools](./tools/ai-tools-master-directory.md)  | Find the right tool       |
| **🎯 Guides**   | [How-To Guides](./guides/goal-oriented-guides.md) | Step-by-step tutorials    |
| **📚 Learning** | [Learning Paths](./learning/README.md)            | Structured education      |
| **💡 TIL**      | [Today I Learned](./personal/til/README.md)       | Daily discoveries         |
| **🆕 Latest**   | [2025 Updates](./reference/2025-ai-updates.md)    | Cutting-edge AI           |
| **🐦 X Accounts** | [Curated X Accounts](./reference/curated-x-accounts.md) | Top AI voices & updates   |

---

## 🏛️ Repository Architecture

This repository is organized as a **digital palace** - each section serves a specific purpose in your AI learning journey:

### 📁 **Core Directories**

```text
digital_palace/
├── 🧩 concepts/          # **CORE: Master concept index with cross-links**
├── � people/            # AI/ML influential figures & leaders
├── �📖 learning/           # Structured learning paths & courses
│   └── courses/          # Educational resources
├── 🎯 guides/            # Step-by-step implementation guides
│   ├── prompting/        # Prompting techniques
│   ├── quick-references/ # "For the Impatients" series
│   ├── image-generation/ # AI image guides
│   ├── agent-development/# AI agent SOPs
│   └── training/         # Training resources
├── 🛠️ tools/             # Curated tool directories & comparisons
│   └── development-tools/# VS Code extensions
├── 📚 reference/         # Quick lookups, APIs, cheat sheets
│   ├── technical-articles/# Deep-dive articles
│   ├── techniques/       # AI techniques
│   ├── research-papers/  # Academic papers
│   ├── datasets/         # Training datasets
│   ├── cloud-platforms/  # Cloud guides
│   └── genai-fundamentals/# GenAI basics
├── 🎭 personal/          # Learning philosophy & mental models
│   ├── til/             # Today I Learned
│   ├── mental-models/   # Decision frameworks
│   └── ideas/           # Project concepts
└── 💬 community/         # Discussions, contributions, updates
    ├── newsletters/      # Updates
    ├── social-content/   # LinkedIn posts
    └── external-blogs/   # Blog recommendations
```

### 🎯 **Usage Philosophy**

**🌱 Learn by Doing**: Start with practical projects, understand theory as you build  
**🔄 Iterative Discovery**: Return to concepts as your understanding deepens  
**🤝 Community Growth**: Share learnings, contribute improvements, help others  
**📈 Continuous Updates**: Stay current with the rapidly evolving AI landscape

---

## 🌟 What's Inside

### 🆕 2025 Breakthroughs

- **[o3 & Claude 4](./reference/2025-ai-updates.md)** - Revolutionary reasoning models
- **[Computer Use Agents](./concepts/computer-use.md)** - AI that controls your screen
- **[Voice AI](./concepts/voice-ai.md)** - Real-time conversation
- **[AI Legal Compliance](./concepts/ai-legal-regulatory.md)** - EU AI Act & GDPR

### 🛠️ Tools & Frameworks

- **[158+ AI Tools](./tools/ai-tools-master-directory.md)** - Comprehensive directory
- **[Framework Comparisons](./tools/framework-comparison.md)** - LangChain vs alternatives
- **[Production Tools](./tools/ai-tools-master-directory.md#production-research-tools)** - Enterprise solutions

### 🎯 Practical Guides

- **[Zero-to-App](./guides/goal-oriented-guides.md)** - Build AI apps fast
- **[AI Agents](./guides/ai-agents.md)** - Autonomous systems
- **[RAG Systems](./guides/rag-systems.md)** - AI with your data
- **[Production Deployment](./guides/deployment.md)** - Scale to users

### 📚 Learning Resources

- **[Structured Paths](./learning/README.md)** - Beginner to expert
- **[Research Papers](./reference/research-papers.md)** - Latest findings
- **[Mental Models](./personal/mental-models/README.md)** - Think like an expert

---

## 🎯 **Quick Start Guide**

| **Goal**                     | **Best Path**                                                                        | **Time**   | **Outcome**                 |
| ---------------------------- | ------------------------------------------------------------------------------------ | ---------- | --------------------------- |
| � **Understand AI concepts** | [Concepts Hub](./concepts/README.md)                                                 | 15 minutes | Clear conceptual foundation |
| �🤖 **Try AI now**           | [ChatGPT Alternatives](./tools/ai-tools-master-directory.md#beginner-friendly-tools) | 30 seconds | Working AI demo             |
| 💻 **Build an app**          | [Zero-to-App Guide](./guides/goal-oriented-guides.md#getting-started)                | 5 minutes  | Live application            |
| 📚 **Learn systematically**  | [Learning Roadmap](./learning/README.md#find-your-learning-path)                     | 10 minutes | Structured path             |
| 🛠️ **Find tools**            | [AI Tools Directory](./tools/ai-tools-master-directory.md#quick-tool-finder)         | 2 minutes  | Perfect tool match          |

---

## 🤝 Contributing

We welcome contributions from the AI community! Here's how you can help improve this digital palace:

### 🌟 **Ways to Contribute**

- **📝 Share Knowledge**: Add new articles, tutorials, or insights
- **🛠️ Tool Reviews**: Submit reviews of AI tools you've used
- **🐛 Report Issues**: Found broken links or outdated information?
- **💡 Suggest Improvements**: Ideas for better organization or new sections
- **🔍 Fact Checking**: Help keep information accurate and current

### 📋 **Contribution Guidelines**

1. **Fork this repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-contribution`)
3. **Make your changes** following our style guide
4. **Test your changes** (check links, formatting, etc.)
5. **Commit your changes** (`git commit -m 'Add amazing contribution'`)
6. **Push to the branch** (`git push origin feature/amazing-contribution`)
7. **Open a Pull Request**

### 🎯 **High-Impact Contribution Areas**

- **2025 AI Updates**: Latest model releases, breakthrough papers
- **Tool Comparisons**: Head-to-head analysis of similar tools
- **Implementation Guides**: Step-by-step tutorials for specific use cases
- **Performance Benchmarks**: Real-world testing results
- **Case Studies**: Success/failure stories from actual implementations

---

## 📧 Connect & Support

### 🤝 **Get In Touch**

- **💼 Professional Consultation**: [LinkedIn - Raphaël MANSUY](https://www.linkedin.com/in/raphaelmansuy/)
- **🐦 Latest Updates**: [Twitter/X - @raphaelmansuy](https://twitter.com/raphaelmansuy)
- **💬 Community Discussions**: [GitHub Discussions](https://github.com/raphaelmansuy/digital_palace/discussions)
- **📧 Direct Contact**: [Email](mailto:raphael.mansuy@gmail.com)

### 🌟 **Support This Project**

- **⭐ Star this repository** if you find it valuable
- **🔄 Share** with your network and colleagues
- **💡 Contribute** your own insights and discoveries
- **📢 Spread the word** about useful resources you've found here

### 🏢 **Professional Services**

Need AI implementation for your business? Raphaël offers:

- **🎯 AI Strategy Consulting** - Roadmap and architecture planning
- **🚀 Implementation Support** - Hands-on development and deployment
- **📚 Team Training** - Upskill your developers and data teams
- **🔧 Custom Solutions** - Tailored AI applications for your specific needs

**[Schedule a consultation →](https://www.linkedin.com/in/raphaelmansuy/)**

---

**⭐ If this repository helps you, please give it a star! ⭐**

_Built with ❤️ by [Raphaël MANSUY](https://www.linkedin.com/in/raphaelmansuy/) for the AI community_
