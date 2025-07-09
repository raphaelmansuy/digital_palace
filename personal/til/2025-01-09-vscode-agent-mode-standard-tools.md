# TIL: Standard Tools in VSCode Agent Mode (2025-01-09)

Today I learned about the comprehensive set of built-in tools available in VSCode Agent Mode and how they enable powerful autonomous coding workflows.

## What is VSCode Agent Mode?

VSCode Agent Mode is an autonomous coding feature introduced in VS Code 1.99+ that enables Copilot to work independently, determining relevant context, making multi-file edits, and using specialized tools to complete complex tasks. Unlike other chat modes, Agent Mode operates with minimal user intervention, iterating until tasks are fully complete.

**Key Characteristics:**
- **Autonomous Operation**: Determines context and files automatically
- **Multi-step Execution**: Handles complex workflows with multiple iterations
- **Tool Integration**: Uses specialized tools for different tasks
- **Error Recovery**: Automatically fixes issues that arise during execution
- **Quality Assurance**: Built-in problem checking before completion

## Complete List of Standard Agent Mode Tools

Based on the latest VSCode documentation (December 2024), verified from official Microsoft sources and GitHub Copilot documentation, here are all the built-in tools available in Agent Mode:

### 🔧 **Core Development Tools**

| Tool | Purpose | Usage Example |
|------|---------|---------------|
| **`codebase`** | Perform semantic searches across the entire workspace | `#codebase` - Find authentication patterns |
| **`editFiles`** | Create, modify, and manage files in the workspace | Automatically invoked for code changes |
| **`search`** | Search for specific text patterns within files | `#search` - Find specific function implementations |
| **`problems`** | Check for compilation errors, linting issues, and diagnostics | Quality gates before task completion |
| **`usages`** | Find all references and usages of functions, classes, or variables | Code refactoring and impact analysis |
| **`changes`** | Get diff information for modified files | Review pending changes |
| **`selection`** | Work with currently selected text in editor | Context for specific code blocks |

### 🌐 **External Integration Tools**

| Tool | Purpose | Usage Example |
|------|---------|---------------|
| **`fetch`** | Retrieve content from web pages and APIs | `#fetch https://api.docs.example.com` |
| **`githubRepo`** | Search and reference code from GitHub repositories | `#githubRepo microsoft/vscode` |

### 🧪 **Testing & Quality Tools**

| Tool | Purpose | Usage Example |
|------|---------|---------------|
| **`findTestFiles`** | Locate test files related to source code | Find unit tests for specific modules |
| **`testFailure`** | Analyze and diagnose test failures | Debug failing test suites |
| **`runNotebooks`** | Execute Jupyter notebook cells | Data science and analysis workflows |

### ⚙️ **System & Environment Tools**

| Tool | Purpose | Usage Example |
|------|---------|---------------|
| **`runCommands`** | Execute terminal commands and scripts | Build, deploy, and system operations |
| **`runTasks`** | Execute predefined VS Code tasks from `tasks.json` | Run build, test, or custom tasks |
| **`terminalLastCommand`** | Get the output of the last terminal command | Debug command execution |
| **`terminalSelection`** | Work with selected text in the terminal | Process terminal output |

### 📁 **Workspace & Navigation Tools**

| Tool | Purpose | Usage Example |
|------|---------|---------------|
| **`searchResults`** | Work with search result data | Process search outcomes |
| **`new`** | Create new projects, files, or components | Project scaffolding |
| **`newJupyterNotebook`** | Create new Jupyter notebooks | Data science workflows |

### 🔌 **VS Code Integration Tools**

| Tool | Purpose | Usage Example |
|------|---------|---------------|
| **`extensions`** | Manage VS Code extensions | Install, configure, or query extensions |
| **`vscodeAPI`** | Access VS Code API functionality | Advanced editor operations |
| **`openSimpleBrowser`** | Open URLs in VS Code's built-in browser | Preview web applications |

## Tool Categories & Use Cases

### **🏗️ Project Setup & Scaffolding**
```bash
# Tools: new, extensions, runTasks, runCommands
"Create a new React TypeScript project with testing setup"
```

