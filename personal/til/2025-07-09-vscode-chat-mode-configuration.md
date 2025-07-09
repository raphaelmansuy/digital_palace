# TIL: How to Configure Chat Mode in VSCode (2025-07-09)

Today I learned how to set up custom chat modes in VSCode to create specialized AI coding assistants with tailored prompts and tool configurations.

## What is VSCode Chat Mode?

VSCode offers three built-in chat modes and supports custom chat modes for specialized workflows:

### Built-in Chat Modes
- **Ask Mode**: Optimized for answering questions about codebase, coding concepts, and technology
- **Edit Mode**: Optimized for making code edits across multiple files with direct application in the editor
- **Agent Mode**: Optimized for autonomous edits with tool invocation and terminal commands (requires VS Code 1.99+)

### Custom Chat Modes
Custom chat modes allow you to create specialized AI assistants with specific system prompts, tool configurations, and behaviors. They're particularly powerful for creating coding agents that follow specific workflows or methodologies.

## Configuration Paths & Methods

### 1. Command Palette Method (Recommended)

```bash
# Create new chat mode
Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (Mac)
# Search for: "Chat: New Mode File"

# Configure existing chat modes
Ctrl+Shift+P → "Chat: Configure Chat Modes"
```

### 2. File-Based Configuration

#### Workspace Chat Modes
**Default Location**: `.github/chatmodes/` folder in your workspace
**Custom Location**: Configure with `chat.modeFilesLocations` setting
**File Format**: `.chatmode.md`

```bash
# Example structure
your-workspace/
├── .github/
│   └── chatmodes/
│       ├── planning.chatmode.md
│       ├── debugging.chatmode.md
│       └── documentation.chatmode.md
└── .vscode/
    └── settings.json
```

#### User Profile Chat Modes
**Location**: User profile directory (accessible across all workspaces)
**Access**: Command Palette → "Chat: New Mode File" → "User Profile"

### 3. Settings Configuration

```json
// settings.json - Tool sets configuration
{
  "chat.modeFilesLocations": [".chatmodes", ".github/chatmodes"],
  "chat.agent.enabled": true,
  "chat.agent.maxRequests": 15,
  "chat.mcp.enabled": true,
  "chat.extensionTools.enabled": true
}
```

## Chat Mode File Structure

### Frontmatter Configuration

```yaml
---
description: 'Brief description shown in chat mode dropdown'
tools: ['codebase', 'editFiles', 'fetch', 'problems', 'runCommands', 'search']
---
```

### Available Tools (Built-in)

```yaml
Core Built-in Tools:
  - codebase: Search and understand codebase structure
  - editFiles: Create and modify files
  - search: Search within files and directories
  - fetch: Retrieve web content and documentation
  - problems: Check for code issues and diagnostics
  - runCommands: Execute terminal commands
  - runTasks: Run predefined VS Code tasks
  - changes: View git changes and diffs
  - findTestFiles: Locate test files for source files
  - usages: Find code references and usages
  - githubRepo: GitHub repository operations (if configured)

Extension Tools:
  - extensions: VS Code extension management
  - terminalSelection: Work with terminal selections
  - vscodeAPI: Access VS Code API functionality

MCP Tools:
  # Add any MCP server tools you've configured
  # Examples: database tools, API connectors, custom integrations
```

### Tool Sets Configuration

Create reusable tool groups in `.jsonc` format stored in your **user profile**.

**Location**: Tool sets files are stored in your user profile directory (not workspace-specific)
**Access**: Command Palette → "Chat: Configure Tool Sets" → "Create new tool sets file"
**File Format**: `.jsonc` file in user profile

```json
// Tool sets file (created via "Chat: Configure Tool Sets")
// File location: User profile directory (cross-workspace)
{
  "reader": {
    "tools": [
      "changes",
      "codebase", 
      "fetch",
      "findTestFiles",
      "githubRepo",
      "problems",
      "usages"
    ],
    "description": "Read-only tools for analysis and exploration",
    "icon": "search"
  },
  "developer": {
    "tools": [
      "codebase",
      "editFiles", 
      "runTasks",
      "runCommands",
      "problems"
    ],
    "description": "Full development workflow tools",
    "icon": "tools"
  }
}
```

**Key Notes:**
- Tool sets are **user-level configuration** (not workspace-specific)
- Available across all workspaces once created
- Use Command Palette to create and manage tool sets
- Reference tool sets in chat prompts with `#toolset-name`

### MCP Server Integration

Configure MCP servers for extended functionality:

