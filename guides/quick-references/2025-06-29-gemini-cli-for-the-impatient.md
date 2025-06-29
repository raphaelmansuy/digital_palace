# Google Gemini CLI for the Impatient

> Get started with Google's official AI command-line workflow tool in minutes

## 🚀 **Quick Start**

**Install & Run** (Node.js 18+ required):
```bash
# Option 1: Direct execution
npx https://github.com/google-gemini/gemini-cli

# Option 2: Global installation
npm install -g @google/gemini-cli
gemini
```

**First Time Setup:**
1. Choose a color theme
2. Sign in with personal Google account
3. Get 60 requests/minute, 1000/day free

## ⚡ **Essential Commands**

**Start Interactive Session:**
```bash
cd your-project/
gemini
```

**Common Use Cases:**
```bash
# Explore new codebase
> Describe the main pieces of this system's architecture

# Code analysis & improvement  
> Help me migrate this codebase to the latest version of Java

# Generate new features
> Implement a first draft for GitHub issue #123

# System automation
> Convert all images in this directory to PNG with date-based names
```

## 🌟 **Key Features**

- **1M Token Context** - Analyze massive codebases
- **Multimodal Support** - Work with PDFs, images, code  
- **MCP Server Integration** - Connect external tools
- **Google Search Integration** - Ground queries with real-time data
- **File System Operations** - Direct file manipulation
- **Git Integration** - Analyze repository history

## 🔧 **Advanced Configuration**

**Use API Key for Higher Limits:**
```bash
export GEMINI_API_KEY="your_key_from_ai_studio"
```

**Generate API Key:** [Google AI Studio](https://aistudio.google.com/apikey)

## 📚 **Popular Workflows**

**New Project Setup:**
```bash
cd new-project/
gemini
> Write me a Discord bot that answers questions using FAQ.md
```

**Codebase Analysis:**
```bash
git clone https://github.com/some/repository
cd repository  
gemini
> Give me a summary of all changes from yesterday
```

**System Integration:**
```bash
> Make a slide deck from git history of last 7 days
> Organize my PDF invoices by month of expenditure
```

## 🛠️ **Troubleshooting**

**Common Issues:**
- **Authentication**: Use personal Google account, not workspace
- **Node.js Version**: Ensure 18+ installed
- **Rate Limits**: Get API key for higher usage

**Documentation:**
- [Full Documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/index.md)
- [CLI Commands](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/commands.md)  
- [Troubleshooting Guide](https://github.com/google-gemini/gemini-cli/blob/main/docs/troubleshooting.md)

## 🔗 **Related Tools**

- **Alternative CLIs:** [llm](https://llm.datasette.io/), [QLLM](https://github.com/quantalogic/qllm)
- **IDE Integration:** [Cursor](https://cursor.sh/), [GitHub Copilot](https://github.com/features/copilot)
- **Agent Frameworks:** [LangChain](https://langchain.com/), [CrewAI](https://github.com/joaomdmoura/crewAI)

---

**⭐ GitHub Stats:** 41.4k stars, 3.3k forks, active development  
**📝 License:** Apache-2.0  
**🏢 Maintainer:** Google Gemini Team

*Updated: June 2025 | Part of the [Digital Palace](../../README.md) AI Knowledge Repository*
