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

## 📁 Configuration File Locations & Setup

This section provides specific file paths and actionable examples for configuring VSCode Agent Mode tools.

### **🗂️ Configuration File Hierarchy**

VSCode loads configuration from multiple locations with the following priority:

1. **Workspace Settings** (highest priority)
2. **Folder Settings** 
3. **User Settings**
4. **Default Settings** (lowest priority)

#### **File Locations by Operating System**

**macOS:**
```bash
# User Settings
~/Library/Application Support/Code/User/settings.json

# Workspace Settings  
<workspace>/.vscode/settings.json

# Tool Sets Configuration
~/Library/Application Support/Code/User/toolsets.jsonc

# MCP Servers (Workspace)
<workspace>/.vscode/mcp.json

# Chat Modes (User)
~/Library/Application Support/Code/User/chatmodes/

# Chat Modes (Workspace)
<workspace>/.vscode/chatmodes/
<workspace>/.github/chatmodes/
```

**Windows:**
```bash
# User Settings
%APPDATA%\Code\User\settings.json

# Workspace Settings
<workspace>\.vscode\settings.json

# Tool Sets Configuration
%APPDATA%\Code\User\toolsets.jsonc

# MCP Servers (Workspace)
<workspace>\.vscode\mcp.json

# Chat Modes (User)
%APPDATA%\Code\User\chatmodes\

# Chat Modes (Workspace)
<workspace>\.vscode\chatmodes\
<workspace>\.github\chatmodes\
```

**Linux:**
```bash
# User Settings
~/.config/Code/User/settings.json

# Workspace Settings
<workspace>/.vscode/settings.json

# Tool Sets Configuration
~/.config/Code/User/toolsets.jsonc

# MCP Servers (Workspace)
<workspace>/.vscode/mcp.json

# Chat Modes (User)
~/.config/Code/User/chatmodes/

# Chat Modes (Workspace)
<workspace>/.vscode/chatmodes/
<workspace>/.github/chatmodes/
```

### **⚙️ Actionable Configuration Examples**

#### **1. User Settings Configuration**

**File:** `~/Library/Application Support/Code/User/settings.json` (macOS)

```json
{
  // Agent Mode Core Settings
  "chat.agent.enabled": true,
  "chat.agent.maxRequests": 20,
  "github.copilot.chat.agent.autoFix": true,
  "github.copilot.chat.agent.runTasks": true,
  
  // Tool Management
  "chat.extensionTools.enabled": true,
  "chat.tools.autoApprove": false,
  "chat.mcp.discovery.enabled": true,
  
  // Enhanced Features
  "github.copilot.chat.codesearch.enabled": true,
  "chat.editing.autoAcceptDelay": 3000,
  
  // MCP Global Configuration
  "mcp": {
    "servers": {
      "github-tools": {
        "type": "stdio",
        "command": "npx",
        "args": ["-y", "@github/github-mcp-server"],
        "env": {
          "GITHUB_TOKEN": "${input:github-token}"
        }
      },
      "fetch-tools": {
        "type": "stdio", 
        "command": "uvx",
        "args": ["mcp-server-fetch"]
      }
    }
  },
  
  // Input Variables for MCP
  "inputs": [
    {
      "type": "promptString",
      "id": "github-token",
      "description": "GitHub Personal Access Token",
      "password": true
    }
  ]
}
```

**How to Apply:**
1. Open Command Palette: `Cmd+Shift+P` (macOS) / `Ctrl+Shift+P` (Windows/Linux)
2. Type: "Preferences: Open User Settings (JSON)"
3. Copy the configuration above
4. Restart VSCode

#### **2. Workspace Settings Configuration**

**File:** `<your-project>/.vscode/settings.json`