#### Workspace MCP Configuration (`.vscode/mcp.json`)

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "api-key",
      "description": "API Key for external service",
      "password": true
    }
  ],
  "servers": {
    "perplexity": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "server-perplexity-ask"],
      "env": {
        "PERPLEXITY_API_KEY": "${input:api-key}"
      }
    },
    "database": {
      "type": "stdio", 
      "command": "uvx",
      "args": ["mcp-server-sqlite", "--db-path", "${workspaceFolder}/data.db"]
    }
  }
}
```

#### User Settings MCP Configuration

```json
// settings.json
{
  "mcp": {
    "servers": {
      "global-tools": {
        "type": "stdio",
        "command": "my-global-mcp-server",
        "args": []
      }
    }
  }
}
```

## Actionable Examples

### Example 1: Planning Mode (Read-Only)

**File**: `.github/chatmodes/planning.chatmode.md`

```markdown
---
description: 'Generate implementation plans without making code edits'
tools: ['codebase', 'fetch', 'findTestFiles', 'githubRepo', 'search', 'usages']
---

# Planning Mode Instructions

You are in planning mode. Your task is to generate implementation plans for new features or refactoring existing code.

**DO NOT make any code edits** - only generate plans.

## Plan Structure
Create a Markdown document with:

1. **Overview**: Brief description of the feature/refactoring task
2. **Requirements**: List of requirements and constraints  
3. **Implementation Steps**: Detailed step-by-step plan
4. **Testing Strategy**: Tests needed to verify implementation
5. **Risk Assessment**: Potential issues and mitigation strategies

## Analysis Process
1. Search codebase to understand current architecture
2. Find related test files and existing patterns
3. Research external documentation if needed
4. Identify dependencies and integration points
```

### Example 2: Advanced Coding Agent

**File**: `.github/chatmodes/senior-dev.chatmode.md`

```markdown
---
description: 'Production-grade coding agent with systematic workflow'
tools: ['codebase', 'editFiles', 'runTasks', 'problems', 'runCommands', 'search', 'changes']
---

# Senior Developer Agent

You are a senior-level coding agent with systematic workflow approach.

## Workflow Protocol
1. **Context Analysis**: Always search codebase first to understand context
2. **Task Planning**: Create detailed todo list before starting
3. **Implementation**: Make changes systematically with testing
4. **Quality Check**: Run tests and check for problems
5. **Documentation**: Update docs and comments as needed

## Todo List Management
- Use standard Markdown: `[ ]`, `[x]`, `[-]` 
- Wrap in code blocks with triple backticks
- Update after completing each step
- Never use HTML for todo lists

## Code Quality Standards
- Follow existing code style and patterns
- Add comprehensive error handling
- Include unit tests for new functionality
- Update documentation for public APIs
- Verify no lint errors or warnings

## Communication Style
- Acknowledge request with single sentence
- Explain actions before taking them
- Provide reasoning for technical decisions
- Keep responses concise and actionable
```

### Example 3: Debugging Specialist

**File**: `.github/chatmodes/debugger.chatmode.md`

```markdown
---
description: 'Specialized debugging and troubleshooting assistant'
tools: ['problems', 'codebase', 'search', 'changes', 'runCommands', 'usages']
---

# Debugging Specialist

You are a specialized debugging agent focused on identifying and resolving code issues.

## Debugging Methodology
1. **Problem Identification**: Use problems tool to identify current issues
2. **Root Cause Analysis**: Search codebase for related patterns and dependencies
3. **Historical Context**: Check recent changes that might have introduced issues
4. **Usage Analysis**: Find how problematic code is used throughout codebase
5. **Solution Verification**: Suggest fixes with minimal impact

## Investigation Process
- Start with problems tool to see current diagnostics
- Search for error patterns and similar issues
- Check git changes for recent modifications
- Analyze code usage to understand impact scope
- Provide step-by-step debugging guidance

## Solution Approach
- Suggest least invasive fixes first
- Provide multiple solution options when possible
- Include steps to verify the fix works
- Recommend preventive measures for similar issues
```

### Example 4: Documentation Writer

**File**: `.github/chatmodes/docs.chatmode.md`

```markdown
---
description: 'Technical documentation and README specialist'
tools: ['codebase', 'editFiles', 'search', 'fetch', 'githubRepo']
---

# Documentation Specialist

You are a technical documentation expert focused on creating clear, comprehensive documentation.

## Documentation Standards
- Use clear, concise language
- Include practical examples and code snippets
- Follow existing documentation style and structure
- Add proper cross-references and links
- Include troubleshooting sections where relevant

## Content Types
- **API Documentation**: Function signatures, parameters, return values, examples
- **README Files**: Project overview, setup instructions, usage examples
- **How-to Guides**: Step-by-step tutorials for common tasks
- **Architecture Docs**: System design and component interactions

