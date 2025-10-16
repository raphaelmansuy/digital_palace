# Part 4: Protocols & Architecture

[← Previous: Platforms Compared](./03-platforms-compared.md) | [Back to Index](./README.md) | [Next: Implementation Guide →](./05-implementation.md)

---

## The Plumbing That Makes It Work

We've seen **what** platforms provide and **which** platforms exist. Now let's understand **how** they work under the hood.

Two protocols are emerging as standards:

1. **MCP (Model Context Protocol)** - Tool integration standard (like USB-C for AI)
2. **A2A (Agent-to-Agent Protocol)** - Agent communication standard (like SMTP for agents)

Plus the **unified core architecture** that all platforms share.

---

## MCP: The "USB-C for AI Tools"

### The Problem MCP Solves

**Before MCP** (2023-2024):

```text
Every agent builds custom integrations to every tool:

Agent A ──┬─── Custom Salesforce connector (1000 lines)
          ├─── Custom Slack connector (800 lines)
          └─── Custom GitHub connector (1200 lines)

Agent B ──┬─── Different Salesforce connector! (1000 lines)
          ├─── Different Slack connector! (800 lines)
          └─── Different GitHub connector! (1200 lines)

Total: 6000 lines of duplicated integration code
```

**With MCP** (2025 onwards):

```text
Standard protocol, reusable connectors:

MCP Server: Salesforce ──┬─── Agent A
MCP Server: Slack ───────┼─── Agent B
MCP Server: GitHub ──────┴─── Agent C

Total: 3 MCP servers, shared by all agents
```

### MCP Architecture

```text
╔══════════════════════════════════════════════════════════════════╗
║                    MCP ARCHITECTURE                              ║
║                "USB-C for AI Tools"                              ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   ┌──────────────────────────────────────────────────────────┐  ║
║   │                    YOUR AI AGENTS                        │  ║
║   │  [Customer Service] [Sales] [Data] [Code] [HR]           │  ║
║   └─────────┬───────────┬────────────┬──────────┬────────────┘  ║
║             │           │            │          │                ║
║   ┌─────────┴───────────┴────────────┴──────────┴────────────┐  ║
║   │          MCP CLIENT (in your platform)                   │  ║
║   │  - Discovery: What tools are available?                  │  ║
║   │  - Request formatting: Convert agent intent to MCP       │  ║
║   │  - Response parsing: Convert MCP back to agent context   │  ║
║   └─────────┬───────────┬────────────┬──────────┬────────────┘  ║
║             │           │            │          │                ║
║             │  MCP Protocol (JSON-RPC over stdio/HTTP/SSE)   │  ║
║             │  ┌───────────────────────────────────┐         │  ║
║             │  │ Standard Message Format:          │         │  ║
║             │  │ { "method": "tools/call",         │         │  ║
║             │  │   "params": {                     │         │  ║
║             │  │     "name": "query_crm",          │         │  ║
║             │  │     "arguments": {...}            │         │  ║
║             │  │   }                                │         │  ║
║             │  │ }                                  │         │  ║
║             │  └───────────────────────────────────┘         │  ║
║             │           │            │          │                ║
║   ┌─────────┴───────────┴────────────┴──────────┴────────────┐  ║
║   │                    MCP SERVERS                           │  ║
║   │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐  │  ║
║   │  │Salesforce│  │  Slack   │  │  GitHub  │  │ Custom  │  │  ║
║   │  │  Server  │  │  Server  │  │  Server  │  │  Tool   │  │  ║
║   │  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬────┘  │  ║
║   └───────┼─────────────┼─────────────┼─────────────┼───────┘  ║
║           │             │             │             │           ║
║   ┌───────┴─────────────┴─────────────┴─────────────┴───────┐  ║
║   │              EXTERNAL SERVICES                           │  ║
║   │  [Salesforce API] [Slack API] [GitHub API] [Your API]   │  ║
║   └──────────────────────────────────────────────────────────┘  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

KEY BENEFITS:
├─ Reusability: One MCP server, many agents
├─ Discoverability: Agents ask "what tools exist?"
├─ Standardization: Same protocol for all tools
└─ Security: MCP server handles auth, not agents
```

