# Part 7: Reality Check & Limitations

[← Previous: Implementation Guide](./06-implementation.md) | [Back to Index](./README.md) | [Next: Path Forward →](./08-path-forward.md)

---

## The Honest Assessment

We've covered the vision, the platforms, the architectures, and the code. Now let's talk about **reality**.

Agentic platforms are powerful but **not magic**. Here's what's working, what's not, and what you need to know before betting your infrastructure on them.

---

## ✅ What's Working Well (October 2025)

### 1. Simple Tool Integrations

**Status**: ✅ **Production-ready**

**What works**:

- MCP protocol makes tool connections straightforward
- 100+ pre-built MCP servers (Salesforce, Slack, GitHub, databases)
- Platforms handle OAuth, rate limiting, retries automatically

**Real example**: Epsilon (AWS Bedrock)

- Connected to Google Ads, Meta Ads, analytics platforms via MCP
- **30% time reduction** in ad performance analysis
- No custom integration code needed

**Recommendation**: ✅ **Use platforms for tool integration**. This is their core strength.

---

### 2. Conversational Interfaces

**Status**: ✅ **Production-ready**

**What works**:

- Natural language queries work reliably for well-defined domains
- Memory management handles multi-turn conversations
- Context retention across sessions (days to weeks)

**Real example**: Vodafone (Microsoft Copilot Studio)

- Customer service agents query 10+ systems conversationally
- **50% reduction** in resolution time
- M365 Graph provides seamless context across Teams, SharePoint

**Recommendation**: ✅ **Use platforms for customer-facing or internal chatbots** where the domain is well-scoped.

---

### 3. Observability & Debugging

**Status**: 🟡 **Good, but improving**

**What works**:

- Reasoning traces show agent decision paths
- Distributed tracing tracks requests across services
- Cost tracking shows per-query expenses

**What needs work**:

- Non-deterministic behavior makes reproducing bugs hard
- "Why did the agent do that?" still requires manual trace analysis
- Drift detection (agent behavior changing over time) is manual

**Real example**: AWS Bedrock

- CloudWatch metrics show agent latency, error rates, token usage
- But debugging "why did agent call wrong tool?" requires manual trace reading

**Recommendation**: 🟡 **Use platform observability**, but expect to build custom dashboards for complex debugging.

---

### 4. Enterprise Security

**Status**: ✅ **Production-ready** (with caveats)

**What works**:

- IAM integration (Google Cloud IAM, AWS IAM, Entra ID)
- Audit logging (every agent action logged)
- Guardrails (PII filters, content moderation)

**What needs work**:

- Fine-grained permissions across agents are complex
- "Agent A should trust Agent B" authorization is immature
- Cross-platform security (agents on GCP + AWS) requires custom work

**Real example**: Financial services company (AWS Bedrock)

- Compliance agent with strict IAM policies
- Guardrails block PII leakage
- But cross-agent permissions required custom Verified Permissions policies

**Recommendation**: ✅ **Use platform security for single-cloud deployments**. Cross-cloud requires additional work.

---

## ⚠️ What's Not Working Yet (October 2025)

### 1. Multi-Agent Coordination at Scale

**Status**: ⚠️ **Early days**

**The problem**:

- A2A protocol works for 2-3 agents
- 10+ agents = complex orchestration challenges
- "Who should handle this request?" discovery is slow or manual
- Circular dependencies (Agent A waits for B, B waits for C, C waits for A)

**Real pain point**:

> "We built 8 agents for different departments. When a customer query spans multiple domains, the agents don't know who should coordinate. We hardcoded the orchestration logic."
>
> — Engineering lead, Fortune 500

**Current state**:

- Google A2A: Works for simple handoffs, not complex workflows
- AWS, Microsoft, Salesforce: No standard multi-agent protocol

**Recommendation**: ⚠️ **Start with 1-3 agents**. Multi-agent (10+) requires custom orchestration layer.

---

### 2. Complex Reasoning (>5 steps)

**Status**: ⚠️ **Hit-or-miss**

**The problem**:

- Simple tasks (1-2 tool calls): 85-95% success
- Complex tasks (5+ tool calls, branching logic): 40-70% success
- Agent "forgets" intermediate steps in long reasoning chains
- Backtracking ("that didn't work, try a different approach") is unreliable

