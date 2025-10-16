# Part 6: Reality Check & Limitations

[← Previous: Implementation Guide](./05-implementation.md) | [Back to Index](./README.md) | [Next: The Path Forward →](./07-path-forward.md)

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

**Next**: Where is this all heading?

[Continue to Part 7 →](./07-path-forward.md)

---

[← Previous: Implementation Guide](./05-implementation.md) | [Back to Index](./README.md) | [Next: The Path Forward →](./07-path-forward.md)