### MCP Message Flow: Example

**Scenario**: Agent wants to query Salesforce CRM.

```text
STEP 1: Agent discovers available tools
┌──────────┐                           ┌─────────────┐
│  Agent   │ ─────────────────────────>│ MCP Client  │
│          │  "What tools can I use?"  │             │
└──────────┘                           └──────┬──────┘
                                              │
                                              │ tools/list
                                              │
┌──────────────────┐                   ┌──────▼──────┐
│ MCP Server:      │<──────────────────│ MCP Client  │
│ Salesforce       │   discovery req   │             │
└────────┬─────────┘                   └─────────────┘
         │
         │ returns: ["query_crm", "create_lead", "update_opp"]
         │
┌────────▼─────────┐                   ┌─────────────┐
│ MCP Server:      │───────────────────>│ MCP Client  │
│ Salesforce       │   tool list        │             │
└──────────────────┘                   └──────┬──────┘
                                              │
                                              │ presents tools
                                              │
┌──────────┐                           ┌──────▼──────┐
│  Agent   │<──────────────────────────│ MCP Client  │
│          │  "You can use query_crm"  │             │
└──────────┘                           └─────────────┘

STEP 2: Agent calls tool
┌──────────┐                           ┌─────────────┐
│  Agent   │ ─────────────────────────>│ MCP Client  │
│          │ query_crm(customer="XYZ") │             │
└──────────┘                           └──────┬──────┘
                                              │
                                              │ tools/call
                                              │ { "name": "query_crm",
                                              │   "arguments": {"customer": "XYZ"} }
                                              │
┌──────────────────┐                   ┌──────▼──────┐
│ MCP Server:      │<──────────────────│ MCP Client  │
│ Salesforce       │   tool call       │             │
└────────┬─────────┘                   └─────────────┘
         │
         │ executes: Salesforce API call
         │ (handles OAuth, rate limits, retries)
         │
┌────────▼─────────┐                   ┌─────────────┐
│ MCP Server:      │───────────────────>│ MCP Client  │
│ Salesforce       │   result           │             │
└──────────────────┘   {customer data}  └──────┬──────┘
                                              │
                                              │ parses result
                                              │
┌──────────┐                           ┌──────▼──────┐
│  Agent   │<──────────────────────────│ MCP Client  │
│          │  customer data             │             │
└──────────┘                           └─────────────┘

STEP 3: Agent continues reasoning
┌──────────┐
│  Agent   │ "Based on customer XYZ's data, I should..."
│          │ (continues agent logic with tool result)
└──────────┘
```

### MCP Ecosystem (October 2025)

**Official MCP Servers** (from Anthropic and community):

- **Claude Desktop**: filesystem, database, web browsing
- **AWS**: S3, DynamoDB, Lambda, Bedrock
- **Google**: BigQuery, Cloud Storage, Vertex AI
- **Databases**: PostgreSQL, MySQL, MongoDB, Redis
- **DevOps**: GitHub, GitLab, Kubernetes, Docker
- **Productivity**: Slack, Notion, Google Workspace

**MCP Server Statistics**:
- 100+ community MCP servers (as of Oct 2025)
- Growing at ~10 new servers per week
- Standard: All use JSON-RPC over stdio/HTTP/SSE

**Key Platforms Supporting MCP**:
- ✅ AWS Bedrock (Gateway service)
- ✅ Google ADK (MCP client built-in)
- ✅ Salesforce Agentforce (MCP integration)
- ✅ Claude Desktop (native MCP support)
- ✅ LangChain, LangGraph, CrewAI (via connectors)

**Why MCP is winning**: It's **open, simple, and battle-tested** (inspired by LSP - Language Server Protocol).

---

## A2A: Agent-to-Agent Communication

### The Problem A2A Solves

**Before A2A**:

```text
Agent A needs help from Agent B:

Problem 1: Discovery
└─ How does Agent A even know Agent B exists?
   └─ Hardcoded list? Service registry? Manual config?

Problem 2: Communication
└─ How do agents exchange messages?
   └─ REST API? WebSocket? Custom protocol?

Problem 3: Context Transfer
└─ How does Agent B understand what Agent A was doing?
   └─ Shared database? Message payload? No context?

Problem 4: Trust
└─ Should Agent B trust Agent A's request?
   └─ Authentication? Authorization? Audit?

Result: Every company builds custom solutions.
```

