# Part 3: The Five Platform Approaches Compared

[← Previous: Why Platforms](./02-why-platforms.md) | [Back to Index](./README.md) | [Next: Protocols & Architecture →](./04-protocols-architecture.md)

---

## The Platform Landscape (October 2025)

Five distinct platform approaches have emerged for building and deploying AI agents:

**Four US Hyperscaler Platforms** (Cloud-Native, Framework-Locked):

1. **Google Vertex AI Agent Builder (ADK)** - Launched Q4 2024, A2A protocol leader, GCP-native, production-ready
2. **AWS Bedrock AgentCore** - GA Q1 2025, AWS-native, MCP-first architecture, enterprise compliance
3. **Microsoft Copilot Studio** - Most mature (160K+ users), Azure/M365-native, low-code + pro-code
4. **Salesforce Agentforce** - Launched Q4 2024, CRM-native, deterministic reasoning engine

**One Sovereign Universal Runtime Platform** (Framework-Agnostic, Deploy-Anywhere):

5. **QuantaLogic** - Phase 1 (October 2025): EU sovereign platform with multi-model generative AI. Phase 2 (Q3 2026): Runs agents built with ADK/CrewAI/LangGraph/LangChain, multi-model (15+), deploy anywhere

Each platform reflects different strategic priorities: hyperscaler platforms prioritize ecosystem integration and convenience within their cloud; universal runtime platforms prioritize framework flexibility, deployment sovereignty, and multi-model choice.

Let's compare all five approaches.

---

## Platform Comparison Matrix

### Core Capabilities

| Feature | Google ADK | AWS Bedrock | Microsoft Copilot | Salesforce | **QuantaLogic** |
|---------|-----------|-------------|-------------------|------------|-----------------|
| **FRAMEWORK SUPPORT** | ⚠️ ADK only | ⚠️ Bedrock Agents only | ⚠️ Copilot Studio only | ⚠️ Agentforce only | ✅ **Phase 2: ADK, CrewAI, LangGraph, LangChain** |
| **PRIMARY MODEL** | Gemini 2.5 (native) | Claude 4.5 (default) | GPT-5 (latest) | Mix + Atlas | **Phase 1: Any (15+ models)** |
| **MULTI-MODEL** | ✅ Vertex models | ✅ Bedrock models | ✅ Azure AI + OpenAI | ⚠️ Limited | ✅ **Phase 1: Mistral, Claude, Gemini, GPT, local** |
| **PROTOCOL** | ✅ A2A (native) + MCP | ✅ MCP (gateway) | ⚠️ Custom (1000+) | 🟡 MCP + A2A (roadmap) | ✅ **Phase 1: MCP native, Phase 2: A2A roadmap** |
| **TOOL ECOSYSTEM** | MCP + Python | AWS + MCP | Power Platform | Apex + MCP | **Phase 1: MCP servers (community)** |
| **MEMORY** | Vertex AI Vector DB | Memory service | M365 Graph | CRM Data Cloud | **Phase 1: Vector DB (any)** |
| **ORCHESTRATION** | LangGraph + AG2 | Step Functions | Low-code designer | Atlas Engine | **Phase 2: Framework-agnostic runtime** |
| **IDENTITY/AUTH** | Google IAM | AWS IAM | Entra ID (AAD) | Salesforce Org | **Phase 1: Standard IAM + SSO** |
| **OBSERVABILITY** | Cloud Logging | CloudWatch | App Insights | Einstein Analytics | **Phase 1: OpenTelemetry-based** |
| **DEPLOYMENT** | GCP only | AWS only | Azure/M365 only | Salesforce cloud | ✅ **Phase 1: On-prem, EU cloud (OVHCloud, IONOS), SaaS** |
| **DATA SOVEREIGNTY** | ❌ US Cloud Act | ❌ US Cloud Act | ❌ US Cloud Act | ❌ US Cloud Act | ✅ **Phase 1: EU sovereign (GDPR/NIS2/DORA)** |
| **PRICING** | Pay-per-use (LLM) | Pay-per-use | Per-agent license | Per-conversation | **Phase 1: Plans €0-€29.99/user + LLM costs** |
| **IDEAL FOR** | GCP-native, multi-agent | AWS-native, compliance | M365-heavy, low-code | CRM-centric | **EU/regulated, multi-cloud, framework flexibility** |
| **MATURITY** | 🟡 Early (Q4 2024) | 🟡 Early (Q1 2025) | 🟢 Mature (years) | 🟡 Early (Q4 2024) | 🟡 **Phase 1: Early but production-ready (Oct 2025)** |

