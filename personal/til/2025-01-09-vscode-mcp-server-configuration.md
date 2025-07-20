# TIL: Configuring MCP Servers in VSCode (2025-01-09)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Seamless AI tool integration in VSCode** – Use MCP servers to connect Copilot Agent Mode with external tools, APIs, and data sources for advanced workflows.

---

## The Pain Point

Connecting VSCode Copilot Agent Mode to external tools and data sources is complex and error-prone. MCP servers standardize integration, making it secure, flexible, and scalable.

---

## Overview

Model Context Protocol (MCP) servers enable VSCode Copilot Agent Mode to connect with external tools, databases, APIs, and data sources through a standardized interface. This TIL provides a comprehensive guide to setting up and configuring MCP servers in VSCode based on the latest official documentation.

## What is MCP?

MCP (Model Context Protocol) is an open protocol that standardizes how AI applications provide context to LLMs. Think of MCP like a USB-C port for AI applications—it provides a standardized way to connect AI models to different data sources and tools.

### Key Components

- **MCP Hosts**: Programs like VSCode, Claude Desktop, IDEs that want to access data through MCP
- **MCP Clients**: Protocol clients that maintain 1:1 connections with servers  
- **MCP Servers**: Lightweight programs that expose specific capabilities through the standardized protocol
- **Local Data Sources**: Your computer's files, databases, and services
- **Remote Services**: External systems available over the internet

## Prerequisites

- **VSCode 1.99 or later** (MCP support is in preview)
- **GitHub Copilot** subscription (Free, Pro, or Enterprise)
- **Node.js** (for TypeScript-based servers)
- **Python/uvx** (for Python-based servers)

## Enable MCP Support in VSCode

1. **Enable MCP Setting**:
   ```json
   {
     "chat.mcp.enabled": true
   }
   ```

2. **Enable Agent Mode**:
   ```json
   {
     "chat.agent.enabled": true
   }
   ```

3. **Enable MCP Discovery** (optional):
   ```json
   {
     "chat.mcp.discovery.enabled": true
   }
   ```

## Configuration Methods

### 1. Workspace Configuration (Recommended for Teams)

Create `.vscode/mcp.json` in your workspace root:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "github-token",
      "description": "GitHub Personal Access Token",
      "password": true
    },
    {
      "type": "promptString", 
      "id": "perplexity-key",
      "description": "Perplexity API Key",
      "password": true
    }
  ],
  "servers": {
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "${workspaceFolder}"
      ]
    },
    "github": {
      "type": "stdio", 
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github-token}"
      }
    },
    "perplexity": {
      "type": "stdio",
      "command": "npx", 
      "args": ["-y", "server-perplexity-ask"],
      "env": {
        "PERPLEXITY_API_KEY": "${input:perplexity-key}"
      }
    },
    "memory": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

### 2. User Settings (Global Configuration)

Add to VSCode user settings (`settings.json`):

```json
{
  "mcp": {
    "servers": {
      "filesystem": {
        "type": "stdio",
        "command": "npx",
        "args": [
          "-y", 
          "@modelcontextprotocol/server-filesystem",
          "/Users/username/Desktop",
          "/Users/username/Downloads"
        ]
      },
      "fetch": {
        "type": "stdio",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-fetch"]
      }
    }
  }
}
```

### 3. Automatic Discovery

VSCode can automatically detect MCP servers configured in other tools like Claude Desktop:

```json
{
  "chat.mcp.discovery.enabled": true
}
```

This discovers servers from:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

## Popular MCP Servers

### Official Reference Servers

1. **Filesystem Server**:
   ```bash
   npx -y @modelcontextprotocol/server-filesystem
   ```

2. **Memory Server** (Knowledge Graph):
   ```bash
   npx -y @modelcontextprotocol/server-memory
   ```

3. **Fetch Server** (Web Content):
   ```bash
   npx -y @modelcontextprotocol/server-fetch
   ```

4. **Sequential Thinking Server**:
   ```bash
   npx -y @modelcontextprotocol/server-sequentialthinking
   ```

### Community Servers