## Research Process
1. Search codebase to understand functionality
2. Find existing documentation patterns
3. Research external resources for best practices
4. Identify missing or outdated documentation
5. Create comprehensive, user-friendly docs
```

## Advanced Configuration & Management

### Key Settings Reference

```json
// VS Code settings.json
{
  // Chat mode core settings
  "chat.agent.enabled": true,
  "chat.agent.maxRequests": 15,
  "chat.modeFilesLocations": [".chatmodes", ".github/chatmodes"],
  
  // Tool management
  "chat.extensionTools.enabled": true,
  "chat.tools.autoApprove": false,
  
  // MCP server settings  
  "chat.mcp.enabled": true,
  "chat.mcp.discovery.enabled": true,
  
  // Agent mode behavior
  "github.copilot.chat.agent.runTasks": true,
  "github.copilot.chat.agent.autoFix": true,
  "chat.editing.autoAcceptDelay": 0
}
```

### Management Commands

```bash
# Chat mode management
"Chat: New Mode File"           # Create new chat mode
"Chat: Configure Chat Modes"    # Edit existing modes

# Tool management  
"Chat: Configure Tool Sets"     # Create tool groupings
"Chat: Reset Tool Confirmations" # Reset tool approvals

# MCP server management
"MCP: Add Server"              # Add MCP server
"MCP: List Servers"            # View/manage servers
"MCP: Browse Resources"        # View MCP resources
```

### Enterprise Configuration

For organizations wanting to centrally manage chat modes:

```json
// Centrally managed settings
{
  "chat.agent.enabled": false,           // Disable agent mode
  "chat.tools.autoApprove": false,       // Require tool approval
  "chat.mcp.enabled": false,             // Disable MCP servers
  "chat.extensionTools.enabled": false   // Disable extension tools
}
```

### Multiple Environment Setup

**Development Environment**
```markdown
---
description: 'Development workflow with full toolset'
tools: ['codebase', 'editFiles', 'runTasks', 'runCommands', 'problems']
---
# Development instructions...
```

**Production Environment** 
```markdown
---
description: 'Read-only analysis for production issues'
tools: ['codebase', 'search', 'problems', 'changes']
---
# Production troubleshooting instructions...
```

**Code Review Environment**
```markdown  
---
description: 'Code review and quality assessment'
tools: ['codebase', 'search', 'problems', 'usages', 'changes']
---
# Code review guidelines...
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

### Essential Commands

```bash
# Chat Mode Management
Ctrl+Shift+P → "Chat: New Mode File"
Ctrl+Shift+P → "Chat: Configure Chat Modes"

# Tool Configuration  
Ctrl+Shift+P → "Chat: Configure Tool Sets"
Ctrl+Shift+P → "Chat: Reset Tool Confirmations"

# MCP Server Management
Ctrl+Shift+P → "MCP: Add Server"
Ctrl+Shift+P → "MCP: List Servers"

# Switch to Agent Mode (Direct)
Ctrl+Cmd+I (Mac) or Ctrl+Alt+I (Windows/Linux) → Select "Agent"
```

### File Locations

```bash
# Workspace chat modes (shared with team)
.github/chatmodes/*.chatmode.md
.chatmodes/*.chatmode.md  

# User profile chat modes (personal)
~/.vscode/chatmodes/*.chatmode.md

# MCP server configuration
.vscode/mcp.json          # Workspace
settings.json             # User profile

# Tool sets configuration (user profile only)
# Created via Command Palette: "Chat: Configure Tool Sets"
# Stored in user profile directory - accessible across all workspaces
User profile directory/.jsonc  # Exact path managed by VS Code
```

### Essential Settings

```json
{
  "chat.agent.enabled": true,
  "chat.agent.maxRequests": 15,
  "chat.mcp.enabled": true,
  "chat.extensionTools.enabled": true
}
```

## Prerequisites & Compatibility

- **VS Code Version**: 1.99+ (for Agent mode and MCP support)
- **GitHub Copilot**: Active subscription or free plan
- **Custom Chat Modes**: VS Code 1.101+ (currently in preview)
- **Agent Mode**: Requires `chat.agent.enabled: true`
- **MCP Support**: Requires `chat.mcp.enabled: true`

## Latest Features (2025)

### New in VS Code 1.101+
- **Custom Chat Modes**: Full support for `.chatmode.md` files
- **Tool Sets**: Group related tools for easier management
- **Enhanced MCP Integration**: Better server discovery and management
- **Improved Agent Mode**: More reliable autonomous editing

### MCP Server Ecosystem
- **Auto-discovery**: Reuse MCP servers from Claude Desktop
- **Workspace Configuration**: Share MCP setups with team via `.vscode/mcp.json`
- **Tool Approval**: Fine-grained control over tool execution
- **Resource Integration**: Access external data sources as chat context

*This TIL demonstrates how VS Code's chat modes have evolved into a powerful platform for AI-assisted development, offering unprecedented customization and integration capabilities for modern development workflows.*