### **🔍 Code Analysis & Understanding**
```bash
# Tools: codebase, search, usages, problems
"Analyze the authentication flow in this application #codebase"
```

### **⚡ Multi-file Refactoring**
```bash
# Tools: editFiles, usages, findTestFiles, problems
"Refactor the user service to use async/await patterns"
```

### **🌐 External Integration**
```bash
# Tools: fetch, githubRepo, runCommands
"Integrate with the GitHub API using the patterns from #githubRepo octocat/Hello-World"
```

### **🧪 Testing & Quality Assurance**
```bash
# Tools: findTestFiles, testFailure, runCommands, problems
"Add comprehensive unit tests for the payment module"
```

## Tool Selection & Configuration

### **Automatic Tool Selection**
Agent Mode intelligently selects tools based on:
- **Task complexity**: Simple edits vs. complex workflows
- **Context requirements**: Local files vs. external resources
- **Quality needs**: Testing, validation, error checking
- **Integration requirements**: Terminal commands, external APIs

### **Manual Tool References**
You can explicitly reference tools in prompts:
```bash
# Direct tool invocation
"Explain the authentication flow #codebase"
"Get the latest React patterns #fetch https://react.dev/blog"
"Review code style consistency with #githubRepo airbnb/javascript"
```

### **Tool Sets Configuration**
Create custom tool groups for specific workflows:
```json
{
  "reader": {
    "tools": ["changes", "codebase", "fetch", "findTestFiles", "githubRepo", "problems", "usages"],
    "description": "Tools for code analysis and research",
    "icon": "search"
  },
  "builder": {
    "tools": ["editFiles", "runCommands", "runTasks", "new", "problems"],
    "description": "Tools for development and building",
    "icon": "tools"
  }
}
```

## Advanced Tool Features

### **🔄 Iterative Execution**
Agent Mode uses tools in sequences:
1. **`codebase`** → Understand existing code
2. **`editFiles`** → Make changes
3. **`problems`** → Check for issues
4. **`runCommands`** → Run tests
5. **`testFailure`** → Analyze failures (if any)
6. **`editFiles`** → Fix issues
7. **`problems`** → Final validation

### **🛡️ Safety & Approval**
Tools requiring approval:
- **`runCommands`**: Terminal command execution
- **`runTasks`**: VS Code task execution
- **MCP tools**: External tool integrations

**Auto-approval options:**
```json
{
  "chat.tools.autoApprove": false, // Require confirmation (default)
  "chat.agent.maxRequests": 15     // Maximum tool invocations per session
}
```

### **🔧 Extension Integration**
Tools can be extended via:
- **MCP Servers**: External tool protocols
- **VS Code Extensions**: Custom tool contributions
- **Tool Sets**: Grouped tool configurations

## Best Practices for Tool Usage

### **1. Context-First Approach**
```bash
# ✅ Good: Provide context first
"Understanding the current architecture #codebase, refactor the auth module to use OAuth"

# ❌ Less effective: Vague request
"Change the authentication"
```

### **2. Specific Tool Guidance**
```bash
# ✅ Explicit tool usage
"Compare our implementation with industry standards #githubRepo auth0/node-jsonwebtoken"

# ✅ Multi-tool workflow
"Analyze current test coverage #findTestFiles and add missing tests"
```

### **3. Quality Gates**
```bash
# ✅ Built-in quality assurance
"Refactor the API endpoints and ensure no breaking changes #problems"
```

### **4. Iterative Refinement**
```bash
# ✅ Let agent iterate
"Implement user registration with email verification and handle all edge cases"
```

## Tool Performance & Optimization

### **Request Limits**
- **Copilot Free**: 5 requests per session
- **Copilot Pro/Business**: 15 requests per session
- **Configurable**: `chat.agent.maxRequests` setting

### **Efficiency Tips**
1. **Use `#codebase` for large workspaces** instead of individual file references
2. **Combine related operations** in single prompts
3. **Enable auto-fix** with `github.copilot.chat.agent.autoFix: true`
4. **Optimize task definitions** in `tasks.json` for `runTasks` efficiency

## Configuration Settings