```json
{
  // Project-specific Agent Mode settings
  "chat.agent.enabled": true,
  "chat.agent.maxRequests": 15,
  
  // Project-specific tool restrictions
  "chat.tools.autoApprove": false,
  
  // Disable certain tools for this project
  "chat.agent.disallowedTools": [
    "runCommands"
  ],
  
  // Allow only specific tools
  "chat.agent.allowedTools": [
    "codebase",
    "editFiles", 
    "search",
    "problems",
    "usages",
    "fetch",
    "githubRepo"
  ],
  
  // Project-specific MCP server discovery
  "chat.mcp.discovery.enabled": true,
  
  // Custom chat mode locations
  "chat.modeFilesLocations": [
    ".vscode/chatmodes",
    ".github/chatmodes"
  ]
}
```

**How to Apply:**
1. Navigate to your project root
2. Create `.vscode/` folder if it doesn't exist
3. Create or edit `settings.json` in that folder
4. Add the configuration above

#### **3. MCP Servers Configuration**

**File:** `<your-project>/.vscode/mcp.json`

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "openai-api-key",
      "description": "OpenAI API Key",
      "password": true
    },
    {
      "type": "promptString", 
      "id": "database-url",
      "description": "PostgreSQL Database URL",
      "password": true
    }
  ],
  "servers": {
    "postgres-tools": {
      "type": "stdio",
      "command": "uvx",
      "args": ["mcp-server-postgres"],
      "env": {
        "DATABASE_URL": "${input:database-url}"
      }
    },
    "file-manager": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "mcp-server-filesystem"],
      "env": {
        "ALLOWED_PATHS": "${workspaceFolder}"
      }
    },
    "aws-tools": {
      "type": "stdio",
      "command": "uvx", 
      "args": ["mcp-server-aws"],
      "env": {
        "AWS_REGION": "us-east-1"
      }
    },
    "docker-tools": {
      "type": "stdio",
      "command": "uvx",
      "args": ["mcp-server-docker"]
    }
  }
}
```

**How to Apply:**
1. Navigate to your project root
2. Create `.vscode/` folder if it doesn't exist
3. Create `mcp.json` with the configuration above
4. Install required MCP servers:
   ```bash
   # Install MCP servers globally
   pip install mcp-server-postgres
   npm install -g mcp-server-filesystem
   pip install mcp-server-aws
   pip install mcp-server-docker
   ```

#### **4. Tool Sets Configuration**

**File:** `~/Library/Application Support/Code/User/toolsets.jsonc` (macOS)

```jsonc
{
  // Development workflow tool sets
  "backend-dev": {
    "tools": [
      "codebase",
      "editFiles", 
      "runCommands",
      "runTasks",
      "postgres-tools",
      "docker-tools",
      "problems"
    ],
    "description": "Backend development and database work",
    "icon": "server"
  },
  
  "frontend-dev": {
    "tools": [
      "codebase",
      "editFiles",
      "openSimpleBrowser", 
      "runCommands",
      "runTasks",
      "fetch",
      "problems"
    ],
    "description": "Frontend development and testing",
    "icon": "browser"
  },
  
  "security-audit": {
    "tools": [
      "codebase",
      "search",
      "usages",
      "fetch",
      "githubRepo",
      "problems"
    ],
    "description": "Security analysis and code review",
    "icon": "shield"
  },
  
  "data-science": {
    "tools": [
      "newJupyterNotebook",
      "runNotebooks",
      "postgres-tools",
      "fetch",
      "codebase",
      "editFiles"
    ],
    "description": "Data analysis and machine learning",
    "icon": "graph"
  },
  
  "devops": {
    "tools": [
      "runCommands",
      "runTasks", 
      "docker-tools",
      "aws-tools",
      "codebase",
      "problems"
    ],
    "description": "DevOps and infrastructure management", 
    "icon": "cloud"
  }
}
```

**How to Apply:**
1. Open Command Palette: `Cmd+Shift+P`
2. Type: "Chat: Configure Tool Sets"
3. Select: "Create new tool sets file"
4. Replace content with configuration above

#### **5. Custom Chat Mode Examples**

**File:** `<project>/.vscode/chatmodes/code-review.md`

```markdown
---
description: 'Comprehensive code review mode with security focus'
tools: ['codebase', 'usages', 'problems', 'fetch', 'githubRepo', 'security-audit']
model: 'gpt-4'
---

