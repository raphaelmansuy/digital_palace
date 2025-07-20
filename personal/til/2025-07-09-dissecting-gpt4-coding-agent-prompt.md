# TIL: Dissecting the GPT-4.1 Coding Agent System Prompt (2025-07-09)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Burke Holland's GPT-4.1 Coding Agent System Prompt provides a production-grade workflow for AI coding assistants in VS Code, emphasizing todo list management, tool discipline, and communication protocols.**

---

## The Pain Point

Most AI coding agents lack systematic workflows, clear progress tracking, and robust communication standards, leading to incomplete solutions and user frustration. Burke Holland's prompt solves this by enforcing a structured, transparent, and thorough approach.

---

## Step-by-Step Guide

1. Search the codebase for context before planning or acting
2. Create a detailed todo list using Markdown checklist syntax (never HTML)
3. Use tools (fetch, read, grep, problems) with explicit user communication before each use
4. Update the todo list only after completing items
5. Check for problems before returning control to the user
6. Recursively fetch web links for complete context
7. Avoid redundant operations; reuse context when possible

---

## Troubleshooting

- If tools are inaccessible, try removing YAML metadata from chat mode files
- For excessive tool usage, add guidelines to prompts
- If todo lists are verbose, only re-render after completing items
- For incomplete solutions, ensure recursive link fetching and full file reads

---

## Security Considerations

- Never expose API keys, secrets, or sensitive data in prompts or configuration files
- Limit tool permissions (especially `runCommands`) to trusted environments
- Audit system prompts for compliance and privacy risks
- Use workspace-level configuration for team security

---

## Related Resources

- [GPT-4.1 Coding Agent System Prompt (Burke Holland)](https://gist.github.com/burkeholland/7aa408554550e36d4e951a1ead2bc3ac)
- [Burke Holland GitHub Profile](https://github.com/burkeholland)
- [How to Configure Chat Mode in VSCode](2025-07-09-vscode-chat-mode-configuration.md)
- [Prompt Engineering](../../concepts/prompt-engineering.md)
- [AI Agents Guide](../../guides/ai-agents.md)

---

*⚡ Pro tip: Use Markdown todo lists and explicit tool usage guidelines for reliable, production-grade AI coding agents!*