**With A2A**:

```text
Standard protocol for agent coordination:

Agent A ─────┬─ A2A Protocol ───> Agent B
             │  - Discovery: Who can do what?
             │  - Message format: Standard JSON-RPC
             │  - Context: Shared conversation state
             └─ Security: Identity + permissions
```

### A2A Protocol Architecture

```text
╔══════════════════════════════════════════════════════════════════╗
║                    A2A PROTOCOL ARCHITECTURE                     ║
║              "Agent-to-Agent Communication Standard"             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   AGENT DISCOVERY (Dynamic Service Registry)                    ║
║   ┌──────────────────────────────────────────────────────────┐  ║
║   │              A2A Service Registry                        │  ║
║   │  ┌────────────────────────────────────────────────────┐  │  ║
║   │  │ Agent: sales_assistant                            │  │  ║
║   │  │ Capabilities: [customer_lookup, send_proposal]    │  │  ║
║   │  │ Endpoint: https://api.company.com/agents/sales    │  │  ║
║   │  │ Auth: OAuth2 client credentials                   │  │  ║
║   │  └────────────────────────────────────────────────────┘  │  ║
║   │  ┌────────────────────────────────────────────────────┐  │  ║
║   │  │ Agent: data_analyst                               │  │  ║
║   │  │ Capabilities: [run_analytics, generate_report]    │  │  ║
║   │  │ Endpoint: https://api.company.com/agents/data     │  │  ║
║   │  │ Auth: OAuth2 client credentials                   │  │  ║
║   │  └────────────────────────────────────────────────────┘  │  ║
║   └──────────────────────────────────────────────────────────┘  ║
║                              ▲                                   ║
║                              │ query: "Who can run_analytics?"  ║
║                              │                                   ║
║   ┌──────────────────────────┴───────────────────────────────┐  ║
║   │              AGENT A (Sales Assistant)                   │  ║
║   │  ─ Needs analytics on customer XYZ                       │  ║
║   │  ─ Discovers Agent B via A2A registry                    │  ║
║   │  ─ Sends A2A task request                                │  ║
║   └──────────────────────┬───────────────────────────────────┘  ║
║                          │                                       ║
║                          │ A2A MESSAGE (JSON-RPC)                ║
║                          │ ┌─────────────────────────────────┐  ║
║                          │ │ {                               │  ║
║                          │ │   "jsonrpc": "2.0",             │  ║
║                          │ │   "method": "agent/invoke",     │  ║
║                          │ │   "params": {                   │  ║
║                          │ │     "task": "run_analytics",    │  ║
║                          │ │     "context": {                │  ║
║                          │ │       "customer_id": "XYZ",     │  ║
║                          │ │       "conversation_id": "123", │  ║
║                          │ │       "history": [...]          │  ║
║                          │ │     }                            │  ║
║                          │ │   },                            │  ║
║                          │ │   "auth": {                     │  ║
║                          │ │     "token": "...",             │  ║
║                          │ │     "agent_id": "sales_agent"   │  ║
║                          │ │   }                             │  ║
║                          │ │ }                               │  ║
║                          │ └─────────────────────────────────┘  ║
║                          │                                       ║
║                          ▼                                       ║
║   ┌──────────────────────────────────────────────────────────┐  ║
║   │              AGENT B (Data Analyst)                      │  ║
║   │  ─ Receives task with full context                       │  ║
║   │  ─ Runs analytics on customer XYZ                        │  ║
║   │  ─ Returns results via A2A                               │  ║
║   └──────────────────────┬───────────────────────────────────┘  ║
║                          │                                       ║
║                          │ A2A RESPONSE                          ║
║                          │ ┌─────────────────────────────────┐  ║
║                          │ │ {                               │  ║
║                          │ │   "jsonrpc": "2.0",             │  ║
║                          │ │   "result": {                   │  ║
║                          │ │     "analytics": {              │  ║
║                          │ │       "ltv": "$50K",            │  ║
║                          │ │       "churn_risk": "low"       │  ║
║                          │ │     }                            │  ║
║                          │ │   },                            │  ║
║                          │ │   "conversation_id": "123"      │  ║
║                          │ │ }                               │  ║
║                          │ └─────────────────────────────────┘  ║
║                          ▼                                       ║
║   ┌──────────────────────────────────────────────────────────┐  ║
║   │              AGENT A (Sales Assistant)                   │  ║
║   │  ─ Receives analytics with full context                  │  ║
║   │  ─ Continues conversation with customer                  │  ║
║   │  ─ "Based on your $50K lifetime value..."                │  ║
║   └──────────────────────────────────────────────────────────┘  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

KEY BENEFITS:
├─ Discovery: Agents find each other dynamically
├─ Context Transfer: Full conversation history preserved
├─ Security: Authentication + authorization built-in
└─ Cross-Platform: Works across clouds (GCP, AWS, on-prem)
```