**Example failure mode**:

```text
Task: "Find all customers at risk of churning and create retention plan"

Agent reasoning:
1. Query CRM for customers with low engagement ✅
2. Fetch purchase history for each customer ✅
3. Calculate churn risk score ✅
4. Generate personalized retention offers ✅
5. Create tasks for sales team ❌ (Agent forgot context)
6. Send email notifications ❌ (Agent skipped step)

Success rate: 4/6 steps = 67%
```

**Why it fails**:

- Long context windows (128K+ tokens) don't prevent "attention drift"
- No explicit state machine for multi-step workflows
- Error recovery requires starting over

**Recommendation**: ⚠️ **Keep agent tasks simple (1-3 steps)**. For complex workflows, use deterministic orchestration (Step Functions, Temporal) + agents for reasoning.

---

### 3. Reliability & Production Incidents

**Status**: ⚠️ **Improving, but immature**

**The challenges**:

**LLM API Outages**:

- Claude 3.5 outage (August 2024): 4 hours
- GPT-4 rate limits (common during high demand)
- No multi-model failover built into platforms

**Non-Deterministic Failures**:

- Same query, different result (temperature >0)
- "Agent worked yesterday, fails today" (model updates)
- Hard to write traditional unit tests

**Cost Spikes**:

- Agent stuck in reasoning loop: $10K → $50K/month
- No circuit breakers for runaway token usage
- Manual intervention required to catch spikes

**Real incident**:

> "Our data agent had a bug: infinite reasoning loop. Took 3 days to notice because observability doesn't alert on 'reasoning loop detected.' Cost: $127K in one week."
>
> — CTO, Marketing SaaS

**Recommendation**: ⚠️ **Set budget alerts**, monitor token usage daily, implement timeouts for long-running agents.

---

### 4. Cross-Platform Agents

**Status**: ⚠️ **Fragmented**

**The problem**:

- Agent on GCP needs to talk to agent on AWS
- No standard protocol (A2A only works within Google ecosystem currently)
- Authentication across clouds is custom (Workload Identity Federation, etc.)

**Example**:

- Company has agents on Google ADK (GCP) + Microsoft Copilot (Azure)
- Agents can't discover each other
- Custom REST APIs + manual authentication required

**Current state**:

- Google pushing A2A as cross-platform standard
- AWS, Microsoft don't support A2A yet
- MCP works cross-platform for tools, not agents

**Recommendation**: ⚠️ **Pick one platform** if you need multi-agent coordination. Cross-platform agents require significant custom work.

---

### 5. Vendor Lock-In

**Status**: ⚠️ **Real concern**

**The problem**:

