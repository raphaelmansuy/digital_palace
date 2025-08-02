---
title: "Crush: Terminal AI Coding Agent"
description: "Multi-model, extensible, open-source AI agent for your terminal. Supports LLMs, MCP, LSP, and custom workflows."
tags: [ai-agent, cli, terminal, coding, open-source, mcp, lsp, workflow, multi-model, charmbracelet]
links:
  - label: "GitHub Repository"
    url: "https://github.com/charmbracelet/crush"
  - label: "Documentation"
    url: "https://github.com/charmbracelet/crush#readme"
  - label: "Latest Release"
    url: "https://github.com/charmbracelet/crush/releases"
  - label: "Charmbracelet Discord"
    url: "https://charm.land/discord"
---

# Crush: Terminal AI Coding Agent

Crush is a multi-model, extensible, open-source AI coding agent for your terminal. It supports a wide range of LLMs (OpenAI, Anthropic, Gemini, Groq, OpenRouter, and custom providers), lets you switch models mid-session, and maintains multiple work contexts per project. It’s extensible via MCP (Model Context Protocol) and LSPs, works on all major OSes, and is open source (MIT/FSL-1.1).

## Key Features
- **Multi-Model:** Choose from many LLMs or add your own via OpenAI/Anthropic-compatible APIs
- **Flexible:** Switch LLMs mid-session while preserving context
- **Session-Based:** Maintain multiple work sessions and contexts per project
- **LSP-Enhanced:** Use Language Server Protocols for additional context
- **Extensible:** Add capabilities via MCPs (`http`, `stdio`, `sse`)
- **Works Everywhere:** First-class support in every terminal (macOS, Linux, Windows, BSD)
- **Open Source:** MIT/FSL-1.1 license

## Installation
- **Homebrew:** `brew install charmbracelet/tap/crush`
- **NPM:** `npm install -g @charmland/crush`
- **Arch Linux:** `yay -S crush-bin`
- **Nix:** `nix run github:numtide/nix-ai-tools#crush`
- **Go:** `go install github.com/charmbracelet/crush@latest`
- **Binaries:** [Releases page](https://github.com/charmbracelet/crush/releases) for Linux, macOS, Windows, BSD

## Configuration
- JSON-based config: `crush.json` or `.crush.json` (local or global)
- Supports custom providers, LSPs, MCPs, file ignoring (`.crushignore`), tool whitelisting, and debug options
- See [README](https://github.com/charmbracelet/crush#readme) for full config examples

## Logging
- Logs stored in `./.crush/logs/crush.log` (per project)
- CLI commands: `crush logs`, `crush logs --tail 500`, `crush logs --follow`

## Community & Support
- [Charmbracelet Discord](https://charm.land/discord)
- [Twitter](https://twitter.com/charmcli)
- [Discussions](https://github.com/charmbracelet/crush/discussions)

## Related Concepts
- [Qwen Code](./qwen-code.md)
- [Workflow Automation](./workflow-automation.md)
- [Vibe Coding](./vibe-coding.md)
- [AI Agents](./ai-agents.md)
- [MCP Illustrated Guidebook](./mcp-illustrated-guidebook.md)

---

> "Your new coding bestie, now available in your favourite terminal. Your tools, your code, and your workflows, wired into your LLM of choice." — Charmbracelet

---

For more, see the [GitHub repository](https://github.com/charmbracelet/crush) and [documentation](https://github.com/charmbracelet/crush#readme).