### A2A vs Traditional APIs

| Feature | Traditional REST API | A2A Protocol |
|---------|---------------------|--------------|
| **Discovery** | Hardcoded endpoints | Dynamic service registry |
| **Context** | Stateless (pass everything) | Stateful (conversation ID) |
| **Security** | API keys, OAuth | Agent identity + permissions |
| **Format** | Custom JSON | Standard JSON-RPC |
| **Coordination** | Manual orchestration | Built-in task handoff |
| **Observability** | Custom logging | A2A trace headers |

**Example**: Agent A needs help from Agent B.

**Traditional API approach**:

```python
# Agent A code:
import requests

# Hardcoded endpoint (brittle)
response = requests.post(
    'https://api.company.com/agents/data_analyst/run_analytics',
    json={'customer_id': 'XYZ'},
    headers={'Authorization': 'Bearer ' + api_key}
)

# No conversation context! Agent B starts from scratch.
# Agent A must manually pass all relevant history.
```

**A2A approach**:

```python
# Agent A code:
from google.adk.protocols.a2a import A2AClient

a2a = A2AClient()

# Dynamic discovery (flexible)
data_agent = a2a.discover(capability='run_analytics')

# Context automatically transferred
response = a2a.send_task(
    agent=data_agent,
    task='run_analytics',
    params={'customer_id': 'XYZ'}
    # conversation_id, history, auth handled automatically
)

# Agent B receives full context, continues seamlessly.
```

### A2A Adoption (October 2025)

**Google's A2A Partners** (50+ announced):

- **Enterprise Software**: Box, Deloitte, Elastic, MongoDB, Salesforce, ServiceNow, UiPath
- **Collaboration**: Cisco, Miro, Slack
- **Data & Analytics**: Databricks, Snowflake
- **DevOps**: Atlassian (Jira, Confluence), GitHub, GitLab
- **Security**: CrowdStrike, Palo Alto Networks

**A2A Status**:
- ✅ Google ADK: Native A2A support
- 🟡 AWS: A2A via Gateway service (roadmap)
- 🟡 Salesforce: A2A integration (roadmap)
- ⚠️ Microsoft: Custom connector needed (no native A2A yet)

**The bet**: A2A becomes the "SMTP for agents" — a standard protocol for agent communication across platforms.

---

## Unified Core Architecture: The Seven Layers

All agentic platforms provide these seven layers:

