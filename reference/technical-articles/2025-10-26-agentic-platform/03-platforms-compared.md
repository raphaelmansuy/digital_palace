# Part 3: The Four Major Platforms Compared

[← Previous: Why Platforms](./02-why-platforms.md) | [Back to Index](./README.md) | [Next: Protocols & Architecture →](./04-protocols-architecture.md)

---

## The Platform Landscape (October 2025)

Four major hyperscalers have launched production-grade agentic platforms:

1. **Google Vertex AI Agent Builder (ADK)** - Launched Q4 2024, A2A protocol leader
2. **AWS Bedrock AgentCore** - Announced re:Invent 2024, GA Q1 2025
3. **Microsoft Copilot Studio** - Evolution of Bot Framework, 160K+ customers
4. **Salesforce Agentforce** - Launched Dreamforce 2024, 1M+ requests processed

Each platform reflects its parent company's DNA. Let's compare them.

---

## Platform Comparison Matrix

### Core Capabilities

| Feature | Google ADK | AWS Bedrock AgentCore | Microsoft Copilot Studio | Salesforce Agentforce |
|---------|-----------|----------------------|--------------------------|----------------------|
| **PRIMARY MODEL** | Gemini 2.5 Flash (native) | Claude 4.5 Sonnet (default) | GPT-5 (latest, 2025-10-06) | Mix of models + Atlas |
| **MULTI-MODEL SUPPORT** | ✅ Any model via Vertex | ✅ Bedrock models | ✅ Azure AI + OpenAI | ⚠️ Limited (SaaS focus) |
| **PROTOCOL SUPPORT** | ✅ A2A (native) + MCP | ✅ MCP (gateway) | ⚠️ Custom connectors (1000+) | ✅ MCP + A2A (roadmap) |
| **TOOL ECOSYSTEM** | MCP servers + custom Python | AWS services + MCP + custom | Power Platform connectors | Apex code + MCP + APIs |
| **MEMORY** | Vector DB (Vertex AI) + custom | Memory service (managed) | M365 Graph + custom | CRM data + Data Cloud |
| **ORCHESTRATION** | LangGraph + AG2 + custom | Step Functions + custom | Low-code designer + copilot | Atlas Reasoning Engine |
| **IDENTITY/AUTH** | Google IAM + Workload Identity | AWS IAM + Amazon Verified Permissions | Entra ID (AAD) + M365 identity | Salesforce Org permissions |
| **OBSERVABILITY** | Cloud Logging + Trace | CloudWatch + Bedrock metrics | Application Insights + custom | Einstein Analytics + custom |
| **DEPLOYMENT** | GKE, Cloud Run, Vertex AI managed | Lambda, ECS, Fargate, EC2 | Azure Functions, AKS, VMs | Salesforce cloud (managed) |
| **PRICING MODEL** | Pay-per-use (LLM tokens) | Pay-per-use + managed services | Per-agent licensing | Per-conversation + usage |
| **IDEAL FOR** | GCP-native, multi-agent systems | AWS-native, enterprise compliance | M365-heavy orgs, low-code | CRM-centric businesses |
| **MATURITY** | 🟡 Early (Q4 2024) | 🟡 Early (Q1 2025) | 🟢 Mature (years) | 🟡 Early (Q4 2024) |

### Problems Solved by Each Platform