# Code Review Assistant

You are a senior software engineer conducting a thorough code review. Focus on:

## 🔍 Code Quality
- **Architecture**: Assess overall design patterns
- **Performance**: Identify potential bottlenecks  
- **Maintainability**: Check for code clarity and documentation
- **Testing**: Ensure adequate test coverage

## 🔒 Security Analysis
- **Vulnerabilities**: Look for common security issues (OWASP Top 10)
- **Input Validation**: Check for proper sanitization
- **Authentication**: Verify secure auth implementations
- **Dependencies**: Check for vulnerable packages

## 📋 Best Practices
- **Standards Compliance**: Compare with #githubRepo airbnb/javascript
- **Industry Patterns**: Reference #fetch https://web.dev/security
- **Team Guidelines**: Follow project conventions

Always provide actionable feedback with specific examples and suggested improvements.
```

**File:** `<project>/.github/chatmodes/feature-planning.md`

```markdown
---
description: 'Feature planning and architecture design mode'
tools: ['codebase', 'new', 'fetch', 'githubRepo', 'backend-dev', 'frontend-dev']
---

# Feature Planning Assistant

You are an experienced tech lead planning new features. Your approach:

## 🎯 Requirements Analysis
1. **Understand** the feature requirements thoroughly
2. **Identify** technical dependencies and constraints  
3. **Research** similar implementations #githubRepo
4. **Plan** the implementation strategy

## 🏗️ Architecture Design
1. **Database Schema**: Design data models
2. **API Design**: Plan endpoints and contracts
3. **Frontend Components**: Design UI architecture
4. **Integration Points**: Identify external services

## 📋 Implementation Plan
1. **Task Breakdown**: Create detailed development tasks
2. **Dependencies**: Map prerequisite work
3. **Testing Strategy**: Plan unit, integration, and e2e tests
4. **Deployment**: Consider rollout and monitoring

Use #codebase to understand existing patterns and #new to scaffold components.
```

**How to Apply Chat Modes:**
1. Create the folders: `.vscode/chatmodes/` or `.github/chatmodes/`
2. Add the `.md` files with configurations above
3. Restart VSCode or reload window
4. Access via Chat Mode dropdown in Chat view

#### **6. Team Configuration Template**

**File:** `<project>/.vscode/settings.json` (Team Settings)

```json
{
  // Team-wide Agent Mode configuration
  "chat.agent.enabled": true,
  "chat.agent.maxRequests": 12,
  
  // Safety settings for team use
  "chat.tools.autoApprove": false,
  "github.copilot.chat.agent.autoFix": false,
  
  // Allowed tools for team projects
  "chat.agent.allowedTools": [
    "codebase",
    "editFiles",
    "search", 
    "problems",
    "usages",
    "changes",
    "fetch",
    "githubRepo",
    "findTestFiles",
    "testFailure"
  ],
  
  // Restricted tools
  "chat.agent.disallowedTools": [
    "runCommands",
    "runTasks"
  ],
  
  // Chat mode locations
  "chat.modeFilesLocations": [
    ".github/chatmodes",
    ".vscode/chatmodes"
  ],
  
  // Enhanced search for better context
  "github.copilot.chat.codesearch.enabled": true
}
```

### **🚀 Quick Setup Scripts**

#### **macOS/Linux Setup Script**

```bash
#!/bin/bash
# VSCode Agent Mode Quick Setup

echo "Setting up VSCode Agent Mode configuration..."