```text
╔══════════════════════════════════════════════════════════════════╗
║           UNIFIED AGENTIC PLATFORM ARCHITECTURE                  ║
║                  "The Cloud OS for Agents"                       ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ┌────────────────────────────────────────────────────────────┐ ║
║  │  LAYER 7: AGENT APPLICATIONS                               │ ║
║  │  Your custom agents, business logic, reasoning strategies  │ ║
║  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐      │ ║
║  │  │Customer  │ │  Sales   │ │   Data   │ │   Code   │      │ ║
║  │  │ Service  │ │Assistant │ │ Analyst  │ │  Helper  │      │ ║
║  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘      │ ║
║  └────────────────────────┬───────────────────────────────────┘ ║
║                           │                                     ║
║  ┌────────────────────────┴───────────────────────────────────┐ ║
║  │  LAYER 6: AGENT RUNTIME ENGINE                             │ ║
║  │  Execution, orchestration, lifecycle management            │ ║
║  │  ┌─────────────────┐  ┌─────────────────┐  ┌────────────┐ │ ║
║  │  │ Reasoning Loop  │  │ Multi-Agent     │  │ Workflow   │ │ ║
║  │  │ (ReAct, CoT)    │  │ Orchestration   │  │ Execution  │ │ ║
║  │  └─────────────────┘  └─────────────────┘  └────────────┘ │ ║
║  └────────────────────────┬───────────────────────────────────┘ ║
║                           │                                     ║
║  ┌────────────────────────┴───────────────────────────────────┐ ║
║  │  LAYER 5: TOOL GATEWAY                                     │ ║
║  │  Unified interface to external tools and services          │ ║
║  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │ ║
║  │  │ MCP Client  │  │ API Proxies │  │ SDK Wrappers│        │ ║
║  │  │ (standard)  │  │ (REST, etc.)│  │ (custom)    │        │ ║
║  │  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘        │ ║
║  │         │                │                │                │ ║
║  │  ┌──────┴────────────────┴────────────────┴──────┐         │ ║
║  │  │ Auth, Rate Limiting, Retries, Caching         │         │ ║
║  │  └───────────────────────────────────────────────┘         │ ║
║  └────────────────────────┬───────────────────────────────────┘ ║
║                           │                                     ║
║  ┌────────────────────────┴───────────────────────────────────┐ ║
║  │  LAYER 4: MEMORY SERVICE                                   │ ║
║  │  Persistent state, context, and knowledge                  │ ║
║  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │ ║
║  │  │ Short-Term  │  │ Long-Term   │  │ Semantic    │        │ ║
║  │  │ Memory      │  │ Memory      │  │ Memory      │        │ ║
║  │  │ (session)   │  │ (history)   │  │ (vector DB) │        │ ║
║  │  └─────────────┘  └─────────────┘  └─────────────┘        │ ║
║  └────────────────────────┬───────────────────────────────────┘ ║
║                           │                                     ║
║  ┌────────────────────────┴───────────────────────────────────┐ ║
║  │  LAYER 3: IDENTITY & ACCESS MANAGEMENT                     │ ║
║  │  Agent identity, permissions, and security                 │ ║
║  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │ ║
║  │  │ Agent ID    │  │ Permissions │  │ Audit Logs  │        │ ║
║  │  │ (who am I?) │  │ (what can   │  │ (what did   │        │ ║
║  │  │             │  │  I do?)     │  │  I do?)     │        │ ║
║  │  └─────────────┘  └─────────────┘  └─────────────┘        │ ║
║  └────────────────────────┬───────────────────────────────────┘ ║
║                           │                                     ║
║  ┌────────────────────────┴───────────────────────────────────┐ ║
║  │  LAYER 2: OBSERVABILITY                                    │ ║
║  │  Monitoring, debugging, and cost tracking                  │ ║
║  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │ ║
║  │  │ Reasoning   │  │ Distributed │  │ Cost        │        │ ║
║  │  │ Traces      │  │ Tracing     │  │ Tracking    │        │ ║
║  │  │ (why?)      │  │ (how?)      │  │ (how much?) │        │ ║
║  │  └─────────────┘  └─────────────┘  └─────────────┘        │ ║
║  └────────────────────────┬───────────────────────────────────┘ ║
║                           │                                     ║
║  ┌────────────────────────┴───────────────────────────────────┐ ║
║  │  LAYER 1: AGENT COMMUNICATION (A2A)                        │ ║
║  │  Agent-to-agent discovery, messaging, and coordination     │ ║
║  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │ ║
║  │  │ Discovery   │  │ Messaging   │  │ Context     │        │ ║
║  │  │ (who?)      │  │ (messages)  │  │ Transfer    │        │ ║
║  │  └─────────────┘  └─────────────┘  └─────────────┘        │ ║
║  └────────────────────────────────────────────────────────────┘ ║
║                                                                 ║
╚═════════════════════════════════════════════════════════════════╝
```

### Layer Breakdown