| Problem | Google ADK | AWS Bedrock | Microsoft Copilot | Salesforce Agentforce |
|---------|-----------|-------------|-------------------|----------------------|
| **Multi-agent coordination** | ✅ A2A native, discovery protocol | 🟡 Gateway service | ⚠️ Custom logic needed | 🟡 Roadmap feature |
| **Tool integration sprawl** | ✅ MCP + Python functions | ✅ MCP + AWS services | ✅ Power Platform connectors | ✅ MCP + Apex |
| **Enterprise security** | ✅ GCP IAM + Workload Identity | ✅ AWS IAM + Verified Permissions | ✅ Entra ID integration | ✅ Salesforce security model |
| **Cost optimization** | 🟡 Manual monitoring | ✅ Cost tracking in CloudWatch | 🟡 App Insights custom | 🟡 Einstein Analytics custom |
| **Observability** | 🟡 Cloud Logging | ✅ Full Bedrock metrics | 🟡 App Insights | 🟡 Einstein Analytics |
| **Memory management** | ✅ Vertex AI Vector DB | ✅ Managed memory service | ✅ M365 Graph | ✅ Data Cloud |
| **Cross-platform agents** | ✅ A2A protocol | 🟡 MCP gateway | ⚠️ M365-centric | ⚠️ CRM-centric |

**Legend**:
- ✅ Native, production-ready
- 🟡 Available but requires configuration
- ⚠️ Requires significant custom work

---

## Deep Dive: Each Platform's Unique Strengths

### 1. Google Vertex AI Agent Builder (ADK)

**DNA**: Google's research-first approach, strong on protocols and multi-agent systems.

**Unique Strengths**:

- **A2A Protocol Leadership**: Only platform with native Agent-to-Agent communication
- **Research Pedigree**: Built on Google DeepMind's agent research (see: Gemini models, AlphaGo)
- **Framework Flexibility**: Works with LangGraph, AG2, CrewAI, AutoGen
- **Gemini 2.5 Integration**: Native access to Google's latest multimodal models (Gemini 2.5 Pro, Flash, Flash-Lite)

**Sweet Spot**: Companies building **complex multi-agent systems** where agents need to discover each other, negotiate tasks, and coordinate autonomously.

**Example Deployment**:

```python
# Google ADK: A2A-native agent coordination
from google.adk.agents.llm_agent import Agent
from google.adk.protocols.a2a import A2AProtocol

# Agent 1: Sales Agent
sales_agent = Agent(
    name="sales_assistant",
    model="gemini-2.5-flash",
    tools=[crm_tool, email_tool],
    capabilities=["customer_lookup", "send_proposal"]
)

# Agent 2: Data Agent  
data_agent = Agent(
    name="data_analyst",
    model="gemini-2.5-flash",
    tools=[bigquery_tool, sheets_tool],
    capabilities=["run_analytics", "generate_report"]
)

# A2A Protocol: Agents discover and coordinate
a2a = A2AProtocol()
a2a.register(sales_agent)
a2a.register(data_agent)

# Sales agent can now discover and call data agent:
# "Get me analytics on customer XYZ"
# → Sales agent discovers data_agent has "run_analytics"
# → Sends A2A message with context
# → Data agent returns results
# → Sales agent continues with full context
```

**Problems It Solves Best**:
- ✅ Multi-agent orchestration across organizational boundaries
- ✅ Agent discovery (who can do what?)
- ✅ Cross-cloud agent communication (A2A works outside GCP)
- ✅ Research/experimental agent architectures

**Real Deployment**: *Google claims 50+ A2A partners (Box, Deloitte, Elastic, MongoDB, Salesforce, ServiceNow, UiPath).*

---

### 2. AWS Bedrock AgentCore

**DNA**: AWS's enterprise-first approach, strong on security and compliance.

**Unique Strengths**:

- **Seven Core Services**: Modular architecture (Runtime, Gateway, Memory, Identity, Observability, Code-interpreter, Browser-tool)
- **MCP Integration**: Gateway service makes MCP protocol first-class
- **AWS Ecosystem**: Native integration with S3, DynamoDB, Lambda, Step Functions
- **Enterprise Security**: AWS IAM, Verified Permissions, audit logging built-in

**Sweet Spot**: **AWS-native enterprises** needing bulletproof security, compliance, and deep integration with existing AWS services.

**Example Deployment**:

```python
# AWS Bedrock: MCP Gateway + IAM
import boto3

bedrock_agent = boto3.client('bedrock-agent')

# Create agent with MCP tool access via Gateway
response = bedrock_agent.create_agent(
    agentName='customer_support_agent',
    foundationModel='anthropic.claude-4-5-sonnet-20251022-v2:0',
    agentResourceRoleArn='arn:aws:iam::123456789:role/AgentRole',
    
    # MCP Gateway: Connect to MCP servers
    tools=[{
        'type': 'mcp',
        'mcpServer': {
            'serverUrl': 'https://mcp.example.com/salesforce',
            'authentication': {
                'type': 'IAM',  # ← AWS IAM for MCP auth
                'roleArn': 'arn:aws:iam::123456789:role/MCPRole'
            }
        }
    }],
    
    # Memory service: Managed by AWS
    memoryConfiguration={
        'enabledMemoryTypes': ['SESSION_SUMMARY'],
        'storageDays': 30
    },
    
    # Observability: CloudWatch integration
    guardrailConfiguration={
        'guardrailIdentifier': 'guardrail-xyz',
        'guardrailVersion': '1'
    }
)

# Identity: AWS Verified Permissions for fine-grained access
avp_client = boto3.client('verifiedpermissions')
avp_client.is_authorized(
    policyStoreId='ps-123',
    principal={'entityType': 'Agent', 'entityId': response['agentId']},
    action={'actionType': 'Action', 'actionId': 'ReadCustomerData'},
    resource={'entityType': 'CRM', 'entityId': 'salesforce'}
)
```

**Problems It Solves Best**:
- ✅ Enterprise compliance (HIPAA, SOC2, PCI-DSS)
- ✅ Fine-grained permissions (who can access what?)
- ✅ Cost tracking and budgets (CloudWatch metrics)
- ✅ Integration with existing AWS infrastructure

**Real Deployment**: *Epsilon case study - 30% reduction in ad performance analysis time, 20% increase in client campaign success rate, 8hrs/week saved per team.*

---

### 3. Microsoft Copilot Studio

**DNA**: Microsoft's productivity-first approach, strong on low-code and M365 integration.

**Unique Strengths**:

- **Low-Code + Pro-Code**: Visual designer for non-developers, full code access for pros
- **M365 Integration**: Native access to Teams, Outlook, SharePoint, OneDrive, Graph API
- **160,000+ Customers**: Most mature platform (evolution of Bot Framework)
- **Power Platform Connectors**: 1000+ pre-built integrations (Salesforce, SAP, etc.)

**Sweet Spot**: **M365-heavy enterprises** needing rapid deployment with low-code tools, or companies wanting non-developers to build agents.

**Example Deployment**:

```yaml
# Microsoft Copilot Studio: Low-code configuration
name: "HR Onboarding Assistant"
trigger:
  - type: "teams_message"
    keywords: ["onboarding", "new hire", "start date"]

flows:
  - name: "Create Onboarding Checklist"
    steps:
      - action: "microsoft.graph.getUser"
        inputs:
          userId: "@{trigger.sender.id}"
      - action: "sharepoint.createList"
        inputs:
          site: "HR Site"
          listName: "Onboarding - @{user.displayName}"
      - action: "teams.sendMessage"
        inputs:
          message: "Onboarding checklist created!"

memory:
  type: "m365_graph"
  scope: ["chat.history", "calendar", "files"]

identity:
  type: "entra_id"
  permissions: ["User.Read", "Sites.ReadWrite.All"]
```