### **Essential Settings**
```json
{
  // Enable Agent Mode (VS Code 1.99+)
  "chat.agent.enabled": true,
  
  // Request limits
  "chat.agent.maxRequests": 15,
  
  // Auto-fix capabilities
  "github.copilot.chat.agent.autoFix": true,
  
  // Enable workspace tasks
  "github.copilot.chat.agent.runTasks": true,
  
  // Enhanced codebase search
  "github.copilot.chat.codesearch.enabled": true,
  
  // Tool approval (use carefully)
  "chat.tools.autoApprove": false
}
```

### **Enterprise Configuration**
Organizations can centrally manage:
- Tool availability and restrictions
- Auto-approval policies
- Request limits and quotas
- MCP server configurations

## Integration with MCP Servers

Agent Mode supports **Model Context Protocol (MCP)** servers for extended functionality:

### **Popular MCP Tools**
- **Database Integration**: PostgreSQL, MySQL, SQLite
- **Cloud Services**: AWS, Azure, GCP
- **Development Tools**: Docker, Kubernetes, Git
- **APIs & Services**: REST, GraphQL, external services

### **MCP Configuration**
```json
{
  "chat.mcp.discovery.enabled": true,
  "chat.extensionTools.enabled": true
}
```

## Real-World Examples

### **🚀 Full-Stack Feature Development**
```bash
"Create a user authentication system with:
- JWT-based auth
- Password reset functionality  
- Email verification
- Rate limiting
- Comprehensive tests
- API documentation"
```

**Tools Used**: `codebase`, `editFiles`, `findTestFiles`, `runCommands`, `problems`, `fetch` (for best practices)

### **🔄 Legacy Code Migration**
```bash
"Migrate this Express.js app to Fastify, maintaining all functionality and improving performance"
```

**Tools Used**: `codebase`, `usages`, `editFiles`, `findTestFiles`, `runCommands`, `problems`

### **📊 Performance Optimization**
```bash
"Analyze and optimize the database queries in this application, add proper indexing and caching"
```

**Tools Used**: `codebase`, `search`, `editFiles`, `runCommands`, `problems`

## Troubleshooting Common Issues

### **Tool Access Problems**
```bash
# If tools aren't working, check:
1. Agent Mode is enabled: chat.agent.enabled: true
2. Extension tools: chat.extensionTools.enabled: true  
3. Remove custom tool restrictions in chat mode metadata
```

### **Request Limit Exceeded**
```bash
# Increase limits or break down tasks:
"chat.agent.maxRequests": 25  // Increase limit
# Or split complex tasks into smaller ones
```

### **Tool Approval Issues**
```bash
# Configure approval settings:
"chat.tools.autoApprove": false      // Require approval (safer)
"chat.tools.autoApprove": true       // Auto-approve (convenience)
```

## 🔗 Related Resources

- [VSCode Agent Mode Documentation](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) - Official guide
- [VSCode Chat Context Management](https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context) - Context and tools reference
- [GitHub Copilot Chat Cheat Sheet](https://docs.github.com/en/copilot/using-github-copilot/github-copilot-chat-cheat-sheet) - Complete command reference
- [MCP Servers Documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) - Extending with external tools
- [GPT-4.1 Coding Agent TIL](./2025-07-09-dissecting-gpt4-coding-agent-prompt.md) - Advanced prompt engineering
- [VSCode Chat Mode Configuration TIL](./2025-07-09-vscode-chat-mode-configuration.md) - Custom chat modes

## Key Takeaways

1. **Comprehensive Toolset**: 20+ built-in tools covering development, testing, and integration
2. **Autonomous Operation**: Tools work together without manual intervention
3. **Quality Assurance**: Built-in error checking and iterative refinement
4. **Extensible Architecture**: MCP servers and extensions expand capabilities
5. **Enterprise Ready**: Centralized configuration and approval workflows
6. **Performance Optimized**: Intelligent tool selection and request management

*Agent Mode represents a paradigm shift from assisted coding to autonomous development, where AI systems can complete complex, multi-step programming tasks with minimal human oversight while maintaining quality and safety standards.*
