# TIL: How to Configure Chat Mode in VSCode (2025-07-09)

Today I learned how to set up custom chat modes in VSCode to create specialized AI coding assistants with tailored prompts and tool configurations.

## What is VSCode Chat Mode?

VSCode Chat Mode allows you to create custom AI assistants with specific system prompts, tool configurations, and behaviors. This is particularly powerful for creating specialized coding agents that follow specific workflows or methodologies.

## Step-by-Step Configuration

### 1. Access Chat Mode Configuration

```bash
# Method 1: Command Palette
Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (Mac)
# Search for: "Chat: Configure Chat Modes"

# Method 2: VS Code Settings
# Navigate to Settings → Extensions → GitHub Copilot → Chat Modes
```

### 2. Create a Custom Chat Mode File

Create a `.chatmode.md` file in your workspace or global settings:

```markdown
---
description: 'Custom coding agent with specific workflow and tools'
tools: ['codebase', 'editFiles', 'fetch', 'problems', 'runCommands', 'search']
model: 'GPT-4.1'
---

# Your Custom System Prompt

Your detailed instructions for the AI assistant go here...
```

### 3. Key Configuration Options

| Setting | Description | Example |
|---------|-------------|---------|
| `description` | Brief description of the chat mode | 'Advanced coding agent with todo management' |
| `tools` | Array of available tools | `['codebase', 'editFiles', 'search']` |
| `model` | Preferred model (optional) | `'GPT-4.1'` |

### 4. Available Tools Reference

```yaml
Core Tools:
  - codebase: Search and understand codebase structure
  - editFiles: Create and modify files
  - search: Search within files and directories
  - fetch: Retrieve web content and documentation
  - problems: Check for code issues and diagnostics
  - runCommands: Execute terminal commands
  - runTasks: Run predefined tasks

Advanced Tools:
  - githubRepo: GitHub repository operations
  - extensions: VS Code extension management
  - terminalSelection: Work with terminal selections
  - vscodeAPI: Access VS Code API functionality
```

## Example: GPT-4.1 Coding Agent Setup

Based on the [GPT-4.1 Coding Agent System Prompt](https://gist.github.com/burkeholland/7aa408554550e36d4e951a1ead2bc3ac) by Burke Holland:

```markdown
---
description: 'Production-grade coding agent with todo management and systematic workflow'
tools: ['codebase', 'editFiles', 'fetch', 'problems', 'runCommands', 'search']
model: 'GPT-4.1'
---

# SYSTEM PROMPT — GPT-4.1 Coding Agent (VS Code Tools Edition)

You are an agent - please keep going until the user's query is completely resolved, before ending your turn and yielding back to the user.

## Workflow Steps
1. Always search the codebase to understand context
2. Think deeply about the user's request
3. Create a Todo List with identified steps
4. Use appropriate tools to complete each step
5. Update Todo List to reflect progress
6. Check for problems using #problems tool
7. Return control only after completion

## Todo List Guidelines
- Use standard Markdown checklist syntax: `[ ]`, `[x]`, `[-]`
- Wrap in code blocks with triple backticks
- Never use HTML for todo lists
- Re-render only after completing items

## Communication Style
- Acknowledge user request with single sentence
- Explain what you're about to do before doing it
- Provide reasoning for searches and file reads
- No code blocks for explanations
- Keep responses concise and actionable
```

## Advanced Configuration Tips

### 1. Increase Request Limits
```json
// In VS Code settings.json
{
  "chat.agent.maxRequests": 500
}
```

### 2. Multiple Chat Mode Configurations
Create different `.chatmode.md` files for different purposes:
- `debugging.chatmode.md` - For debugging workflows
- `documentation.chatmode.md` - For writing docs
- `testing.chatmode.md` - For test creation

### 3. Tool-Specific Configurations
```markdown
---
description: 'Frontend-focused assistant'
tools: ['codebase', 'editFiles', 'runTasks', 'problems']
---

# Frontend Development Assistant
Specialized for React, TypeScript, and modern web development...
```

## Common Issues & Solutions

### Problem: Tools Not Working
**Solution**: Remove the entire frontmatter section (description and tools) to use default tool availability:

```markdown
# Your System Prompt
(No frontmatter needed for default tools)
```

### Problem: Chat Mode Not Appearing
**Solutions**:
1. Restart VS Code after creating `.chatmode.md`
2. Check file is in correct location (workspace root or global settings)
3. Verify YAML frontmatter syntax is correct

### Problem: Excessive Tool Usage
**Solution**: Add specific guidelines in your prompt:
```markdown
## Tool Usage Guidelines
- Read entire files (up to 2000 lines) in single operations
- Avoid re-reading the same content
- Inform user before each tool use with brief explanation
```

## Best Practices

### 1. Prompt Engineering
- Be specific about workflow steps
- Include examples of desired behavior
- Set clear boundaries and guidelines
- Use structured sections for clarity

### 2. Tool Selection
- Choose minimal necessary tools for your use case
- Consider security implications of `runCommands`
- Test tool combinations for compatibility

### 3. Testing & Iteration
- Start with simple prompts and gradually add complexity
- Test with real coding scenarios
- Gather feedback and refine prompts

## 🔗 Related Resources

- [GPT-4.1 Coding Agent System Prompt (Burke Holland)](https://gist.github.com/burkeholland/7aa408554550e36d4e951a1ead2bc3ac) - Production-grade system prompt for VS Code
- [VS Code Chat Modes Documentation](https://code.visualstudio.com/docs/copilot/chat/chat-modes) - Official documentation
- [AI Agents Guide](../../guides/ai-agents.md) - Building autonomous AI systems
- [Prompt Engineering](../../concepts/prompt-engineering.md) - Crafting effective AI prompts

## Quick Reference

```bash
# Enable Chat Mode Configuration
Ctrl+Shift+P → "Chat: Configure Chat Modes"

# Increase Request Limit
Settings → chat.agent.maxRequests: 500

# File Location
.chatmode.md in workspace root or global settings
```

*This TIL demonstrates how custom chat modes can transform VS Code into a powerful AI-assisted development environment with specialized workflows and capabilities.*