### Problems Solved by Each Platform

| Problem | Google ADK | AWS Bedrock | Microsoft Copilot | Salesforce | **QuantaLogic** |
|---------|-----------|-------------|-------------------|------------|-----------------|
| **Framework lock-in** | ❌ ADK only | ❌ Bedrock only | ❌ Copilot only | ❌ Agentforce only | ✅ **Universal runtime** |
| **Multi-agent coordination** | ✅ A2A native | 🟡 Gateway | ⚠️ Custom logic | 🟡 Roadmap | 🟡 **A2A roadmap** |
| **Tool integration sprawl** | ✅ MCP + Python | ✅ MCP + AWS | ✅ Power Platform | ✅ MCP + Apex | ✅ **MCP native** |
| **Enterprise security** | ✅ GCP IAM | ✅ AWS IAM | ✅ Entra ID | ✅ Salesforce | ✅ **Standard IAM** |
| **Data sovereignty** | ❌ US jurisdiction | ❌ US jurisdiction | ❌ US jurisdiction | ❌ US jurisdiction | ✅ **EU compliant** |
| **Cost optimization** | 🟡 Manual | ✅ CloudWatch | 🟡 App Insights | 🟡 Einstein | ✅ **Multi-model switching** |
| **Observability** | 🟡 Cloud Logging | ✅ Full metrics | 🟡 App Insights | 🟡 Einstein | ✅ **OpenTelemetry** |
| **Memory management** | ✅ Vertex Vector DB | ✅ Managed service | ✅ M365 Graph | ✅ Data Cloud | ✅ **Any vector DB** |
| **Cross-platform agents** | ✅ A2A protocol | 🟡 MCP gateway | ⚠️ M365-centric | ⚠️ CRM-centric | ✅ **Framework-agnostic** |
| **Vendor lock-in escape** | ❌ GCP-locked | ❌ AWS-locked | ❌ Azure-locked | ❌ SF-locked | ✅ **Deploy anywhere** |

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

**Real Deployment**: *AWS reports 50+ enterprise customers using Bedrock Agents for production AI agent systems. MCP Gateway enables integration with any tool via standard protocol.*

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

### 5. QuantaLogic (Sovereign Universal Runtime)

**DNA**: European tech sovereignty meets universal framework compatibility. "Kubernetes for AI agents."

**Phase Timeline**:
- **Phase 1 (October 2025 - LIVE)**: Sovereign AI generative platform with multi-model support, QAgent chat, workflow automation, EU deployments
- **Phase 2 (Q3 2026 - Roadmap)**: Universal agent runtime supporting multi-framework orchestration (ADK, CrewAI, LangGraph, LangChain, AutoGen)

**Phase 1 Unique Positioning (Live Now)**:

- **Multi-Model Generative**: 15+ LLMs (Mistral, Claude, Gemini, GPT, DeepSeek, local models)
- **Conversational AI**: QAgent - advanced chat interface with context management
- **Workflow Automation**: Visual workflow builder for AI processes
- **Deployment Options**: SaaS, on-premise, EU cloud (OVHCloud, IONOS), 100% EU data residency
- **EU Sovereign**: GDPR/NIS2/DORA compliant by design, no US Cloud Act exposure
- **Open Protocols**: MCP native support

