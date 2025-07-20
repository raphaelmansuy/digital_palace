# TIL: How to Configure Chat Mode in VSCode (2025-07-09)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Configure custom chat modes in VSCode for specialized AI coding assistants, tailored prompts, and tool configurations.**

---

## The Pain Point

VSCode's default chat modes are powerful, but customizing them for specific workflows (planning, debugging, documentation, agent mode) requires understanding configuration files, tool sets, and integration points. Many users struggle to set up specialized chat agents and manage tool permissions securely.

---

## Step-by-Step Guide

### 1. Command Palette Method (Recommended)

```bash
# Create new chat mode
Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (Mac)
# Search for: "Chat: New Mode File"

# Configure existing chat modes
Ctrl+Shift+P → "Chat: Configure Chat Modes"
```

### 2. File-Based Configuration

- Workspace chat modes: `.github/chatmodes/` or `.chatmodes/` folder
- User profile chat modes: User profile directory
- File format: `.chatmode.md` (Markdown with YAML frontmatter)

### 3. Tool Sets & MCP Server Integration

- Tool sets: User-level `.jsonc` files for reusable tool groups
- MCP servers: Configure in `.vscode/mcp.json` (workspace) or `settings.json` (user)

### 4. Example Chat Mode Files

- Planning, debugging, documentation, and agent modes with structured prompts and tool lists

### 5. Essential Settings & Commands

- Key settings in `settings.json` for agent mode, tool management, and MCP integration
- Command Palette for chat mode and tool set management

---

## Troubleshooting

- Restart VS Code after creating `.chatmode.md` files
- Check file locations and YAML syntax
- Remove frontmatter for default tool availability
- Add guidelines to prompts for tool usage boundaries

---

## Security Considerations

- Limit tool permissions (especially `runCommands`) to trusted users and environments
- Store API keys and secrets in secure input fields, not in plain text
- Audit custom chat modes for excessive tool access or risky commands
- Use workspace-level configuration for team security; restrict agent mode in production

---

## Related Resources

- [VS Code Chat Modes Documentation](https://code.visualstudio.com/docs/copilot/chat/chat-modes)
- [GPT-4.1 Coding Agent System Prompt (Burke Holland)](https://gist.github.com/burkeholland/7aa408554550e36d4e951a1ead2bc3ac)
- [AI Agents Guide](../../guides/ai-agents.md)
- [Prompt Engineering](../../concepts/prompt-engineering.md)

---

*⚡ Pro tip: Use tool sets and workspace-level `.chatmode.md` files to create robust, secure, and highly customized AI coding agents in VSCode!*