- Agent code is portable (Python, C#, Apex)
- Platform integrations are **not** portable:
  - IAM policies (GCP ≠ AWS ≠ Azure)
  - Observability (Cloud Logging ≠ CloudWatch ≠ App Insights)
  - Memory services (Vertex AI Vector ≠ Bedrock Memory)
  - A2A protocol (Google-only)

**Migration cost**:

- Rewriting IAM policies: 2-4 weeks
- Re-integrating tools: 1-2 weeks per tool
- Testing in new environment: 4-8 weeks

**Example**:

> "We built on AWS Bedrock. AWS changed pricing (hypothetical). Migrating to Google ADK would take 3-6 months. We're locked in."
>
> — Platform Engineer

**Recommendation**: ⚠️ **Choose your platform carefully**. Switching costs are high. Use MCP for tools (portable), but accept platform lock-in for runtime/memory/IAM.

---

## 🟡 Gray Areas (Depends on Use Case)

### 1. Cost vs Build-Your-Own

**When platforms are cheaper**:

- Small-scale (< 10,000 queries/day)
- Simple use cases (1-3 agents, 5-10 tools)
- Time to market is critical (weeks vs months)

**When DIY might be cheaper**:

- Large-scale (>100,000 queries/day) where per-query cost adds up
- Highly custom workflows (platforms constrain you)
- Security requirements platform can't meet

**Example cost comparison (30K queries/day)**:

| Approach                    | Initial Cost | Monthly Cost       | Total (1 year) |
| --------------------------- | ------------ | ------------------ | -------------- |
| **Google ADK (platform)**   | $45K setup   | $1,260 LLM + infra | $60K           |
| **AWS Bedrock (platform)**  | $45K setup   | $9,450 LLM + infra | $158K          |
| **DIY (LangGraph + infra)** | $2.8M build  | $945K ops          | $4.6M          |

**Verdict**: Platforms are cheaper for 95% of companies. Only at massive scale (millions of queries/day) does DIY make financial sense.

---

### 2. Accuracy vs Deterministic Systems

**When agents excel**:

- Ambiguous user queries ("Find customers who might churn")
- Natural language interfaces
- Context-aware responses (using conversation history)

**When deterministic systems excel**:

- Mission-critical workflows (financial transactions, healthcare)
- Compliance requirements (must explain every decision)
- Tasks requiring 99%+ accuracy

**Hybrid approach** (Salesforce Agentforce Atlas Engine):

- Deterministic rules for routing, scoring, triage
- LLM for reasoning, summarization, personalization

**Example**: Lead qualification

- Deterministic: Score based on company size, revenue, industry
- LLM: "Why is this lead high-quality?" narrative
- Result: Reliable + intelligent

**Recommendation**: 🟡 **Use hybrid** (deterministic + LLM) for production systems. Pure LLM agents for internal tools or non-critical workflows.

---

## Decision Framework: Should You Use a Platform?

### ✅ Use a platform if:

1. **Tool integration is your main pain**: ✅ MCP solves this elegantly
2. **You're on one cloud**: ✅ Platform integrates seamlessly with your stack
3. **Speed to market matters**: ✅ Weeks vs months
4. **You want to focus on agent logic**: ✅ Platform handles infrastructure
5. **Your use case is conversational**: ✅ Chatbots, Q&A, search

### ⚠️ Think twice if:

1. **Multi-agent coordination at scale**: ⚠️ Still immature (Oct 2025)
2. **Complex reasoning workflows**: ⚠️ Success rates 40-70%
3. **Cross-platform agents**: ⚠️ Requires custom work
4. **Mission-critical, must be deterministic**: ⚠️ Use hybrid approach
5. **Massive scale (millions of queries/day)**: ⚠️ Cost may favor DIY

### ❌ Don't use a platform if:

1. **You're in research/experimental phase**: ❌ Frameworks (LangGraph, AG2) give more control
2. **You need full control over every layer**: ❌ Platforms abstract too much
3. **Your use case doesn't fit platform model**: ❌ (e.g., batch processing, edge deployment)

---

## Real Success Rates (October 2025)

| Use Case                 | Complexity | Success Rate | Notes                             |
| ------------------------ | ---------- | ------------ | --------------------------------- |
| **CRM Lookup**           | Simple     | 90-95%       | Single tool call, deterministic   |
| **Customer Support**     | Medium     | 75-85%       | 2-3 tool calls, context-aware     |
| **Data Analysis**        | Medium     | 70-80%       | Query + reasoning + visualization |
| **Lead Qualification**   | Medium     | 60-75%       | Hybrid deterministic + LLM        |
| **Multi-Agent Workflow** | Complex    | 40-70%       | 5+ steps, coordination required   |
| **Code Generation**      | Complex    | 50-60%       | Requires validation + testing     |

**Key insight**: Success rate drops with:

- Task complexity (more steps = lower success)
- Ambiguity (clear instructions = higher success)
- Domain breadth (narrow domain = higher accuracy)

---

## Build vs Buy Decision Matrix

```text
╔══════════════════════════════════════════════════════════════════╗
║                  BUILD vs BUY DECISION MATRIX                    ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  YOUR SITUATION              RECOMMENDATION                      ║
║  ───────────────────────────────────────────────────────────     ║
║                                                                  ║
║  Startup, <50 people         → BUY (Platform)                    ║
║  Time to market critical     → Focus on product, not infra       ║
║                                                                  ║
║  Mid-Market, 500-5K people   → BUY (Platform)                    ║
║  Standard use cases          → Unless massive scale              ║
║                                                                  ║
║  Enterprise, >10K people     → BUY (Platform) initially          ║
║  Existing cloud investment   → Leverage cloud-native platform    ║
║                                                                  ║
║  AI-First Company            → BUILD (Custom)                    ║
║  Agents are core product     → Need full control, optimization   ║
║                                                                  ║
║  Research Lab                → BUILD (Frameworks)                ║
║  Experimental architectures  → LangGraph, AG2, CrewAI            ║
║                                                                  ║
║  Regulated Industry          → BUY (with audit)                  ║
║  Compliance requirements     → Platform security + custom guard  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## What to Expect: 90-Day Reality Check

### Week 1-4: Honeymoon Phase

**What happens**:

- ✅ POC works great (80-90% success)
- ✅ Stakeholders are excited
- ✅ "This is easy! Why didn't we do this earlier?"

**Why it's misleading**:

- POC uses simple queries (cherry-picked)
- Small scale (no cost or performance issues yet)
- No edge cases discovered

### Week 5-8: Reality Hits

**What happens**:

- ⚠️ Edge cases appear (success rate drops to 60-70%)
- ⚠️ Cost spikes ($100/month → $1,000/month)
- ⚠️ "Agent did something weird" debugging begins
- ⚠️ "Can we add just one more agent?" complexity explosion

**Common issues**:

- Agent ignores instructions
- Tool calls fail with cryptic errors
- Context loss in long conversations
- Latency spikes during peak usage

### Week 9-12: Production Hardening

**What happens**:

- 🛠️ Implement guardrails and error handling
- 🛠️ Optimize prompts based on failure analysis
- 🛠️ Set up monitoring and alerting
- 🛠️ Add circuit breakers for runaway costs

**Stabilization**:

- Success rate: 70-85% (acceptable)
- Cost: Optimized via caching, model selection
- Team: Confident in debugging and iteration

**Key lesson**: **Expect 2-3 months of iteration** before production-ready.

---

## Summary: Honest Recommendations

**✅ What platforms do well (Oct 2025)**:

1. Tool integration (MCP)
2. Conversational interfaces
3. Observability & debugging
4. Enterprise security (single-cloud)

**⚠️ What platforms don't do well yet**:

1. Multi-agent coordination at scale (10+ agents)
2. Complex reasoning (5+ steps)
3. Production reliability (non-deterministic failures)
4. Cross-platform agents
5. Vendor lock-in (real concern)

**🟡 Gray areas**:

1. Cost (cheaper for most, but not all)
2. Accuracy (good for conversational, not mission-critical)

**Pragmatic advice**:

- Start with platforms for 95% of use cases
- Keep tasks simple (1-3 steps)
- Plan for 2-3 months of iteration
- Accept some vendor lock-in
- Use hybrid (deterministic + LLM) for critical workflows

---

## 🆕 QuantaLogic Universal Runtime: Maturity Assessment

### Honest Framework Support Status (October 2025)

**Status**: 🟡 **Emerging Platform - Growing Ecosystem**

QuantaLogic's universal runtime positioning is compelling, but it's important to understand where it stands vs hyperscalers:

#### ✅ What's Working Well

**1. Framework Translation (Core Value Proposition)**:
- ✅ Google ADK support: Production-ready
- ✅ CrewAI support: Production-ready
- ✅ LangGraph support: Beta (working, improving)
- ✅ LangChain support: Beta
- 🟡 AutoGen support: Roadmap (not yet available)

**Verdict**: The core promise (run agents from different frameworks) **is real** for the major frameworks. This is QuantaLogic's key differentiation.

**2. EU Sovereign Deployment**:
- ✅ OVHCloud integration: Production
- ✅ IONOS integration: Production
- ✅ GDPR/NIS2/DORA compliance: Certified
- ✅ Data residency enforcement: Automatic

**Verdict**: This is QuantaLogic's **strongest feature**. If EU sovereignty is required, this is the only platform that delivers it natively.

**3. Multi-Model Routing**:
- ✅ Mistral models: Native support (EU partner)
- ✅ Claude models: Production
- ✅ OpenAI models: Production
- ✅ Gemini models: Production
- ✅ Local models (Llama, etc.): Production

**Verdict**: Multi-model flexibility **works as advertised**. Cost savings (49%) are real when you can choose optimal model per task.

#### ⚠️ What's Still Maturing

**1. Ecosystem Size**:
- Hyperscalers: 50K-160K customers, thousands of pre-built integrations
- QuantaLogic: ~500 customers (estimate), ~50 MCP connectors

**Reality**: Smaller ecosystem means:
- Fewer pre-built connectors (rely on MCP community)
- Smaller community for troubleshooting
- Less mature third-party tooling

**Mitigation**: MCP protocol means QuantaLogic can use ANY MCP server from the community (100+). You're not limited to QuantaLogic-specific integrations.

**2. Framework Translation Overhead**:
- Google ADK native on GCP: <10ms overhead
- Google ADK on QuantaLogic: 30-50ms framework translation

**Reality**: Framework translation adds 30-50ms latency. For most use cases (1-5s total), this is <5% overhead. For latency-critical apps (<100ms), this matters.

**Recommendation**: ✅ Acceptable for conversational agents, support bots, data analysis. ⚠️ Consider native platform for ultra-low-latency use cases.

**3. Cross-Framework Coordination**:
- Single-framework agents: Production-ready
- Cross-framework handoffs (ADK → CrewAI): Beta (works, but limited testing)
- Complex multi-framework orchestration: Roadmap

**Reality**: Running ADK + CrewAI + LangGraph agents on same platform **works**. Sophisticated cross-framework orchestration (ADK agent dynamically discovering CrewAI agent capabilities) is still early.

**Recommendation**: ✅ Use for independent agents from different frameworks. 🟡 Keep cross-framework handoffs simple (explicit, not dynamic discovery).

**4. Enterprise Support**:
- Hyperscalers: 24/7 global support, SLAs, dedicated TAMs
- QuantaLogic: Business hours support (EU timezone), growing support org

**Reality**: Smaller company = smaller support org. Response times are good, but not 24/7 global coverage (yet).

**Recommendation**: ✅ Fine for EU companies in EU timezones. ⚠️ Global 24/7 companies may want hyperscaler support.

#### 🔴 What's Not Yet Available

**1. Some Frameworks on Roadmap**:
- ❌ AutoGen (Microsoft): Roadmap (Q3 2026)
- ❌ Haystack (deepset): Roadmap (Q3 2026)
- ❌ Rasa: Not planned (niche framework)

**Reality**: QuantaLogic Phase 2 (Q3 2026) will add AutoGen and Haystack support for multi-framework teams.

**2. Some Cloud-Specific Features**:
- ❌ AWS-specific services (Step Functions, EventBridge): Not integrated
- ❌ GCP-specific services (Cloud Tasks, Pub/Sub): Not integrated
- ❌ Azure-specific services (Logic Apps, Service Bus): Not integrated

**Reality**: QuantaLogic is cloud-agnostic = doesn't integrate cloud-specific orchestration services. You use Kubernetes-native solutions instead.

**Mitigation**: Use cloud-agnostic alternatives (Temporal, Argo Workflows, Kubernetes Jobs).

**3. Hyperscaler-Scale Marketplace**:
- AWS: 10K+ ready-to-use agents in marketplace
- Salesforce: 1K+ pre-built agents in AgentExchange
- QuantaLogic: No marketplace (build your own)

**Reality**: Hyperscalers have massive pre-built agent marketplaces. QuantaLogic doesn't. You build all agents yourself (or use MCP community servers).

#### Strategic Trade-Off Analysis

| Dimension | Hyperscalers | QuantaLogic | Winner |
|-----------|-------------|-------------|--------|
| **Ecosystem maturity** | ✅ 50K-160K customers | 🟡 ~500 customers | Hyperscalers |
| **Framework flexibility** | ❌ Single framework | ✅ ADK/CrewAI/LangGraph | QuantaLogic |
| **EU sovereignty** | ❌ US Cloud Act | ✅ GDPR/DORA/NIS2 | QuantaLogic |
| **Deployment options** | ❌ Cloud-locked | ✅ Anywhere | QuantaLogic |
| **Support** | ✅ 24/7 global | 🟡 Business hours EU | Hyperscalers |
| **Pre-built integrations** | ✅ 1000s | 🟡 ~50 MCP | Hyperscalers |
| **Model choice** | ⚠️ Cloud's models | ✅ 15+ models | QuantaLogic |
| **Cost** | ⚠️ Cloud markup | ✅ 49% cheaper | QuantaLogic |
| **Vendor lock-in** | ❌ High | ✅ None | QuantaLogic |
| **Production maturity** | ✅ Years | 🟡 Months | Hyperscalers |

### When to Choose QuantaLogic (Realistic Assessment)

**✅ Strong Use Cases** (QuantaLogic is the right choice):

1. **EU Regulated Industries** (Financial services, healthcare, government)
   - DORA/GDPR/NIS2 compliance is non-negotiable
   - Data MUST stay in EU (no US Cloud Act exposure)
   - **Verdict**: ✅ QuantaLogic is the ONLY platform that delivers this

2. **Multi-Framework Teams**
   - Backend team knows Google ADK
   - Data team prefers CrewAI
   - Different frameworks are required for different use cases
   - **Verdict**: ✅ QuantaLogic avoids framework lock-in

3. **Multi-Cloud Strategy**
   - Don't want to be locked to AWS/GCP/Azure
   - Need to deploy same agents to different clouds
   - **Verdict**: ✅ QuantaLogic is cloud-agnostic

4. **Cost-Sensitive**
   - Need to optimize model costs (use cheapest model per task)
   - Want to avoid hyperscaler markup
   - **Verdict**: ✅ 49% savings are real

**⚠️ Marginal Use Cases** (Consider both options):

1. **Growing Startups** (100-1000 employees)
   - If EU-based → ✅ QuantaLogic (sovereignty + cost)
   - If US-based, not regulated → 🟡 Hyperscaler (ecosystem)

2. **Single Framework** (everyone uses Google ADK only)
   - If EU data → ✅ QuantaLogic (sovereignty)
   - If no EU requirements → 🟡 Google ADK on GCP (native integration)

**❌ Weak Use Cases** (Hyperscaler is better):

1. **24/7 Global Operations** (need support in all timezones)
   - QuantaLogic support is EU business hours
   - **Verdict**: ❌ Choose hyperscaler for global 24/7 support

2. **Need Maximum Marketplace** (1000+ pre-built agents)
   - AWS/Salesforce have huge agent marketplaces
   - **Verdict**: ❌ Choose hyperscaler if you want pre-built agents

3. **Cloud-Specific Features Required** (Step Functions, EventBridge, etc.)
   - QuantaLogic is cloud-agnostic = doesn't integrate cloud-specific services
   - **Verdict**: ❌ Stay on native hyperscaler platform

### Honest Recommendation

**QuantaLogic is NOT**:
- ❌ A feature-complete hyperscaler alternative (ecosystem is smaller)
- ❌ A replacement for hyperscalers in ALL use cases
- ❌ A mature platform with years of production hardening

**QuantaLogic IS**:
- ✅ The ONLY EU sovereign agentic platform (GDPR/DORA/NIS2 native)
- ✅ The ONLY platform that runs agents from multiple frameworks
- ✅ A cost-effective alternative (49% savings vs hyperscaler lock-in)
- ✅ A hedge against vendor lock-in (deploy anywhere, use any framework)

**Decision Framework**:

```text
START: Should you choose QuantaLogic?
│
├─ Is EU data sovereignty REQUIRED (regulated industry)?
│  └─ YES → ✅ QuantaLogic (ONLY option for EU sovereignty)
│
├─ Do you have multi-framework teams?
│  └─ YES → ✅ QuantaLogic (avoid framework lock-in)
│
├─ Is vendor lock-in a concern?
│  └─ YES → ✅ QuantaLogic (cloud/framework agnostic)
│
├─ Need 24/7 global support?
│  └─ YES → ❌ Choose hyperscaler
│
├─ Need 1000+ pre-built agents from marketplace?
│  └─ YES → ❌ Choose hyperscaler
│
└─ Default:
   ├─ EU company → 🟡 Lean QuantaLogic (sovereignty + cost)
   └─ US company → 🟡 Lean hyperscaler (ecosystem + support)
```

**Timeline Expectation**:
- Hyperscaler: Mature platform (2-3 years production), large ecosystem
- QuantaLogic: Emerging platform (6-12 months production), growing ecosystem

**Realistic Adoption**:
- If sovereignty is required → QuantaLogic is the answer
- If framework flexibility matters → QuantaLogic is compelling
- If neither → Hyperscaler is safer bet (more mature)

---

**Next**: Where is this all heading?

[Continue to Part 8 →](./08-path-forward.md)

---

[← Previous: Implementation Guide](./06-implementation.md) | [Back to Index](./README.md) | [Next: The Path Forward →](./08-path-forward.md)

*Written by [Raphaël Mansuy](https://www.linkedin.com/in/raphaelmansuy/)*

