# 🏗️ 12-Factor Agents: Patterns for Reliable LLM Applications

- [Overview](#overview)
- [Core Philosophy](#core-philosophy)
- [The 12 Factors](#the-12-factors)
  - [Factor 1: Structured Output](#factor-1-structured-output)
  - [Factor 2: Own Your Prompts](#factor-2-own-your-prompts)
  - [Factor 3: Context Engineering](#factor-3-context-engineering)
  - [Factor 4: Tool Use Is Just JSON + Code](#factor-4-tool-use-is-just-json--code)
  - [Factor 5: Error Handling with Context Management](#factor-5-error-handling-with-context-management)
  - [Factor 6: Human-in-the-Loop Integration](#factor-6-human-in-the-loop-integration)
  - [Factor 7: Multi-Channel Integration](#factor-7-multi-channel-integration)
  - [Factor 9: Micro-Agents Over Monoliths](#factor-9-micro-agents-over-monoliths)
  - [Factor 10: Stateless Agents](#factor-10-stateless-agents)
  - [Factor 11: Pause and Resume Capability](#factor-11-pause-and-resume-capability)
  - [Factor 12: Production Deployment Patterns](#factor-12-production-deployment-patterns)
- [Common Pitfalls & Anti-Patterns](#common-pitfalls--anti-patterns)
- [Migration Path: How to Start](#migration-path-how-to-start)
- [Implementation Strategies](#implementation-strategies)
- [Real-World Examples](#real-world-examples)
- [Monitoring and Observability](#monitoring-and-observability)
- [Cross-References](#cross-references)
- [Production Considerations](#production-considerations)
- [Next Steps](#next-steps)
- [Key Takeaways](#key-takeaways)


**Implementation**:

- Design context windows intentionally
- Optimize for token density and clarity
- Don't blindly append everything to context
- Summarize and filter strategically

Based on the seminal presentation "[12-Factor Agents: Patterns of reliable LLM applications](https://www.youtube.com/watch?v=8kMaTybvDUw)" by [Dex Horthy](../../people/dex-horthy.md), HumanLayer CEO, at AI Engineer Conference 2024.

---

## 🎯 Overview

The 12-Factor Agents methodology adapts the proven [12-Factor App](https://12factor.net/) principles for building reliable, scalable AI agent applications. Unlike traditional software, AI agents face unique challenges: non-deterministic behavior, complex context management, and the need for human oversight in production environments.

**Key Insight**: Agents are software. Apply everything we've learned from software engineering to build reliable AI systems.

---

## 🧠 Core Philosophy

### **Agents Are Just Software**

- **LLMs are pure functions**: Tokens in → Tokens out
- **Control flow matters**: Own your loops, switches, and state management  
- **JSON + Code**: Tool use is just structured output feeding deterministic logic
- **Context engineering**: Everything depends on getting the right tokens to the model

### **Focus on the Hard AI Parts**

Frameworks should handle infrastructure complexity so you can focus on:

- Getting prompts right
- Optimizing token density and clarity
- Managing context windows effectively
- Building reliable control flow

---

## 📋 The 12 Factors

### **Factor 1: Structured Output** 🏗️

**Principle**: The most magical thing LLMs can do is turn sentences into structured JSON.


**Implementation**:

```python
# Turn natural language into actionable data
user_input = "Schedule a meeting with Sarah next Tuesday at 3 PM"

# LLM outputs structured JSON
{
  "action": "schedule_meeting",
  "participant": "Sarah",
  "date": "2024-07-16",
  "time": "15:00",
  "timezone": "user_default"
}
```

**Why it matters**: This is the foundation. Everything else builds on your ability to reliably extract structured data from natural language.

---

### **Factor 2: Own Your Prompts** ✍️

**Principle**: Eventually, you'll need to write every token by hand for maximum quality.


**Implementation**:

- Start with prompt libraries and frameworks for speed
- Graduate to handcrafted prompts for quality
- Test every token - LLMs are pure functions
- Own the context building process completely

```python
# Instead of framework-generated prompts
prompt = build_custom_prompt(
    system_context=system_context,
    user_input=user_input,
    agent_state=current_state,
    tool_results=tool_outputs
)
```

**Key insight**: You can't optimize what you don't control.

---

### **Factor 3: Context Engineering** 🎯

**Principle**: Everything in making agents good is context engineering - prompt, memory, RAG, history.


**Implementation**:

- Design context windows intentionally
- Optimize for token density and clarity
- Don't blindly append everything to context
- Summarize and filter strategically

```python
def build_context_window(state, new_input):
    # Don't just append everything
    context = {
        "system": get_system_prompt(),
        "relevant_history": summarize_history(state.history, new_input),
        "current_state": state.to_dict(),
        "tools_available": get_relevant_tools(new_input),
        "user_input": new_input
    }
    return optimize_token_density(context)
```

---

### **Factor 4: Tool Use Is Just JSON + Code** 🔧

**Principle**: Abandon the mystical view of "tool use" - it's structured output feeding deterministic code.


**Implementation**:

```python
# LLM generates structured tool call
tool_call = {
    "function": "send_email",
    "parameters": {
        "to": "sarah@company.com",
        "subject": "Meeting Confirmation",
        "body": "..."
    }
}

# Deterministic code executes it
result = execute_tool_call(tool_call)

# Feed result back to context if needed
if should_continue_workflow(result):
    context.append(result)
```

**Anti-pattern**: Treating tool use as magical AI behavior instead of structured programming.

---

### **Factor 5: Error Handling with Context Management** ⚠️

**Principle**: When models mess up, manage errors intelligently in your context window.


**Implementation**:

```python
def handle_tool_error(tool_call, error, context_window):
    # Don't just blindly append stack traces
    if is_valid_retry_scenario(error):
        context_window.clear_pending_errors()
        context_window.add_error_summary(error)
        return retry_with_context(tool_call, context_window)
    else:
        return escalate_to_human(tool_call, error)
```

**Key practice**: Clear successful operations, summarize failures, don't spam context with stack traces.

---

### **Factor 6: Human-in-the-Loop Integration** 👥

**Principle**: Push human interaction decisions to natural language tokens, not binary tool-vs-message choices.


**Implementation**:

```python
# Instead of binary: tool_call OR message
# Use natural language decisions:

agent_response = {
    "intent": "need_clarification",  # or "task_complete", "need_approval", etc.
    "message": "I need clarification on the budget before proceeding",
    "proposed_action": {...},
    "confidence": 0.7
}
```

**Benefits**: More nuanced interaction patterns, better sampling behavior, clearer intent modeling.

---

### **Factor 7: Multi-Channel Integration** 📱

**Principle**: Meet users where they are - email, Slack, Discord, SMS, not just chat interfaces.


**Implementation**:

```python
class AgentInterface:
    def __init__(self):
        self.channels = {
            'slack': SlackHandler(),
            'email': EmailHandler(), 
            'sms': SMSHandler(),
            'api': RestAPIHandler()
        }
    
    def receive_message(self, channel, message):
        # Same agent logic, different interfaces
        response = self.agent.process(message)
        return self.channels[channel].send(response)
```

**Why it matters**: Users don't want 7 tabs open. Integrate with existing workflows.

---

```python
while True:
    if self.should_summarize(context):
        context = self.summarize_and_continue(context)
    else:
        break
        
return self.finalize_response(context)
```

---

### **Factor 9: Micro-Agents Over Monoliths** 🔬

**Principle**: Build small, focused agents (3-10 steps) rather than complex autonomous loops.


**Implementation**:

```python
# Instead of one massive agent
class DeploymentOrchestrator:
    def __init__(self):
        self.deploy_agent = MicroAgent("deployment", max_steps=5)
        self.rollback_agent = MicroAgent("rollback", max_steps=3)
        self.test_agent = MicroAgent("testing", max_steps=7)
    
    def handle_deployment(self, pr_merged_event):
        # Mostly deterministic workflow
        if self.tests_passing(pr_merged_event):
            # Small agent loop for deployment decisions
            deploy_plan = self.deploy_agent.plan(pr_merged_event)
            if self.human_approves(deploy_plan):
                result = self.execute_deployment(deploy_plan)
                # Back to deterministic code
                self.run_integration_tests(result)
```

**Benefits**: Manageable context, clear responsibilities, easier debugging.

---

### **Factor 10: Stateless Agents** 📊

**Principle**: Agents should be stateless - externalize state management.


**Implementation**:

```python
class StatelessAgent:
    def process(self, input_data, state_id=None):
        # Load state from external store
        state = self.state_store.load(state_id) if state_id else {}
        
        # Process with current state
        response = self.generate_response(input_data, state)
        
        # Save updated state
        new_state_id = self.state_store.save(response.state)
        
        return {
            "response": response.content,
            "state_id": new_state_id,
            "next_action": response.next_action
        }
```

**Benefits**: Scalable, recoverable, pausable workflows.

---

### **Factor 11: Pause and Resume Capability** ⏸️

**Principle**: Enable workflows to pause for long-running tasks or human approval.


**Implementation**:

```python
async def pausable_workflow(workflow_id, current_step):
    state = await self.state_store.load(workflow_id)
    
    if state.requires_human_approval:
        # Serialize context and wait
        await self.notification_service.request_approval(
            workflow_id, 
            state.pending_action
        )
        return {"status": "paused", "workflow_id": workflow_id}
    
    # Continue processing
    result = await self.execute_step(state.current_step)
    state.update(result)
    
    if result.needs_background_task:
        # Queue long-running task
        await self.task_queue.enqueue(workflow_id, result.task)
        return {"status": "background", "workflow_id": workflow_id}
    
    return self.continue_workflow(workflow_id, state)
```

---

### **Factor 12: Production Deployment Patterns** 🚀

**Principle**: Apply cloud-native deployment practices to AI agents.

**Implementation**:


**Environment Parity**:

```yaml
# Same agent config across environments
apiVersion: v1
kind: ConfigMap
metadata:
  name: agent-config
data:
  model_provider: "openai"
  max_context_tokens: "8192"
  tool_timeout: "30s"
  human_approval_required: "true"
```


**Observability**:

```python
class ObservableAgent:
    def process(self, input_data):
        span = self.tracer.start_span("agent.process")
        span.set_attribute("input.type", type(input_data).__name__)
        
        try:
            response = self.llm.generate(input_data)
            span.set_attribute("tokens.used", response.token_count)
            span.set_attribute("confidence", response.confidence)
            return response
        except Exception as e:
            span.record_exception(e)
            raise
        finally:
            span.end()
```


**Graceful Degradation**:

```python
def fallback_processing(input_data):
    try:
        return self.primary_agent.process(input_data)
    except ModelUnavailable:
        return self.backup_agent.process(input_data)
    except ContextTooLarge:
        return self.summarize_and_retry(input_data)
    except Exception:
        return self.human_escalation(input_data)
```

---

## 🚩 Common Pitfalls & Anti-Patterns

- **Letting frameworks own your agent’s control flow**: Always own your loops, switches, and state transitions.
- **Treating tool use as magic**: Tool use is just structured output (JSON) and deterministic code. Don’t mystify it.
- **Appending everything to context**: Avoid context bloat. Summarize, filter, and optimize for token density.
- **Ignoring observability**: Track metrics, errors, and human escalations from day one.
- **Building monolithic agents**: Prefer micro-agents (3–10 steps) with clear responsibilities.
- **Not externalizing state**: Agents should be stateless; use external stores for workflow state.
- **No pause/resume**: Production agents must support pausing for human input or long-running tasks.
- **No human-in-the-loop**: Push nuanced decisions to natural language, not just binary tool/message splits.

---

## 🛣️ Migration Path: How to Start

1. **Start with Factor 1**: Practice structured output (JSON from LLMs).
2. **Own your prompts**: Move from framework-generated to handcrafted prompts.
3. **Implement observability**: Add logging, tracing, and error tracking early.
4. **Refactor to micro-agents**: Break up monoliths into focused, testable agents.
5. **Externalize state**: Use a database or store for agent state, not in-memory.
6. **Add pause/resume**: Enable workflows to pause for approvals or background tasks.
7. **Integrate human-in-the-loop**: Design for nuanced, token-level human decisions.
8. **Deploy cloud-native**: Use environment parity, observability, and graceful fallback patterns.

---

## 🛠️ Implementation Strategies

### **Start Small, Scale Smart**

1. **Begin with Factor 1**: Master structured output before adding complexity
2. **Own your prompts early**: Don't get locked into framework abstractions
3. **Implement observability from day one**: You'll need it for debugging
4. **Build micro-agents**: 3-10 steps max, clear responsibilities

### **Tools and Frameworks**


**Aligned with 12-Factor Principles**:

- [Langfuse](https://langfuse.com/) - Observability and tracing
- [HumanLayer](https://humanlayer.dev/) - Human-in-the-loop infrastructure


**Migration Strategy**:

```python
# Gradual migration from framework to owned code
class CustomAgent:
    def __init__(self, framework_agent=None):
        self.framework_agent = framework_agent
        self.custom_components = {}
    
    def migrate_component(self, component_name, custom_impl):
        self.custom_components[component_name] = custom_impl
    
    def process(self, input_data):
        # Use custom implementation if available
        if 'prompt_builder' in self.custom_components:
            prompt = self.custom_components['prompt_builder'](input_data)
        else:
            prompt = self.framework_agent.build_prompt(input_data)
        
        return self.generate_response(prompt)
```

---

## 🎯 Real-World Examples

### **Example 1: DevOps Agent (HumanLayer)**


```python
class DevOpsAgent:
    """Micro-agent for deployment decisions"""
    
    def handle_pr_merged(self, pr_event):
        # Factor 1: Structured output
        deployment_plan = self.plan_deployment(pr_event)
        
        # Factor 6: Human approval for high-stakes operations
        if deployment_plan.risk_level > 0.7:
            approval = self.request_human_approval(deployment_plan)
            if not approval.approved:
                return self.handle_rejection(approval.feedback)
        
        # Factor 8: Owned control flow
        result = self.execute_deployment(deployment_plan)
        
        # Factor 11: Pause for background tasks
        if result.requires_testing:
            return self.pause_for_integration_tests(result.deployment_id)
        
        return result

    def plan_deployment(self, pr_event):
        # Factor 2: Custom prompt for deployment planning
        prompt = f"""
        Analyze this PR and create a deployment plan:
        
        PR: {pr_event.title}
        Changes: {pr_event.files_changed}
        Tests: {pr_event.test_results}
        
        Consider:
        - Risk level (0.0-1.0)
        - Deployment order (frontend/backend)
        - Rollback requirements
        
        Output JSON with deployment steps.
        """
        
        return self.llm.generate_structured(prompt, DeploymentPlan)
```

### **Example 2: Customer Support Agent**


```python
class SupportAgent:
    """Multi-channel customer support with escalation"""
    
    def process_inquiry(self, channel, message, customer_id):
        # Factor 10: Stateless with external state
        customer_context = self.load_customer_context(customer_id)
        
        # Factor 3: Context engineering
        context = self.build_support_context(
            customer_context, 
            message, 
            self.get_relevant_kb_articles(message)
        )
        
        # Factor 4: Tool use as structured output
        response = self.generate_response(context)
        
        if response.needs_human_escalation:
            # Factor 6: Human-in-the-loop
            return self.escalate_to_agent(response, customer_context)
        
        # Factor 7: Multi-channel response
        return self.send_via_channel(channel, response.message)
    
    def build_support_context(self, customer, message, kb_articles):
        # Factor 3: Optimized context building
        return {
            "customer_tier": customer.tier,
            "recent_interactions": customer.recent_issues[-3:],
            "current_issue": message,
            "relevant_articles": [a.summary for a in kb_articles],
            "escalation_threshold": 0.8
        }
```

---

## 📊 Monitoring and Observability

### **Key Metrics to Track**


```python
class AgentMetrics:
    def track_execution(self, agent_run):
        # Performance metrics
        self.histogram("agent.execution_time", agent_run.duration)
        self.histogram("agent.token_usage", agent_run.tokens_used)
        self.counter("agent.tool_calls", tags={"tool": agent_run.primary_tool})
        
        # Quality metrics  
        self.gauge("agent.confidence", agent_run.confidence_score)
        self.counter("agent.human_escalations", tags={"reason": agent_run.escalation_reason})
        self.counter("agent.errors", tags={"type": agent_run.error_type})
        
        # Business metrics
        self.counter("agent.tasks_completed", tags={"success": agent_run.success})
        self.histogram("agent.user_satisfaction", agent_run.user_rating)
```

### **Alerting Patterns**


```python
# Set up intelligent alerting
alerts = [
    Alert("high_error_rate", threshold=0.05, window="5m"),
    Alert("token_usage_spike", threshold=2.0, baseline="1h"),
    Alert("human_escalation_surge", threshold=0.3, window="10m"),
    Alert("low_confidence_trend", threshold=0.6, window="30m")
]
```

---

## 🔗 Cross-References

### **Related Digital Palace Content**

**[AI Agents Guide](../ai-agents.md)** - Comprehensive implementation patterns
**[Agent Development SOP](./sop_ai_agent.md)** - Standard operating procedures  
**[Production Deployment](../deployment.md)** - Scaling agents to production
**[Dex Horthy Profile](../../people/dex-horthy.md)** - Author background and expertise
**[HumanLayer](../../tools/ai-tools-master-directory.md#human-in-the-loop-platforms)** - Human-in-the-loop infrastructure

### **Framework Comparisons**

**[AutoGen](../../reference/techniques/autogen/README.md)** - Microsoft's multi-agent framework
**[Design Patterns for LLM Applications](../../reference/techniques/dessign_patterns_for_llm_applications/README.md)** - Architectural patterns
**[Context Management](../../reference/technical-articles/2025-06-29-context-management-llm-agents.md)** - Advanced context strategies

### **Production Considerations**

- **[Observability](../../concepts/observability.md)** - Monitoring patterns
- **[AI Safety & Ethics](../../concepts/ai-safety-ethics.md)** - Responsible deployment
- **[MLOps](../../concepts/mlops.md)** - Operational best practices

---

## 🚀 Next Steps

### **Getting Started**

1. **📺 Watch the original presentation**: [12-Factor Agents video](https://www.youtube.com/watch?v=8kMaTybvDUw)
2. **🛠️ Start with Factor 1**: Practice structured output generation
3. **📖 Read the SOP**: Follow our [Agent Development SOP](./sop_ai_agent.md)
4. **🏗️ Build a micro-agent**: Keep it to 3-10 steps max

### **Advanced Implementation**

1. **🔄 Implement pause/resume**: Add state management to your agents
2. **👥 Add human oversight**: Integrate approval workflows
3. **📊 Set up observability**: Monitor performance and quality metrics
4. **🚀 Deploy to production**: Follow cloud-native deployment patterns

### **Community & Resources**

<!-- GitHub Repository: Link removed, repository not found (404) -->
- **HumanLayer Platform**: [humanlayer.dev](https://humanlayer.dev) - Human-in-the-loop infrastructure
- **AI Tinkerers**: San Francisco meetups on practical AI agent development

---

## ⭐ Key Takeaways

> **"Agents are just software. You all can build software. Anyone ever written a switch statement before? While loop? Yeah, okay, so we can do this stuff."**  
> — Dex Horthy

1. **LLMs are stateless functions** - Focus on token in, token out
2. **Own your state and control flow** - Don't let frameworks control your agent logic
3. **Find the bleeding edge** - Do things better than everyone else through careful engineering
4. **AI agents are better with people** - Build in human collaboration from the start

The 12-Factor methodology isn't anti-framework - it's about understanding what you need to own vs. what can be abstracted. Use frameworks to handle infrastructure complexity so you can focus on the hard AI parts: getting prompts right, managing context effectively, and building reliable agent behavior.

---

*Based on "[12-Factor Agents: Patterns of reliable LLM applications](https://www.youtube.com/watch?v=8kMaTybvDUw)" by [Dex Horthy](../../people/dex-horthy.md)*  
*Last updated: July 13, 2025*