| Layer | Purpose | Example Components | Platform Examples |
|-------|---------|-------------------|------------------|
| **7. Applications** | Your agent logic | Custom agents, business rules | Your code |
| **6. Runtime Engine** | Execute agents | Reasoning loop, orchestration | Google Agent Engine, AWS Lambda |
| **5. Tool Gateway** | Connect to services | MCP client, API proxies | AWS Gateway, Google ADK tools |
| **4. Memory Service** | Store context | Vector DB, session state | Vertex AI Vector, Bedrock Memory |
| **3. Identity/Auth** | Secure access | Agent ID, permissions, audit | GCP IAM, AWS IAM, Entra ID |
| **2. Observability** | Monitor & debug | Traces, logs, cost tracking | Cloud Logging, CloudWatch |
| **1. A2A Communication** | Agent coordination | Discovery, messaging | A2A Protocol, custom |

**Key Insight**: Every platform provides these layers. The **difference** is:

- **How opinionated** (Salesforce: very; Google: flexible)
- **How integrated** (AWS: tight AWS coupling; Google: cross-cloud)
- **How mature** (Microsoft: years of production; Google: months)

---

## Detailed View: How a Request Flows

**Scenario**: User asks Customer Service agent: "What's the status of my order?"

```text
╔══════════════════════════════════════════════════════════════════╗
║                 REQUEST FLOW THROUGH PLATFORM                    ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  1. USER REQUEST                                                 ║
║  ┌──────────────────────────────────────────────────────────┐   ║
║  │ User: "What's the status of my order #12345?"           │   ║
║  └────────────────────────┬─────────────────────────────────┘   ║
║                           │                                      ║
║                           ▼                                      ║
║  2. AGENT APPLICATION (Layer 7)                                  ║
║  ┌──────────────────────────────────────────────────────────┐   ║
║  │ Customer Service Agent receives request                  │   ║
║  │ ─ Parses intent: "order status lookup"                   │   ║
║  │ ─ Identifies need: query order system                    │   ║
║  └────────────────────────┬─────────────────────────────────┘   ║
║                           │                                      ║
║                           ▼                                      ║
║  3. RUNTIME ENGINE (Layer 6)                                     ║
║  ┌──────────────────────────────────────────────────────────┐   ║
║  │ Reasoning Loop (ReAct):                                   │   ║
║  │ ─ Thought: "I need order data for #12345"                │   ║
║  │ ─ Action: Call tool "query_order_system"                 │   ║
║  │ ─ Observation: (wait for tool result)                    │   ║
║  └────────────────────────┬─────────────────────────────────┘   ║
║                           │                                      ║
║                           ▼                                      ║
║  4. IDENTITY CHECK (Layer 3)                                     ║
║  ┌──────────────────────────────────────────────────────────┐   ║
║  │ IAM Service:                                              │   ║
║  │ ─ Who is this agent? → customer_service_agent            │   ║
║  │ ─ Can it read orders? → Check permissions                │   ║
║  │ ─ Result: ✅ Allowed                                      │   ║
║  │ ─ Audit log: [2025-10-26 14:23:15] agent accessed orders│   ║
║  └────────────────────────┬─────────────────────────────────┘   ║
║                           │                                      ║
║                           ▼                                      ║
║  5. TOOL GATEWAY (Layer 5)                                       ║
║  ┌──────────────────────────────────────────────────────────┐   ║
║  │ MCP Client:                                               │   ║
║  │ ─ Discover: "query_order_system" → MCP Server: Orders    │   ║
║  │ ─ Call: mcp.call("query_order_system", {"order_id": ...})│   ║
║  │ ─ Handles: OAuth, rate limits, retries, caching          │   ║
║  └────────────────────────┬─────────────────────────────────┘   ║
║                           │                                      ║
║                           │ HTTP/JSON-RPC to Order System        ║
║                           │                                      ║
║  ┌────────────────────────▼─────────────────────────────────┐   ║
║  │ Order System API:                                         │   ║
║  │ ─ Query: SELECT * FROM orders WHERE id = 12345           │   ║
║  │ ─ Result: {status: "shipped", tracking: "UPS123"}        │   ║
║  └────────────────────────┬─────────────────────────────────┘   ║
║                           │                                      ║
║                           ▼                                      ║
║  6. MEMORY SERVICE (Layer 4)                                     ║
║  ┌──────────────────────────────────────────────────────────┐   ║
║  │ Store conversation context:                               │   ║
║  │ ─ User asked about order #12345                           │   ║
║  │ ─ System returned: "shipped, UPS123"                      │   ║
║  │ ─ Next query can reference this (e.g., "Where is it?")   │   ║
║  └────────────────────────┬─────────────────────────────────┘   ║
║                           │                                      ║
║                           ▼                                      ║
║  7. RUNTIME ENGINE (Layer 6) - Continued                         ║
║  ┌──────────────────────────────────────────────────────────┐   ║
║  │ Reasoning Loop:                                           │   ║
║  │ ─ Observation: Order #12345 is shipped, tracking UPS123  │   ║
║  │ ─ Thought: "I have the answer"                            │   ║
║  │ ─ Action: Respond to user                                │   ║
║  └────────────────────────┬─────────────────────────────────┘   ║
║                           │                                      ║
║                           ▼                                      ║
║  8. OBSERVABILITY (Layer 2)                                      ║
║  ┌──────────────────────────────────────────────────────────┐   ║
║  │ Logs captured:                                            │   ║
║  │ ─ Reasoning trace: intent → tool call → response         │   ║
║  │ ─ Distributed trace: latency breakdown                   │   ║
║  │ ─ Cost: 2000 LLM tokens ($0.02) + API calls ($0.001)     │   ║
║  └────────────────────────┬─────────────────────────────────┘   ║
║                           │                                      ║
║                           ▼                                      ║
║  9. AGENT RESPONSE                                               ║
║  ┌──────────────────────────────────────────────────────────┐   ║
║  │ Agent: "Your order #12345 has been shipped!              │   ║
║  │         Tracking: UPS123                                  │   ║
║  │         Estimated delivery: Tomorrow"                     │   ║
║  └────────────────────────┬─────────────────────────────────┘   ║
║                           │                                      ║
║                           ▼                                      ║
║  10. USER RECEIVES RESPONSE                                      ║
║  ┌──────────────────────────────────────────────────────────┐   ║
║  │ User sees answer in chat/UI                               │   ║
║  └──────────────────────────────────────────────────────────┘   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

TOTAL TIME: ~1-2 seconds
TOTAL COST: $0.021 (LLM + API calls)
VISIBILITY: Full trace, every step logged
```