# Create necessary directories
VSCODE_USER_DIR="$HOME/Library/Application Support/Code/User"
mkdir -p "$VSCODE_USER_DIR/chatmodes"
mkdir -p ".vscode/chatmodes"
mkdir -p ".github/chatmodes"

# Create basic user settings
cat > "$VSCODE_USER_DIR/settings.json" << 'EOF'
{
  "chat.agent.enabled": true,
  "chat.agent.maxRequests": 20,
  "github.copilot.chat.agent.autoFix": true,
  "chat.extensionTools.enabled": true,
  "chat.mcp.discovery.enabled": true,
  "github.copilot.chat.codesearch.enabled": true
}
EOF

# Create workspace settings
cat > ".vscode/settings.json" << 'EOF'
{
  "chat.agent.enabled": true,
  "chat.agent.maxRequests": 15,
  "chat.tools.autoApprove": false,
  "chat.modeFilesLocations": [
    ".vscode/chatmodes",
    ".github/chatmodes"
  ]
}
EOF

# Create MCP configuration
cat > ".vscode/mcp.json" << 'EOF'
{
  "servers": {
    "fetch-tools": {
      "type": "stdio",
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    }
  }
}
EOF

echo "✅ VSCode Agent Mode configuration complete!"
echo "🔄 Please restart VSCode to apply changes"
```

#### **Windows PowerShell Setup Script**

```powershell
# VSCode Agent Mode Quick Setup for Windows

Write-Host "Setting up VSCode Agent Mode configuration..." -ForegroundColor Green

# Create necessary directories
$VSCodeUserDir = "$env:APPDATA\Code\User"
New-Item -ItemType Directory -Force -Path "$VSCodeUserDir\chatmodes"
New-Item -ItemType Directory -Force -Path ".vscode\chatmodes"  
New-Item -ItemType Directory -Force -Path ".github\chatmodes"

# Create basic user settings
$userSettings = @{
    "chat.agent.enabled" = $true
    "chat.agent.maxRequests" = 20
    "github.copilot.chat.agent.autoFix" = $true
    "chat.extensionTools.enabled" = $true
    "chat.mcp.discovery.enabled" = $true
    "github.copilot.chat.codesearch.enabled" = $true
} | ConvertTo-Json -Depth 10

$userSettings | Out-File -FilePath "$VSCodeUserDir\settings.json" -Encoding UTF8

# Create workspace settings
$workspaceSettings = @{
    "chat.agent.enabled" = $true
    "chat.agent.maxRequests" = 15
    "chat.tools.autoApprove" = $false
    "chat.modeFilesLocations" = @(".vscode/chatmodes", ".github/chatmodes")
} | ConvertTo-Json -Depth 10

$workspaceSettings | Out-File -FilePath ".vscode\settings.json" -Encoding UTF8

Write-Host "✅ VSCode Agent Mode configuration complete!" -ForegroundColor Green
Write-Host "🔄 Please restart VSCode to apply changes" -ForegroundColor Yellow
```

### **📋 Configuration Validation Checklist**

Use this checklist to verify your configuration:

- [ ] **Agent Mode Enabled**: `chat.agent.enabled: true` in settings
- [ ] **Tool Access**: Can see tools in Chat view Tools picker
- [ ] **MCP Servers**: `MCP: List Servers` shows configured servers
- [ ] **Chat Modes**: Available in Chat Mode dropdown
- [ ] **Tool Sets**: Visible in Tools picker under tool sets section
- [ ] **File Permissions**: Configuration files have correct permissions
- [ ] **Restart Applied**: VSCode restarted after configuration changes

**Validation Commands:**
```bash
# Check if Agent Mode is working
Cmd/Ctrl + Shift + P → "Chat: Show Available Tools"

# Verify MCP servers
Cmd/Ctrl + Shift + P → "MCP: List Servers"

# Test tool sets
Open Chat → Tools picker → Look for custom tool sets

# Validate chat modes  
Open Chat → Mode dropdown → Look for custom modes
```