**For Pro Developers** (same agent, C# code):

```csharp
// Copilot Studio: Pro-code approach
using Microsoft.Bot.Builder;
using Microsoft.Graph;

public class OnboardingCopilot : ActivityHandler
{
    private readonly GraphServiceClient _graphClient;
    
    protected override async Task OnMessageActivityAsync(
        ITurnContext<IMessageActivity> turnContext,
        CancellationToken cancellationToken)
    {
        var user = await _graphClient.Me.Request().GetAsync();
        
        // Create SharePoint list
        var list = await _graphClient
            .Sites["hr-site"]
            .Lists
            .Request()
            .AddAsync(new List { 
                DisplayName = $"Onboarding - {user.DisplayName}" 
            });
        
        await turnContext.SendActivityAsync(
            "Onboarding checklist created!",
            cancellationToken: cancellationToken);
    }
}
```

**Problems It Solves Best**:
- ✅ Rapid prototyping (low-code designer)
- ✅ M365 data access (Graph API)
- ✅ Enterprise user identity (Entra ID/AAD)
- ✅ Non-developer agent creation

**Real Deployment**: *160,000+ enterprise customers using Copilot Studio (Microsoft 2024 earnings call).*

---

### 4. Salesforce Agentforce

**DNA**: Salesforce's CRM-first approach, strong on customer data and deterministic reasoning.

**Unique Strengths**:

- **Atlas Reasoning Engine**: Hybrid deterministic + LLM (not pure LLM agents)
- **CRM Data Access**: Native to Salesforce Data Cloud (unified customer data)
- **AgentExchange Marketplace**: Pre-built agents for common CRM workflows
- **1M+ Requests**: Production-proven at scale (Salesforce's own usage)

**Sweet Spot**: **CRM-centric businesses** needing agents that act on customer data with high reliability (sales, service, marketing).

**Example Deployment**:

```apex
// Salesforce Agentforce: Apex code + Atlas Engine
public class CustomerRetentionAgent {
    
    @InvocableMethod(label='Identify At-Risk Customers')
    public static List<AgentResponse> identifyAtRiskCustomers(
        List<AgentRequest> requests
    ) {
        // Atlas Engine: Deterministic rules + LLM reasoning
        
        // Step 1: Deterministic query (fast, reliable)
        List<Account> accounts = [
            SELECT Id, Name, LastActivityDate, ARR__c
            FROM Account
            WHERE LastActivityDate < LAST_N_DAYS:60
              AND ARR__c > 100000
        ];
        
        // Step 2: LLM reasoning (context-aware)
        for (Account acc : accounts) {
            String prompt = buildRiskAssessmentPrompt(acc);
            String assessment = LLMService.analyze(prompt);
            
            // Step 3: Atlas decides action (deterministic routing)
            if (assessment.contains('high risk')) {
                createRetentionTask(acc);
                notifyAccountManager(acc);
            }
        }
        
        return buildAgentResponses(accounts);
    }
    
    // MCP Integration: Connect to external tools
    @future(callout=true)
    private static void notifyAccountManager(Account acc) {
        MCPConnector.send('slack', new Map<String, Object>{
            'channel': acc.AccountManager__r.SlackId__c,
            'message': 'Account ' + acc.Name + ' flagged as at-risk'
        });
    }
}
```

**Problems It Solves Best**:
- ✅ CRM workflows (sales, service, marketing)
- ✅ Deterministic + LLM hybrid (reliability)
- ✅ Customer data unification (Data Cloud)
- ✅ Pre-built CRM agents (AgentExchange)

**Real Deployment**: *1M+ support requests processed, data from Dreamforce 2024.*

---

## Framework Flexibility Spectrum

Platforms vary in how much control you have over agent architecture:

```text
FULLY MANAGED ←─────────────────────────────→ FULL CONTROL
(Opinionated)                                  (Flexible)

Salesforce        Microsoft        AWS            Google
Agentforce        Copilot         Bedrock         ADK
    │                │               │              │
    │                │               │              │
    ▼                ▼               ▼              ▼
                                                    
Atlas Engine      Low-code +      Modular         Framework
(fixed)           Pro-code        services        agnostic
                  (hybrid)        (compose)       (BYO)

Use when:         Use when:       Use when:       Use when:
- CRM-centric     - M365-heavy    - AWS-native    - Multi-agent
- Need            - Rapid         - Enterprise    - Research/
  reliability       prototyping     compliance      experimental
- Pre-built       - Low-code      - Cost          - Cross-cloud
  workflows         + custom        optimization
```

### Which Flexibility Level Do You Need?

**Choose Fully Managed (Salesforce)** if:
- You're building CRM workflows (sales, service, marketing)
- Reliability > flexibility (deterministic reasoning important)
- You want pre-built agents from marketplace

**Choose Hybrid (Microsoft)** if:
- You have both non-technical and technical teams
- You need rapid prototyping with option to go pro-code later
- M365 is your primary productivity suite

**Choose Composable (AWS)** if:
- You're AWS-native and need deep integration
- Enterprise compliance is critical (HIPAA, SOC2, etc.)
- You want to mix managed services with custom code

**Choose Flexible (Google)** if:
- You're building multi-agent systems
- You want to use any framework (LangGraph, AG2, CrewAI)
- Cross-platform agent communication is important (A2A)

---

## Real Deployments: What's Working

### Google ADK: Multi-Agent Retail System

**Company**: Global retailer (anonymous, reported at Google I/O 2024)

**Problem**: Customer service agents couldn't access inventory, shipping, and promotions systems simultaneously.

**Solution**: 3-agent system with A2A coordination:

```text
Agent 1: Customer Interface
├─ Handles customer queries
├─ Discovers relevant agents via A2A
└─ Orchestrates responses

Agent 2: Inventory Specialist  
├─ Queries warehouse systems
├─ Real-time stock levels
└─ Returns data to Agent 1 via A2A

Agent 3: Promotions Specialist
├─ Queries marketing systems
├─ Personalized offers
└─ Returns offers to Agent 1 via A2A
```

**Results**:
- 40% reduction in average handling time
- 3 agents coordinate autonomously (no hardcoded integrations)
- Agents deployed across GCP, AWS, on-prem (A2A works cross-cloud)

### AWS Bedrock: Epsilon Ad Campaign Optimization

**Company**: Epsilon (Publicis Groupe)

**Problem**: Manual ad performance analysis took days, limited campaign optimization speed.

**Solution**: Bedrock agent with MCP connectors to ad platforms (Google Ads, Meta Ads, analytics tools).

**Results** (from AWS re:Invent 2024 keynote):
- ✅ **30% reduction** in time to analyze ad performance
- ✅ **20% increase** in client campaign success rate
- ✅ **8 hours/week saved** per marketing team
- ✅ MCP Gateway handled auth/rate limits, team focused on agent logic

### Microsoft Copilot Studio: Vodafone Customer Service

**Company**: Vodafone (reported at Microsoft Build 2024)

**Problem**: Customer service agents manually searched across 10+ systems to resolve inquiries.

**Solution**: Copilot Studio agent integrated with CRM, billing, network systems via Power Platform connectors.

**Results**:
- 50% reduction in average resolution time
- Low-code designer allowed non-developers to iterate on agent flows
- Entra ID integration provided single sign-on across all systems

### Salesforce Agentforce: Salesforce's Own Support

**Company**: Salesforce (dogfooding)

**Problem**: 1M+ support cases per quarter, need to triage and route efficiently.

**Solution**: Agentforce agent with Atlas Reasoning Engine, integrated with Service Cloud.

**Results** (from Dreamforce 2024):
- ✅ **1M+ requests processed** in first 3 months
- ✅ **40-60% automated resolution** for common issues
- ✅ Atlas Engine hybrid approach: deterministic triage + LLM for complex reasoning

---

## Platform Selection Decision Tree

```text
START: Which platform should you choose?
│
├─ Are you 100% on AWS?
│  └─ YES → AWS Bedrock AgentCore
│      ├─ Strengths: IAM, compliance, cost tracking
│      └─ Best for: Enterprise, regulated industries
│
├─ Are you 100% on GCP?
│  └─ YES → Consider usage pattern:
│      ├─ Multi-agent systems? → Google ADK (A2A native)
│      ├─ Single agents? → Google ADK or Vertex AI Agents
│      └─ Best for: Research, multi-agent coordination
│
├─ Are you M365-heavy (Teams, SharePoint, etc.)?
│  └─ YES → Microsoft Copilot Studio
│      ├─ Strengths: M365 integration, low-code
│      └─ Best for: Productivity agents, rapid prototyping
│
├─ Are you Salesforce-centric (Sales Cloud, Service Cloud)?
│  └─ YES → Salesforce Agentforce
│      ├─ Strengths: CRM data, Atlas Engine, marketplace
│      └─ Best for: Sales/service/marketing workflows
│
└─ Multi-cloud or undecided?
   └─ Consider:
       ├─ Need cross-platform agents? → Google ADK (A2A)
       ├─ Need max flexibility? → Google ADK (framework agnostic)
       ├─ Need low-code option? → Microsoft Copilot Studio
       └─ Need CRM-first? → Salesforce Agentforce
```

---

## Pricing Comparison (Approximate, October 2025)

| Platform | Base Cost | Per-Agent Cost | LLM Cost | Enterprise Add-Ons |
|----------|-----------|----------------|----------|-------------------|
| **Google ADK** | $0 (pay-per-use) | $0 | Vertex AI pricing ($0.001-$0.01/1K tokens) | Support contracts |
| **AWS Bedrock** | $0 (pay-per-use) | $0 | Bedrock pricing ($0.003-$0.03/1K tokens) | AWS Enterprise Support |
| **Microsoft Copilot Studio** | $200/month base | $30/agent/month | Included (fair use) or Azure OpenAI pricing | Microsoft 365 E3/E5 licensing |
| **Salesforce Agentforce** | Included in Sales/Service Cloud | $2/conversation | Included (fair use) or Einstein pricing | Data Cloud add-on ($50K+/year) |

**Notes**:
- Google and AWS: Pure consumption pricing (pay only for what you use)
- Microsoft: Per-seat licensing model (familiar to M365 customers)
- Salesforce: Per-conversation pricing (aligns with CRM usage)

**Cost Optimization Tips**:
- **Caching**: All platforms support prompt caching (50-90% cost reduction for repeated queries)
- **Model selection**: Use smaller models (Gemini Flash, Claude Haiku) for simple tasks
- **Batch processing**: Run non-urgent tasks asynchronously
- **Observability**: Use platform metrics to identify expensive agents

---

## Summary: Which Platform Wins?

**Short answer**: It depends on your existing stack.

**Pragmatic answer (as of Oct 2025)**:

- **If AWS-native** → AWS Bedrock (best IAM, compliance, cost tracking)
- **If GCP-native** → Google ADK (A2A protocol, multi-agent)
- **If M365-heavy** → Microsoft Copilot Studio (low-code, M365 integration)
- **If Salesforce-centric** → Salesforce Agentforce (CRM workflows, Atlas Engine)
- **If multi-cloud** → Google ADK (A2A works cross-cloud) or build with MCP for portability

**The trend**: By 2027, expect convergence:
- All platforms will likely support MCP (tool integration standard)
- A2A protocol may become cross-platform standard (Google open-sourcing efforts)
- Observability and cost tracking will improve across all platforms

**The bet**: Pick the platform that aligns with your cloud strategy. Switching costs are high (vendor lock-in), so choose carefully.

---

## Next: Protocols & Architecture

We've compared platforms. Now let's understand the **plumbing** that makes them work:

In [Part 4](./04-protocols-architecture.md), we'll explore:
- **MCP (Model Context Protocol)**: The "USB-C for AI tools"
- **A2A (Agent-to-Agent Protocol)**: How agents discover and coordinate
- **Unified Core Architecture**: The seven layers every platform provides
- **Detailed architectural diagrams** for visual learners

[Continue to Part 4 →](./04-protocols-architecture.md)

---

[← Previous: Why Platforms](./02-why-platforms.md) | [Back to Index](./README.md) | [Next: Protocols & Architecture →](./04-protocols-architecture.md)
