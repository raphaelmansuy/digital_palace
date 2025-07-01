# 🔗 Model Context Protocol (MCP) Servers - Complete Guide

> **🚀 Quick Start**: Get MCP servers running with AI coding assistants in under 10 minutes

## 📋 **Table of Contents**

- [What is MCP?](#what-is-mcp)
- [Getting Started](#getting-started)
- [Popular MCP Servers](#popular-mcp-servers)
- [AI Tool Integrations](#ai-tool-integrations)
- [Building Custom Servers](#building-custom-servers)
- [Production Deployment](#production-deployment)

---

## 🤖 **What is MCP?**

The Model Context Protocol (MCP) is a standardized way for AI applications to securely connect to external data sources and tools. Think of it as the "API protocol" for AI agents.

### **Key Benefits**

- **🔐 Security First**: Built-in permission and access controls
- **🔄 Standardization**: Write once, use across multiple AI applications
- **🛠️ Tool Reusability**: Growing ecosystem of pre-built servers
- **⚡ Performance**: Efficient communication between AI and external systems

---

## 🚀 **Getting Started**

### **Quick Setup with Cline (VS Code)**

1. **Install Cline Extension**
   ```bash
   # In VS Code: Extensions → Search "Cline" → Install
   ```

2. **Configure MCP Server**
   ```json
   // In Cline settings
   {
     "mcpServers": {
       "filesystem": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"],
         "env": {}
       }
     }
   }
   ```

3. **Test Connection**
   - Ask Cline: "List files in the current directory"
   - Cline will use the MCP filesystem server to respond

### **Setup with Continue (VS Code/JetBrains)**

1. **Install Continue**
   ```bash
   # VS Code: Extensions → Search "Continue" → Install
   ```

2. **Add MCP Configuration**
   ```yaml
   # config.yaml
   mcpServers:
     - name: "git"
       command: "npx"
       args: ["-y", "@modelcontextprotocol/server-git", "--repository", "."]
   ```

---

## 🛠️ **Popular MCP Servers**

### **🗂️ File & System Management**

| Server | Purpose | Installation | Use Case |
|--------|---------|--------------|----------|
| **[Filesystem](https://github.com/modelcontextprotocol/servers)** | File operations | `npx @modelcontextprotocol/server-filesystem` | Read/write files safely |
| **[Git](https://github.com/modelcontextprotocol/git)** | Version control | `npx @modelcontextprotocol/server-git` | Commit, branch, merge operations |
| **[Docker](https://github.com/modelcontextprotocol/docker)** | Container management | `npx @modelcontextprotocol/server-docker` | Deploy and manage containers |

### **🌐 Web & APIs**

| Server | Purpose | Installation | Use Case |
|--------|---------|--------------|----------|
| **[Brave Search](https://github.com/modelcontextprotocol/brave-search)** | Web search | `npx @modelcontextprotocol/server-brave-search` | Real-time web information |
| **[Puppeteer](https://github.com/modelcontextprotocol/puppeteer)** | Browser automation | `npx @modelcontextprotocol/server-puppeteer` | Web scraping, testing |
| **[Fetch](https://github.com/modelcontextprotocol/fetch)** | HTTP requests | `npx @modelcontextprotocol/server-fetch` | API integrations |

### **💾 Database & Storage**

| Server | Purpose | Installation | Use Case |
|--------|---------|--------------|----------|
| **[SQLite](https://github.com/modelcontextprotocol/sqlite)** | Database operations | `npx @modelcontextprotocol/server-sqlite` | Local database management |
| **[PostgreSQL](https://github.com/modelcontextprotocol/postgres)** | Database operations | `npx @modelcontextprotocol/server-postgres` | Production database access |
| **[Memory](https://github.com/modelcontextprotocol/memory)** | Persistent memory | `npx @modelcontextprotocol/server-memory` | Context retention |

### **🔧 Development Tools**

| Server | Purpose | Installation | Use Case |
|--------|---------|--------------|----------|
| **[GitHub](https://github.com/modelcontextprotocol/github)** | Repository management | `npx @modelcontextprotocol/server-github` | Issues, PRs, releases |
| **[Jira](https://github.com/modelcontextprotocol/jira)** | Project management | `npx @modelcontextprotocol/server-jira` | Ticket management |
| **[Slack](https://github.com/modelcontextprotocol/slack)** | Team communication | `npx @modelcontextprotocol/server-slack` | Message, channel management |

---

## 🤖 **AI Tool Integrations**

### **Cline (VS Code)**
- **Native MCP Support**: Built-in MCP server management
- **Configuration**: JSON-based server definitions
- **Capabilities**: File operations, git commands, web search
- **Best For**: Development workflows, code analysis

### **Continue (VS Code/JetBrains)**
- **YAML Configuration**: Easy server setup
- **Multi-Model Support**: Works with various LLMs
- **Extensible**: Plugin architecture for custom servers
- **Best For**: Code completion, refactoring

### **Cursor AI**
- **Directory Integration**: MCP servers via [Cursor Directory](https://cursor.directory/)
- **Pre-configured Setups**: Ready-to-use server configurations
- **Community Servers**: Curated collection of MCP servers
- **Best For**: Rapid prototyping, AI-first development

---

## 🏗️ **Building Custom Servers**

### **Python Example**

```python
# my_mcp_server.py
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

app = Server("my-custom-server")

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="say_hello",
            description="Say hello to someone",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Name to greet"}
                },
                "required": ["name"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "say_hello":
        return [TextContent(type="text", text=f"Hello, {arguments['name']}!")]
    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
```

### **TypeScript Example**

```typescript
// my-mcp-server.ts
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new Server('my-custom-server', '1.0.0');

server.setRequestHandler('tools/list', async () => ({
  tools: [{
    name: 'calculate',
    description: 'Perform basic calculations',
    inputSchema: {
      type: 'object',
      properties: {
        operation: { type: 'string', enum: ['add', 'subtract', 'multiply', 'divide'] },
        a: { type: 'number' },
        b: { type: 'number' }
      },
      required: ['operation', 'a', 'b']
    }
  }]
}));

server.setRequestHandler('tools/call', async (request) => {
  const { name, arguments: args } = request.params;
  
  if (name === 'calculate') {
    const { operation, a, b } = args;
    let result: number;
    
    switch (operation) {
      case 'add': result = a + b; break;
      case 'subtract': result = a - b; break;
      case 'multiply': result = a * b; break;
      case 'divide': result = a / b; break;
    }
    
    return {
      content: [{ type: 'text', text: `Result: ${result}` }]
    };
  }
  
  throw new Error(`Unknown tool: ${name}`);
});

const transport = new StdioServerTransport();
server.connect(transport);
```

---

## 🚀 **Production Deployment**

### **Docker Deployment**

```dockerfile
# Dockerfile
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
EXPOSE 3000

CMD ["node", "server.js"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  mcp-server:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    volumes:
      - ./data:/app/data
```

### **AWS Lambda Deployment**

```typescript
// lambda-handler.ts
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { LambdaServerTransport } from '@modelcontextprotocol/sdk/server/lambda.js';

const server = new Server('lambda-mcp-server', '1.0.0');

// Add your tool handlers here
server.setRequestHandler('tools/list', async () => ({ tools: [] }));

export const handler = async (event: any) => {
  const transport = new LambdaServerTransport(event);
  return await server.connect(transport);
};
```

### **Monitoring & Logging**

```javascript
// monitoring.js
import { createLogger } from 'winston';

const logger = createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

// Add to your MCP server
server.onerror = (error) => {
  logger.error('MCP Server Error:', error);
};
```

---

## 🔗 **Related Resources**

### **Documentation**
- [MCP Official Docs](https://modelcontextprotocol.io/)
- [MCP SDK Reference](https://github.com/modelcontextprotocol/typescript-sdk)
- [Community Examples](https://github.com/modelcontextprotocol/examples)

### **Digital Palace Guides**
- [AI Agents Development](./ai-agents.md)
- [AI Tools Directory](../tools/ai-tools-master-directory.md)
- [Core Technologies](../reference/core-technologies.md#model-context-protocol-mcp)

### **Community Resources**
- [Awesome MCP](https://github.com/punkpeye/awesome-mcp) - Curated list of MCP resources
- [MCP Tools](https://github.com/f/mcptools) - Swiss Army Knife for MCP Servers
- [Active Pieces](https://github.com/activepieces/activepieces) - 280+ MCP servers

---

## 📧 **Need Help?**

- **🐛 Issues**: [MCP GitHub Issues](https://github.com/modelcontextprotocol/specification/issues)
- **💬 Community**: [MCP Discord](https://discord.gg/modelcontextprotocol)
- **📖 Learning**: [Digital Palace Learning Hub](../learning/README.md)

---

**⭐ Star this guide** if it helped you set up MCP servers successfully!
