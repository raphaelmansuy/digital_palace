# Today I Learned: Comprehensive Guide to MCP Server Design and Best Practices

**Date:** 2025-07-07

**Sources:**

- [Model Context Protocol Official Documentation](https://modelcontextprotocol.io/)
- [MCP Server Quickstart](https://modelcontextprotocol.io/quickstart/server)
- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/)
- [MCP Tools, Resources, and Prompts Concepts](https://modelcontextprotocol.io/docs/concepts/)

## Overview

Today, I dove deep into the **Model Context Protocol (MCP)** - an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications: it provides a standardized way to connect AI models to different data sources and tools. This comprehensive guide synthesizes the latest official documentation and best practices for designing robust, production-ready MCP servers.

## Key Takeaways

### 1. Understanding MCP Core Concepts

MCP servers provide three main types of capabilities to LLM applications:

- **Resources**: File-like data that can be read by clients (API responses, file contents, database records)
- **Tools**: Functions that can be called by the LLM with user approval (system commands, API integrations, data processing)
- **Prompts**: Pre-written templates that help users accomplish specific tasks (workflows, slash commands)

**Why It Matters**: These primitives enable LLMs to access external data, execute actions, and provide guided interactions while maintaining security through user consent.

### 2. MCP Architecture and Transport

MCP follows a client-server architecture with flexible transport options:

- **JSON-RPC 2.0**: All communication uses JSON-RPC for request/response and notifications
- **Stdio Transport**: Standard input/output for local processes (ideal for development)
- **Streamable HTTP**: HTTP POST with optional Server-Sent Events for production deployments
- **Client-Server Model**: Hosts maintain 1:1 connections with servers through MCP clients

**Why It Matters**: This architecture ensures standardized communication while supporting both local development and scalable production deployments.

### 3. Security and Trust Principles

MCP emphasizes user-controlled security with these core principles:

- **User Consent**: Users must explicitly consent to all data access and tool operations
- **Data Privacy**: Hosts must obtain consent before exposing user data to servers
- **Tool Safety**: All tool executions require explicit user approval with clear descriptions
- **Input Validation**: Comprehensive validation of all parameters, URIs, and data inputs

**Why It Matters**: Security is built into the protocol design, ensuring users maintain control over their data and AI actions.

### 4. Tool Design Best Practices

When implementing MCP tools, follow these patterns:

- **Atomic Operations**: Keep tool operations focused and single-purpose
- **Descriptive Schemas**: Use detailed JSON Schema definitions with clear descriptions
- **Error Handling**: Return errors within results (not as protocol errors) so LLMs can see and handle them
- **Annotations**: Use tool annotations (readOnlyHint, destructiveHint, idempotentHint) for better UX

**Why It Matters**: Well-designed tools enable more effective LLM interactions while maintaining safety and predictability.

### 5. Resource Management Strategies

Effective resource handling requires:

- **URI Schemes**: Define clear, consistent URI patterns for resource identification
- **Content Types**: Support both text (UTF-8) and binary (base64) resources with proper MIME types
- **Dynamic Resources**: Use URI templates for parameterized resource access
- **Subscriptions**: Implement resource change notifications for real-time updates

**Why It Matters**: Proper resource management enables efficient data access and real-time collaboration between LLMs and external systems.

## MCP Server Implementation Examples

### Complete Weather Server (Python FastMCP)

Based on the official MCP quickstart, here's a production-ready weather server implementation:

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather-server")

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "mcp-weather-server/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

    if not data["features"]:
        return "No active alerts for this state."

    alerts = []
    for feature in data["features"]:
        props = feature["properties"]
        alert = f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
"""
        alerts.append(alert)
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    # First get the forecast grid endpoint
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "Unable to fetch forecast data for this location."

    # Get the forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast."

    # Format the periods into a readable forecast
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
```

### TypeScript MCP Server with Tools, Resources, and Prompts

Here's a comprehensive MCP server implementation in TypeScript:

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  ListToolsRequestSchema,
  CallToolRequestSchema,
  ListPromptsRequestSchema,
  GetPromptRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// Initialize the server
const server = new Server({
  name: "comprehensive-mcp-server",
  version: "1.0.0"
}, {
  capabilities: {
    resources: {},
    tools: {},
    prompts: {}
  }
});

// Resources implementation
server.setRequestHandler(ListResourcesRequestSchema, async () => {
  return {
    resources: [
      {
        uri: "logs://application",
        name: "Application Logs",
        description: "Current application logs",
        mimeType: "text/plain"
      },
      {
        uri: "config://app",
        name: "Application Config",
        description: "Current application configuration",
        mimeType: "application/json"
      }
    ]
  };
});

server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const uri = request.params.uri;
  
  if (uri === "logs://application") {
    const logs = "2025-01-07 10:00:00 INFO Server started\n2025-01-07 10:01:00 INFO Request processed";
    return {
      contents: [
        {
          uri,
          mimeType: "text/plain",
          text: logs
        }
      ]
    };
  }
  
  if (uri === "config://app") {
    const config = JSON.stringify({ port: 8000, debug: true }, null, 2);
    return {
      contents: [
        {
          uri,
          mimeType: "application/json", 
          text: config
        }
      ]
    };
  }
  
  throw new Error(`Resource not found: ${uri}`);
});

// Tools implementation
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "calculate_sum",
        description: "Add two numbers together",
        inputSchema: {
          type: "object",
          properties: {
            a: { type: "number", description: "First number" },
            b: { type: "number", description: "Second number" }
          },
          required: ["a", "b"]
        },
        annotations: {
          title: "Calculator",
          readOnlyHint: true,
          openWorldHint: false
        }
      },
      {
        name: "log_message",
        description: "Log a message to the system",
        inputSchema: {
          type: "object",
          properties: {
            message: { type: "string", description: "Message to log" },
            level: { type: "string", enum: ["info", "warn", "error"], description: "Log level" }
          },
          required: ["message"]
        },
        annotations: {
          title: "Logger",
          readOnlyHint: false,
          destructiveHint: false,
          openWorldHint: false
        }
      }
    ]
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  
  if (name === "calculate_sum") {
    const { a, b } = args as { a: number; b: number };
    const result = a + b;
    return {
      content: [
        {
          type: "text",
          text: `The sum of ${a} and ${b} is ${result}`
        }
      ]
    };
  }
  
  if (name === "log_message") {
    const { message, level = "info" } = args as { message: string; level?: string };
    const timestamp = new Date().toISOString();
    const logEntry = `${timestamp} ${level.toUpperCase()} ${message}`;
    
    return {
      content: [
        {
          type: "text",
          text: `Logged: ${logEntry}`
        }
      ]
    };
  }
  
  throw new Error(`Tool not found: ${name}`);
});

// Prompts implementation
server.setRequestHandler(ListPromptsRequestSchema, async () => {
  return {
    prompts: [
      {
        name: "analyze-logs",
        description: "Analyze application logs for issues",
        arguments: [
          {
            name: "timeframe",
            description: "Time period to analyze (e.g., '1h', '1d')",
            required: false
          }
        ]
      },
      {
        name: "debug-issue",
        description: "Help debug a specific issue",
        arguments: [
          {
            name: "error_message",
            description: "The error message to debug",
            required: true
          }
        ]
      }
    ]
  };
});

server.setRequestHandler(GetPromptRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  
  if (name === "analyze-logs") {
    const timeframe = args?.timeframe || "1h";
    return {
      description: `Analyze application logs for the last ${timeframe}`,
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: `Please analyze the application logs for any issues in the last ${timeframe}. Look for errors, warnings, and unusual patterns.`
          }
        }
      ]
    };
  }
  
  if (name === "debug-issue") {
    const errorMessage = args?.error_message;
    return {
      description: "Debug assistance for specific error",
      messages: [
        {
          role: "user",
          content: {
            type: "text",
            text: `I'm encountering this error: "${errorMessage}". Can you help me debug this issue? Please suggest potential causes and solutions.`
          }
        }
      ]
    };
  }
  
  throw new Error(`Prompt not found: ${name}`);
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCP Server running on stdio");
}

main().catch((error) => {
  console.error("Server error:", error);
  process.exit(1);
});
```

## Testing and Development

### Using MCP Inspector

The MCP Inspector provides an interactive debugging interface:

1. **Install**: Use `npx @modelcontextprotocol/inspector`
2. **Test Tools**: Directly invoke server tools and see results
3. **Debug Protocol**: Monitor JSON-RPC message exchanges
4. **Validate Schema**: Ensure proper tool and resource definitions

### Integration with Claude Desktop

Add your server to Claude Desktop configuration:

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/weather-server",
        "run",
        "weather.py"
      ]
    },
    "comprehensive": {
      "command": "node",
      "args": ["/absolute/path/to/comprehensive-server.js"]
    }
  }
}
```

### Testing with Python

```python
import pytest
import asyncio
from mcp.server.fastmcp import FastMCP

@pytest.mark.asyncio
async def test_weather_alerts():
    mcp = FastMCP("test-weather")
    
    # Test tool registration
    tools = await mcp.list_tools()
    assert len(tools.tools) == 2
    assert any(tool.name == "get_alerts" for tool in tools.tools)
    
    # Test tool execution
    result = await mcp.call_tool("get_alerts", {"state": "CA"})
    assert result.content
```

## Best Practices Summary

### Security

- Always validate inputs against JSON schemas
- Implement proper error handling that doesn't leak sensitive information
- Use tool annotations to indicate potential side effects
- Enable user consent for all tool executions

### Performance

- Implement async operations for I/O-bound tasks
- Use appropriate timeouts for external API calls
- Cache frequently accessed resources when possible
- Monitor server performance and resource usage

### Debugging

- Use structured logging with appropriate log levels
- Implement comprehensive error handling
- Test with MCP Inspector during development
- Monitor protocol-level communication for issues

### Deployment

- Use absolute paths in configuration files
- Implement proper environment variable management
- Consider containerization for production deployments
- Document server capabilities and usage patterns

## Why MCP Matters

The Model Context Protocol represents a significant step forward in AI application architecture by:

1. **Standardizing Integration**: Provides a unified way to connect LLMs with external systems
2. **Ensuring Security**: Built-in user consent and validation mechanisms
3. **Enabling Composability**: Mix and match different MCP servers for complex workflows
4. **Supporting Scalability**: From local development to production deployments
5. **Fostering Ecosystem**: Open protocol encourages innovation and interoperability

## 🔧 VS Code Integration

VS Code provides excellent support for MCP servers through its agent mode and Copilot extensibility platform. Here's how to integrate MCP servers with VS Code:

### Configuration Methods

VS Code supports multiple ways to add MCP servers:

1. **Workspace Configuration** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "my-custom-server": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "my_mcp_server"],
      "cwd": "${workspaceFolder}",
      "env": {
        "API_KEY": "${env:MY_API_KEY}"
      }
    }
  }
}
```

1. **User/Remote Settings** - Global configuration in VS Code settings
1. **Extension Registration** - Programmatic registration via extensions
1. **URL Handler** - Install via `vscode:mcp/install?...` links
1. **Command Line** - `code --add-mcp server-config.json`

### Supported MCP Features

VS Code implements the full MCP specification:

- **Tools**: Available in agent mode for automated invocation
- **Resources**: Accessible via "Add Context" or direct browsing
- **Prompts**: Invokable via slash commands (`/mcp.servername.promptname`)
- **Authorization**: OAuth support for GitHub and Microsoft Entra
- **Sampling**: LLM access for server-side processing

### Development & Debugging

Enable development mode for easier testing:

```json
{
  "servers": {
    "dev-server": {
      "type": "stdio",
      "command": "python",
      "args": ["server.py"],
      "dev": {
        "watch": "src/**/*.py",
        "debug": { "type": "python" }
      }
    }
  }
}
```

Features include:

- File watching with automatic restart
- Debugger attachment (Node.js/Python)
- Error logging in Output panel
- Server status monitoring

### Extension Development

Register MCP servers programmatically in VS Code extensions:

```typescript
// package.json
{
  "contributes": {
    "mcpServerDefinitionProviders": [
      {
        "id": "myServerProvider",
        "label": "My Custom MCP Server"
      }
    ]
  }
}

// Extension code
vscode.lm.registerMcpServerDefinitionProvider('myServerProvider', {
  provideMcpServerDefinitions() {
    return [{
      name: 'my-server',
      type: 'stdio',
      command: 'python',
      args: ['-m', 'my_server']
    }];
  },
  resolveMcpServerDefinition(definition) {
    // Handle authentication, validation, etc.
    return definition;
  }
});
```

### Best Practices for VS Code

1. **Tool Design**: Focus on atomic operations for agent mode
2. **Error Handling**: Provide clear error messages for the Problems panel
3. **Progress Reporting**: Use progress indicators for long operations
4. **Resource Templates**: Support parameterized resources with completions
5. **Security**: Implement proper authorization for sensitive operations

### Example: File System MCP Server

```python
import asyncio
from typing import Any, Sequence
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("File System Tools")

@mcp.tool()
def read_file(path: str) -> str:
    """Read contents of a file."""
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

@mcp.tool()
def list_directory(path: str = ".") -> list[str]:
    """List contents of a directory."""
    import os
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Error: {e}"]

if __name__ == "__main__":
    asyncio.run(mcp.run())
```

Configure in `.vscode/mcp.json`:

```json
{
  "servers": {
    "filesystem": {
      "type": "stdio",
      "command": "python",
      "args": ["filesystem_server.py"]
    }
  }
}
```

This server provides file system tools that VS Code's agent mode can automatically invoke when users ask to read files or explore directories.

## References

- [Model Context Protocol Official Documentation](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP Server Examples](https://modelcontextprotocol.io/examples)
- [MCP GitHub Organization](https://github.com/modelcontextprotocol)
- [VS Code MCP Developer Guide](https://code.visualstudio.com/api/extension-guides/ai/mcp)
- [VS Code MCP Servers Gallery](https://code.visualstudio.com/mcp)
- [VS Code Chat Participant API](https://code.visualstudio.com/api/extension-guides/ai/chat)
- [VS Code Extension Samples (MCP)](https://github.com/microsoft/vscode-extension-samples/blob/main/mcp-extension-sample)
- [FastMCP Python Framework](https://github.com/jlowin/fastmcp)
- [MCP Inspector Tool](https://github.com/modelcontextprotocol/inspector)