- **GitHub**: Repository management and API integration
- **Database**: PostgreSQL, SQLite, MongoDB connections
- **Slack**: Channel management and messaging
- **Google Drive**: File access and search
- **Browser Automation**: Puppeteer, Playwright
- **Search**: Brave Search, web scraping

## Configuration Format

### Server Configuration Fields

**For `stdio` transport:**
```json
{
  "type": "stdio",
  "command": "command-name",
  "args": ["arg1", "arg2"],
  "env": {
    "ENV_VAR": "value"
  }
}
```

**For `sse` or `http` transport:**
```json
{
  "type": "sse",
  "url": "https://example.com/mcp",
  "headers": {
    "Authorization": "Bearer ${input:api-key}"
  }
}
```

### Input Variables

Define secure placeholders for sensitive information:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "unique-id",
      "description": "Human-readable description",
      "password": true  // Hide input value
    }
  ]
}
```

### Naming Conventions

- Use **camelCase** for server names (`uiTesting`, not `ui-testing`)
- Avoid whitespace or special characters
- Use unique, descriptive names (`github`, `database`, not `server1`)

## Using MCP in Agent Mode

### 1. Open Agent Mode

- Open Chat view (`Ctrl/Cmd + Shift + I`)
- Select **Agent** from the mode dropdown
- Or use direct link: `vscode://GitHub.Copilot-Chat/chat?mode=agent`

### 2. Select Tools

- Click the **Tools** button in chat input
- Select/deselect specific MCP tools
- Search tools by typing in the search box

### 3. Reference Tools in Prompts

```
# Direct tool reference
Use #filesystem to read my project structure

# Tool with context
#github search for issues related to authentication
```

### 4. Add MCP Resources

- Select **Add Context > MCP Resources**
- Choose resource type and input parameters
- Resources become available as context in chat

### 5. Use MCP Prompts

Invoke preconfigured prompts:
```
/mcp.servername.promptname
```

## Tool Management

### Tool Approval Settings

```json
{
  // Auto-approve all tools (experimental)
  "chat.tools.autoApprove": false,
  
  // Enable extension tools
  "chat.extensionTools.enabled": true
}
```

### Tool Sets

Group related tools for easier management:

```json
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
    "description": "Tools for reading and analyzing code",
    "icon": "tag"
  }
}
```

Create tool sets:
- Run: **Chat: Configure Tool Sets > Create new tool sets file**
- Save in user profile as `.jsonc` file

## Management Commands

| Command | Description |
|---------|-------------|
| `MCP: List Servers` | View all configured servers |
| `MCP: Add Server` | Add new server configuration |
| `MCP: Browse Resources` | View available MCP resources |
| `Chat: Reset Tool Confirmations` | Reset tool approval settings |

### Server Management Actions

For each server:
- **Start/Stop/Restart**: Control server lifecycle
- **Show Output**: View server logs for debugging
- **Show Configuration**: Edit server configuration
- **Configure Model Access**: Set up sampling permissions
- **Browse Resources**: Explore server capabilities

## Troubleshooting

### Common Issues

1. **Server Not Starting**:
   - Check command path and arguments
   - Verify required dependencies installed
   - Review server output logs
   - Ensure environment variables set correctly

2. **Tool Not Available**:
   - Verify server is running (`MCP: List Servers`)
   - Check tool selection in Agent mode
   - Restart VSCode if needed

3. **Authentication Errors**:
   - Verify API keys in input variables
   - Check environment variable names
   - Ensure tokens have required permissions

4. **Docker Issues**:
   - Remove `-d` (detached) mode from arguments
   - Check container logs for errors
   - Verify Docker image and commands

---

## Security Considerations

- Avoid hardcoding secrets; use input variables and secure storage.
- Only install trusted MCP servers and review configuration.
- Limit filesystem and API access to least privilege.
- Use HTTPS and authentication for remote servers.

---

## Related Resources

- [VSCode MCP Documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Official MCP Servers Repository](https://github.com/modelcontextprotocol/servers)
- [VSCode Agent Mode Guide](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)
- [MCP Client Examples](https://modelcontextprotocol.io/clients)

---

*⚡ Pro tip: Use workspace configuration for team projects and user settings for personal tools to maximize flexibility and security!*