**Phase 2 Roadmap (Q3 2026)**:

- **Universal Runtime**: Run agents built with Google ADK, CrewAI, LangGraph, LangChain, AutoGen
- **Framework Independence**: Teams use familiar frameworks, deploy via QuantaLogic
- **A2A Protocol Integration**: Multi-agent coordination (A2A standard from https://a2a-protocol.org/latest/)
- **Advanced Orchestration**: Multi-framework agent choreography

**Why It Exists**: Hyperscalers created framework lock-in + cloud lock-in + model lock-in. QuantaLogic breaks all three while maintaining sovereignty.

**Sweet Spot**: 
- **Phase 1**: EU/regulated enterprises needing sovereign generative AI with multi-model flexibility
- **Phase 2**: Companies with multi-framework teams AND data sovereignty requirements, or multi-cloud strategies

**Example Deployment - Phase 2 (Q3 2026 Roadmap) Multi-Framework Team**:

```yaml
# Team 1: Builds with Google ADK (familiar framework)
# team1-agent.py
from google.adk.agents import Agent

sales_agent = Agent(
    name="sales_assistant",
    model="gemini-2.5-flash",  # Will be overridden by Phase 2 runtime
    tools=[crm_tool, email_tool]
)

# Team 2: Builds with CrewAI (multi-agent)
# team2-crew.py
from crewai import Agent, Crew

analyst = Agent(
    role='Data Analyst',
    model='gpt-4',  # Will be overridden by Phase 2 runtime
    tools=[bigquery_tool]
)
crew = Crew(agents=[analyst])

# QuantaLogic Phase 2 Universal Runtime Deployment
# quantalogic-deploy.yaml
runtime: quantalogic/phase-2
deployment:
  region: eu-west-1  # OVHCloud Paris
  compliance: gdpr-strict
  
agents:
  - framework: google-adk
    source: ./team1-agent.py
    model: mistral-large-2  # EU sovereign model
    
  - framework: crewai
    source: ./team2-crew.py
    model: claude-3.5-sonnet  # Quality tasks
    fallback: mistral-large-2  # Cost optimization

# Result: Both teams use familiar frameworks
#         All agents deploy to EU cloud
#         Model flexibility per task
#         Zero cloud lock-in
#         A2A protocol enables cross-team coordination
```

**Phase 2 Cross-Framework Coordination (Roadmap)**:

```text
┌──────────────────────────────────────────────────┐
│  QuantaLogic Phase 2 Architecture (Q3 2026)      │
│                                                  │
│  ┌─────────┐         ┌──────────┐              │
│  │ Google  │  A2A    │  CrewAI  │              │
│  │  ADK    │◄──────►─│  Agent   │              │
│  │ Agent   │ Protocol│  (crew)  │              │
│  └─────────┘         └──────────┘              │
│       │                    │                    │
│       │                    │                    │
│  ┌────▼────────────────────▼─────────────┐     │
│  │  QuantaLogic Runtime Bridge (Phase 2)  │     │
│  │  ├─ Framework Translation              │     │
│  │  ├─ Shared Context Store               │     │
│  │  ├─ Model Routing (Mistral/Claude/GPT) │     │
│  │  ├─ EU Data Residency Enforcement      │     │
│  │  └─ A2A Protocol Coordination          │     │
│  └────────────────────────────────────────┘     │
│                                                  │
└──────────────────────────────────────────────────┘

ADK agent can hand off task to CrewAI agent via A2A
Both access same customer context
Both use EU-compliant models
```

**Phase 1 Strengths (October 2025 - Live)**:

- ✅ **Multi-Model Flexibility**: Switch between 15+ models (Mistral, Claude, Gemini, GPT, local) per task
- ✅ **Data Sovereignty**: 100% EU data residency, GDPR Article 48 compliant
- ✅ **Deployment Freedom**: On-prem, EU cloud (OVHCloud, IONOS), SaaS options
- ✅ **Cost Optimization**: Multi-model selection reduces LLM costs vs single-vendor
- ✅ **Conversational AI**: QAgent provides advanced chat with workflow integration

**Phase 2 Strengths (Q3 2026 - Roadmap)**:

- ✅ **Framework Independence**: Not locked to ADK/Bedrock/Copilot - use ANY framework
- ✅ **Cloud Independence**: Deploy on-prem, EU cloud, AWS, GCP, Azure, multi-cloud
- ✅ **Multi-Agent Coordination**: A2A protocol for agent-to-agent communication
- ✅ **No Vendor Lock-In**: Open protocols (MCP, A2A), portable agents

**Strategic Trade-Offs** (Honest Assessment):

| Dimension | QuantaLogic | Hyperscalers | Verdict |
|-----------|-------------|--------------|---------|
| **Ecosystem maturity** | 🟡 Growing (newer platform) | ✅ 160K customers (Microsoft) | Hyperscalers more mature |
| **Framework flexibility** | ✅ ADK/CrewAI/LangGraph/etc | ❌ Single framework only | QuantaLogic wins |
| **Data sovereignty** | ✅ EU compliant | ❌ US Cloud Act applies | QuantaLogic wins |
| **Deployment options** | ✅ Anywhere (on-prem/cloud) | ❌ Locked to one cloud | QuantaLogic wins |
| **Enterprise support** | 🟡 Growing | ✅ 24/7 global support | Hyperscalers more mature |
| **Pre-built integrations** | 🟡 MCP community | ✅ Thousands native | Hyperscalers have more |
| **Model choice** | ✅ 15+ models | ⚠️ Limited to cloud's models | QuantaLogic wins |
| **Cost** | ✅ 49% cheaper | ⚠️ Cloud markup | QuantaLogic wins |
| **Vendor lock-in risk** | ✅ None (portable) | ❌ High (cloud-locked) | QuantaLogic wins |

**When to Choose QuantaLogic**:

1. **EU/Regulated Industries**: Financial services (DORA), healthcare (GDPR), government (NIS2)
2. **Multi-Cloud Strategy**: Don't want to be locked to AWS/GCP/Azure
3. **Framework Flexibility**: Teams use different frameworks (ADK, CrewAI, LangGraph)
4. **Cost Optimization**: Need to switch models based on task complexity/cost
5. **Sovereignty Requirements**: Data MUST stay in EU, no US Cloud Act exposure
6. **Exit Strategy**: Need ability to move platforms without rewriting agents

**When Hyperscalers Might Be Better**:

1. **100% Cloud Committed**: Already all-in on AWS/GCP/Azure, no plans to change
2. **Maximum Ecosystem**: Need thousands of pre-built connectors (AWS has most)
3. **24/7 Global Support**: Need hyperscaler's massive support organization
4. **Marketplace**: Want pre-built agents from large marketplace (Salesforce AgentExchange)
5. **Sovereignty Not Critical**: US company, US customers, US data, no EU regulations

**Problems It Solves Best**:

- ✅ Framework lock-in (run ANY framework on one platform)
- ✅ Cloud lock-in (deploy anywhere, not locked to one cloud)
- ✅ Model lock-in (switch between 15+ models including EU sovereign options)
- ✅ Data sovereignty (EU compliant, GDPR/NIS2/DORA native)
- ✅ Cost optimization (multi-model = choose cheapest/best per task)
- ✅ Multi-cloud strategy (same agents deploy to AWS/GCP/Azure/on-prem)

**Real Example**: European Financial Services Company

```text
Challenge: Build AI agents for customer service + compliance
Requirements:
├─ DORA compliant (financial operational resilience)
├─ Data stays in EU (no US Cloud Act exposure)
├─ Backend team knows Google ADK
├─ Data team prefers LangGraph
├─ Need to optimize costs (mix of model quality/price)

Solution: QuantaLogic Universal Runtime
├─ Backend team: Builds agents with Google ADK (familiar)
├─ Data team: Builds agents with LangGraph (preferred)
├─ Deployment: OVHCloud Paris (EU sovereign)
├─ Models:
│   ├─ Mistral Large: Sensitive customer data (EU model)
│   ├─ Claude 3.5: Complex reasoning tasks (quality)
│   └─ Local Llama 3: Internal docs (no external calls)
├─ Cost: $822K over 3 years (vs $1.62M hyperscaler)
└─ Compliance: DORA ✅, GDPR ✅, NIS2 ✅

Result: Framework flexibility + EU sovereignty + cost savings
        No lock-in: Can switch clouds or models anytime
```

---

## Framework Flexibility Spectrum

Platforms vary in how much control you have over agent architecture and deployment:

```text
FULLY MANAGED ←────────────────────────────────────────────→ MAXIMUM FLEXIBILITY
(Opinionated)                                                (Framework-agnostic)

Salesforce      Microsoft      AWS           Google          QuantaLogic
Agentforce      Copilot       Bedrock        ADK            (Universal)
    │              │             │              │                 │
    │              │             │              │                 │
    ▼              ▼             ▼              ▼                 ▼
                                                               
Atlas Engine    Low-code +    Modular        Framework        ANY Framework
(fixed)         Pro-code      services       agnostic         (ADK, CrewAI,
                (hybrid)      (compose)      (BYO)            LangGraph, etc)
                                                               
Deploy:         Deploy:       Deploy:        Deploy:          Deploy:
Salesforce      Azure/M365    AWS only       GCP only         ANYWHERE
cloud only      only                                          (on-prem, EU,
                                                              multi-cloud)

Use when:       Use when:     Use when:      Use when:        Use when:
- CRM-centric   - M365-heavy  - AWS-native   - Multi-agent    - EU sovereign
- Need          - Rapid       - Enterprise   - Research/      - Framework
  reliability     prototyping   compliance     experimental     flexibility
- Pre-built     - Low-code    - Cost         - Cross-cloud    - Multi-model
  workflows       + custom      optimization                    - No lock-in
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

**Choose Universal Runtime (QuantaLogic)** if:

- **EU sovereignty is non-negotiable** (GDPR, NIS2, DORA compliance)
- **Framework flexibility matters** (want to use ADK today, CrewAI tomorrow)
- **Multi-cloud strategy** (don't want to be locked to one cloud)
- **Model flexibility** (want to switch between Mistral/Claude/Gemini/GPT per task)
- **Deploy anywhere** (SaaS for dev, on-prem for production, EU cloud for compliance)
- **No vendor lock-in** (need exit strategy built-in)

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
├─ Do you have EU data sovereignty requirements?
│  └─ YES → Is sovereignty CRITICAL (regulated industry)?
│      ├─ YES → QuantaLogic (EU sovereign, DORA/GDPR/NIS2)
│      └─ NO → Multi-cloud option (Google ADK + QuantaLogic)
│
├─ Do you need framework flexibility (ADK, CrewAI, LangGraph)?
│  └─ YES → Do you want to avoid vendor lock-in?
│      ├─ YES → QuantaLogic (universal runtime)
│      └─ NO → Build with framework, pick cloud later
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
       ├─ Need EU sovereignty? → QuantaLogic (GDPR/NIS2/DORA)
       ├─ Need framework flexibility? → QuantaLogic (ADK/CrewAI/LangGraph)
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
| **QuantaLogic** | From $500/month (SaaS) | Included | Multi-model ($0.001-$0.02/1K tokens) | EU cloud deployment, on-premise |

**Notes**:
- Google and AWS: Pure consumption pricing (pay only for what you use)
- Microsoft: Per-seat licensing model (familiar to M365 customers)
- Salesforce: Per-conversation pricing (aligns with CRM usage)
- QuantaLogic: Predictable pricing, multi-model flexibility (Mistral/Claude/GPT/local)

**3-Year TCO Example** (500 knowledge workers, 8 agents/day):
- **DIY on hyperscaler**: $5.67M (infra + ops + LLM costs)
- **Hyperscaler platform** (AWS/GCP/Azure): $1.62M (platform fees + LLM)
- **QuantaLogic on EU cloud**: $822K (49% cheaper, multi-model optimization)

**Cost Optimization Tips**:
- **Caching**: All platforms support prompt caching (50-90% cost reduction for repeated queries)
- **Model selection**: Use smaller models (Gemini Flash, Claude Haiku, Mistral Small) for simple tasks
- **Batch processing**: Run non-urgent tasks asynchronously
- **Observability**: Use platform metrics to identify expensive agents
- **Multi-model strategy**: Use QuantaLogic to route tasks to cheapest/best model per task

---

## Summary: Which Platform Wins?

**Short answer**: It depends on your priorities—cloud commitment, data sovereignty, or framework flexibility.

**Pragmatic answer (as of Oct 2025)**:

- **If AWS-native** → AWS Bedrock (best IAM, compliance, cost tracking)
- **If GCP-native** → Google ADK (A2A protocol, multi-agent)
- **If M365-heavy** → Microsoft Copilot Studio (low-code, M365 integration)
- **If Salesforce-centric** → Salesforce Agentforce (CRM workflows, Atlas Engine)
- **If EU sovereignty required** → QuantaLogic (GDPR/NIS2/DORA, EU cloud/on-premise)
- **If framework flexibility needed** → QuantaLogic (runs ADK/CrewAI/LangGraph/LangChain)
- **If multi-cloud strategy** → QuantaLogic (deploy anywhere) or Google ADK (A2A cross-cloud)

**The Universal Runtime Case**:

Choose QuantaLogic if you need:
1. **Framework independence**: Teams using different frameworks (ADK, CrewAI, LangGraph)
2. **Cloud independence**: Deploy on-prem, EU cloud, or multi-cloud without lock-in
3. **Model independence**: Switch between 15+ models (Mistral, Claude, GPT, local) per task
4. **Data sovereignty**: EU data residency required (financial services, healthcare, government)
5. **Cost optimization**: Multi-model flexibility = 49% cheaper than hyperscaler lock-in

**The Hyperscaler Case**:

Choose a hyperscaler if you:
1. **100% committed** to one cloud (AWS/GCP/Azure) with no plans to change
2. **Need maximum ecosystem**: Thousands of pre-built connectors (AWS has most)
3. **Want low-code rapid prototyping**: Microsoft Copilot Studio (M365 integration)
4. **Are CRM-first**: Salesforce Agentforce (Sales/Service Cloud workflows)
5. **Sovereignty not critical**: US company, US customers, US data

**The trend**: By 2027, expect convergence:
- All platforms will likely support MCP (tool integration standard)
- A2A protocol may become cross-platform standard (Google open-sourcing efforts)
- Universal runtimes may support more frameworks (QuantaLogic expanding)
- Observability and cost tracking will improve across all platforms

**The strategic choice**: 

- **Lock-in trade-off**: Hyperscalers offer mature ecosystems BUT lock you to their cloud/framework/models
- **Sovereignty trade-off**: QuantaLogic offers EU compliance BUT newer platform, smaller ecosystem
- **Framework trade-off**: Universal runtimes offer flexibility BUT hyperscalers have more mature tooling

**The bet**: 

Pick the platform that aligns with your **non-negotiables**:
- Non-negotiable cloud commitment? → Choose that cloud's platform
- Non-negotiable EU sovereignty? → Choose QuantaLogic
- Non-negotiable framework flexibility? → Choose QuantaLogic or Google ADK
- Non-negotiable CRM integration? → Choose Salesforce

Switching costs are high (vendor lock-in), so choose carefully based on long-term strategy.

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

*Written by [Raphaël Mansuy](https://www.linkedin.com/in/raphaelmansuy/)*

