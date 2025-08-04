---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #fafafa
color: #333
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .small { font-size: 0.8em; }
  h1 { color: #2563EB; }
  h2 { color: #059669; }
  .highlight { background: #FEF3C7; padding: 1rem; border-radius: 8px; }
  .center { text-align: center; }
---

# What is an MCP Server?

## The Smart Adapter for AI Applications

**Model Context Protocol in Practice**

---

## The Problem 🤔

<div class="highlight">

**AI applications need to connect to everything:**
- Databases 🗃️
- Files 📁  
- APIs 🌐
- Services ⚙️

**But each integration requires custom code** 😰

</div>

---

## The Solution: MCP Servers 🔌

<div class="center">

**Think of MCP Server as a USB-C port for AI**

*One standardized interface that any AI application can understand*

</div>

---

## What MCP Servers Provide

<div class="columns">

<div>

### 🛠️ **Tools**
*AI Actions*

- Execute functions
- User approval required
- Examples:
  - `searchFlights()`
  - `sendEmail()`
  - `createEvent()`

</div>

<div>

### 📊 **Resources**  
*Context Data*

- Provide information
- URI-based access
- Examples:
  - `file:///report.pdf`
  - `weather://forecast/paris`
  - `calendar://events/2024`

</div>

</div>

---

## What MCP Servers Provide (cont.)

<div class="center">

### 📝 **Prompts**
*Interaction Templates*

User-controlled templates for common workflows

Examples:
- "Plan a vacation"
- "Summarize meetings" 
- "Debug code issue"

</div>

---

## How It Works

```mermaid
graph LR
    A["🤖 AI App<br/>(Claude, VS Code)"] <--> B["📡 MCP Client"]
    B <--> C["🔌 MCP Server"]
    C <--> D["💾 Your Systems"]
    
    classDef aiApp fill:#E8F4FD,stroke:#2563EB,stroke-width:2px,color:#1E40AF
    classDef mcpClient fill:#F0F9FF,stroke:#0284C7,stroke-width:2px,color:#0C4A6E
    classDef mcpServer fill:#FEF3C7,stroke:#D97706,stroke-width:2px,color:#92400E
    classDef external fill:#F3E8FF,stroke:#7C3AED,stroke-width:2px,color:#5B21B6
    
    class A aiApp
    class B mcpClient
    class C mcpServer
    class D external
```

---

## The Magic ✨

1. **Dynamic Discovery**
   AI applications automatically find available capabilities

2. **Automatic Adaptation**
   When servers add features, AI apps adapt instantly

3. **Secure Execution**
   All actions require explicit user approval

---

## Real-World Examples

| Server Type | Tools | Resources | Use Case |
|-------------|-------|-----------|----------|
| **GitHub MCP** | `createPR()` | `repo://files/*` | Code collaboration |
| **Database MCP** | `executeQuery()` | `schema://tables/*` | Data analysis |
| **Weather MCP** | `getAlerts()` | `weather://forecast/{city}` | Travel planning |

---

## Why MCP Servers Matter

<div class="columns">

<div>

### For Developers 👩‍💻
- **Write once, use everywhere**
- **No breaking changes**
- **Standardized debugging**

### For Organizations 🏢
- **Vendor independence**
- **Scalable architecture**
- **Compliance ready**

</div>

<div>

### For AI Applications 🤖
- **Plug-and-play integration**
- **Rich context access**
- **Secure by default**

</div>

</div>

---

## Getting Started

<div class="center">

### 1. Use Existing Servers
Browse **1000+ available servers**
[github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

### 2. Install in Your AI App
Configure Claude Desktop, VS Code, etc.

### 3. Build Custom Servers
Use official SDKs in Python, TypeScript, etc.

</div>

---

## The Big Picture 🌍

<div class="highlight center">

**MCP servers transform AI applications from isolated tools into extensible platforms**

*Creating a composable ecosystem where capabilities can be mixed, matched, and shared*

</div>

---

## Key Takeaways

✅ **MCP servers are smart adapters** between AI and your systems

✅ **Three capabilities**: Tools, Resources, Prompts

✅ **Dynamic and secure** - adapts automatically, requires approval

✅ **Write once, use everywhere** - works with any MCP-compatible AI app

✅ **Growing ecosystem** - 1000+ servers already available

---

## Questions?

<div class="center">

**Learn More:**
- [Official MCP Documentation](https://modelcontextprotocol.io/)
- [Server Examples](https://github.com/modelcontextprotocol/servers)

**Ready to build the future of AI integration?**

</div>

---

<div class="center small">

**Thank you!**

*Model Context Protocol: The USB-C for AI Applications*

</div>