### What the Platform Handled

**Without platform** (DIY):
- Your team builds: Authentication, rate limiting, retries, caching, logging, tracing, cost tracking
- Your code: ~1000+ lines of infrastructure glue

**With platform**:
- Platform handles: All infrastructure layers (1-6, except your agent logic)
- Your code: ~50 lines (agent logic only)

**The 20x productivity multiplier.**

---

## Summary: Protocols & Architecture

**MCP (Model Context Protocol)**:
- ✅ Standard tool integration (like USB-C)
- ✅ 100+ community servers
- ✅ Supported by AWS, Google, Salesforce, Claude

**A2A (Agent-to-Agent Protocol)**:
- ✅ Standard agent communication
- ✅ 50+ Google partners
- ✅ Discovery, context transfer, security built-in

**Unified Architecture**:
- 7 layers every platform provides
- Layer 7: Your agent logic
- Layers 1-6: Platform handles infrastructure

**Key Insight**: Platforms abstract complexity, just like operating systems did 60 years ago.

---

## Next: Real Implementation Guide

We've seen the architecture. Now let's **build** something.

In [Part 5](./05-implementation.md), we'll cover:
- Google ADK code example (verified, real APIs)
- AWS Bedrock code example (verified, real APIs)
- Microsoft Copilot Studio patterns
- Salesforce Agentforce examples
- Quick Wins Timeline (Week 1, 4, 12)
- Real metrics from deployments

Time to get hands-on.

[Continue to Part 5 →](./05-implementation.md)

---

[← Previous: Platforms Compared](./03-platforms-compared.md) | [Back to Index](./README.md) | [Next: Implementation Guide →](./05-implementation.md)
