# Google ADK (Agent Development Kit) - Complete Guide

> Build production-ready AI agents with Google's official framework - from simple chatbots to complex multi-agent systems

## 🎯 What You'll Achieve

By the end of this guide, you'll have:
- Built your first Google ADK agent
- Understanding of ADK's architecture and components
- Knowledge of multi-agent orchestration
- Production deployment on Google Cloud

**Difficulty**: 🟡 Intermediate | **Time**: 4-8 hours | **Prerequisites**: Python knowledge, basic AI/LLM experience

---

## 🚀 Quick Start

### Installation

```bash
# Install the Python SDK
pip install google-adk

# Or install the Java SDK (if using Java)
# gradle implementation 'com.google.ai:adk:latest'
```

### Your First Agent

```python
from google.ai import adk

# Create a simple agent
agent = adk.Agent(
    name="assistant",
    model="gemini-pro",
    instructions="You are a helpful AI assistant."
)

# Run the agent
response = agent.run("What's the weather like today?")
print(response)
```

---

## 🏗️ Core Architecture

### Agent Types

**1. LLM Agents** - Direct language model interactions
```python
from google.ai.adk import LlmAgent

agent = LlmAgent(
    name="researcher",
    model="gemini-pro",
    instructions="You are a research specialist.",
    tools=["search", "calculator"]
)
```

**2. Workflow Agents** - Orchestrate multiple steps
```python
from google.ai.adk import Sequential, Parallel

# Sequential workflow
workflow = Sequential([
    agent1,  # Research agent
    agent2,  # Analysis agent  
    agent3   # Writing agent
])

# Parallel workflow
parallel_tasks = Parallel([
    agent_a,  # Task A
    agent_b,  # Task B
    agent_c   # Task C
])
```

**3. Loop Agents** - Iterative processing
```python
from google.ai.adk import Loop

loop_agent = Loop(
    agent=processing_agent,
    condition=lambda state: not state.is_complete(),
    max_iterations=10
)
```

### Key Components

| Component | Purpose | Example Use |
|-----------|---------|-------------|
| **Agent** | Core AI entity | Single-purpose tasks |
| **Tools** | External capabilities | API calls, calculations |
| **Memory** | State management | Conversation history |
| **Session** | Execution context | User interactions |
| **Runtime** | Execution engine | Production deployment |

---

## 🛠️ Tools & Integration

### Built-in Tools

```python
from google.ai.adk.tools import Search, CodeExecution

agent = LlmAgent(
    name="developer",
    tools=[
        Search(),                    # Web search
        CodeExecution(),            # Execute code
        "calculator",               # Built-in math
        "file_manager"              # File operations
    ]
)
```

### Custom Tools

```python
from google.ai.adk import tool

@tool
def get_weather(location: str) -> str:
    """Get current weather for a location."""
    # Your weather API logic here
    return f"Weather in {location}: Sunny, 22°C"

@tool  
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email."""
    # Your email sending logic
    return f"Email sent to {to}"

# Use in agent
agent = LlmAgent(
    name="assistant",
    tools=[get_weather, send_email]
)
```

### Third-Party Integrations

**LangChain Integration:**
```python
from langchain.tools import DuckDuckGoSearchResults
from google.ai.adk.tools import LangChainTool

search_tool = LangChainTool(DuckDuckGoSearchResults())

agent = LlmAgent(
    name="researcher",
    tools=[search_tool]
)
```

**CrewAI Integration:**
```python
from crewai import Agent as CrewAgent
from google.ai.adk.tools import CrewAITool

crew_agent = CrewAgent(
    role="Data Analyst",
    goal="Analyze data patterns"
)

adk_tool = CrewAITool(crew_agent)
```

---

## 🤖 Multi-Agent Systems

### Agent Communication

```python
from google.ai.adk import LlmAgent, transfer

# Define specialized agents
research_agent = LlmAgent(
    name="researcher",
    instructions="Research topics thoroughly."
)

analysis_agent = LlmAgent(
    name="analyst", 
    instructions="Analyze research and provide insights."
)

writing_agent = LlmAgent(
    name="writer",
    instructions="Create well-structured reports."
)

# Enable agent-to-agent transfers
research_agent.add_transfer(
    target=analysis_agent,
    condition="when research is complete"
)

analysis_agent.add_transfer(
    target=writing_agent, 
    condition="when analysis is done"
)
```

### Complex Orchestration

```python
from google.ai.adk import Sequential, Parallel, Conditional

# Build a complex workflow
workflow = Sequential([
    # Step 1: Parallel research
    Parallel([
        research_agent_a,  # Research topic A
        research_agent_b,  # Research topic B
        research_agent_c   # Research topic C
    ]),
    
    # Step 2: Conditional analysis  
    Conditional(
        condition=lambda state: state.needs_deep_analysis(),
        if_true=deep_analysis_agent,
        if_false=quick_analysis_agent
    ),
    
    # Step 3: Final report
    writing_agent
])
```

---

## 📊 Evaluation & Testing

### Built-in Evaluation

```python
from google.ai.adk.evaluation import Evaluator, TestCase

# Define test cases
test_cases = [
    TestCase(
        input="What is the capital of France?",
        expected_output="Paris",
        evaluation_criteria=["accuracy", "conciseness"]
    ),
    TestCase(
        input="Calculate 15 * 23",
        expected_output="345",
        evaluation_criteria=["accuracy"]
    )
]

# Run evaluation
evaluator = Evaluator(agent=your_agent)
results = evaluator.evaluate(test_cases)

print(f"Accuracy: {results.accuracy}")
print(f"Average Response Time: {results.avg_response_time}")
```

### Custom Evaluation Metrics

```python
from google.ai.adk.evaluation import custom_metric

@custom_metric
def relevance_score(response: str, context: str) -> float:
    """Calculate relevance score (0-1)."""
    # Your custom scoring logic
    return 0.85

@custom_metric
def safety_check(response: str) -> bool:
    """Check if response is safe.""" 
    # Your safety validation logic
    return True
```

---

## 🚀 Production Deployment

### Local Development

```python
from google.ai.adk.runtime import LocalRuntime

runtime = LocalRuntime(
    agent=your_agent,
    port=8080,
    debug=True
)

runtime.start()  # Agent available at http://localhost:8080
```

### Cloud Run Deployment  

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["python", "main.py"]
```

```python
# main.py
from google.ai.adk.runtime import CloudRunRuntime

runtime = CloudRunRuntime(
    agent=your_agent,
    port=int(os.environ.get("PORT", 8080))
)

if __name__ == "__main__":
    runtime.start()
```

### Vertex AI Agent Engine

```python
from google.ai.adk.deploy import VertexAIDeploy

# Deploy to Vertex AI
deployment = VertexAIDeploy(
    agent=your_agent,
    project_id="your-project-id",
    region="us-central1"
)

deployment.deploy()
print(f"Agent deployed at: {deployment.endpoint}")
```

---

## 🔒 Safety & Security  

### Content Filtering

```python
from google.ai.adk.safety import ContentFilter, SafetySettings

safety_settings = SafetySettings(
    block_harmful_content=True,
    block_harassment=True,
    block_hate_speech=True,
    block_dangerous_content=True
)

agent = LlmAgent(
    name="safe_assistant",
    safety_settings=safety_settings
)
```

### Access Control

```python
from google.ai.adk.auth import AuthConfig

auth_config = AuthConfig(
    require_authentication=True,
    allowed_users=["user1@example.com"],
    rate_limit=100  # requests per hour
)

runtime = CloudRunRuntime(
    agent=your_agent,
    auth_config=auth_config
)
```

---

## 🔄 Streaming & Real-time

### Streaming Responses

```python
from google.ai.adk import StreamingAgent

streaming_agent = StreamingAgent(
    name="chat_assistant",
    model="gemini-pro"
)

# Stream response
for chunk in streaming_agent.stream("Tell me a story"):
    print(chunk, end="", flush=True)
```

### Bi-directional Streaming

```python
from google.ai.adk.streaming import BidiStreaming

async def handle_bidi_stream():
    async with BidiStreaming(agent=your_agent) as stream:
        # Send initial message
        await stream.send("Hello!")
        
        # Listen for responses
        async for response in stream:
            print(f"Agent: {response}")
            
            # Send follow-up
            user_input = input("You: ")
            await stream.send(user_input)
```

---

## 📈 Monitoring & Observability

### Built-in Metrics

```python
from google.ai.adk.monitoring import MetricsCollector

metrics = MetricsCollector(agent=your_agent)

# Access metrics
print(f"Total requests: {metrics.total_requests}")
print(f"Average latency: {metrics.avg_latency}")
print(f"Error rate: {metrics.error_rate}")
```

### Integration with External Tools

```python
# Arize Phoenix integration
from google.ai.adk.observability import ArizePhoenix

phoenix = ArizePhoenix(
    api_key="your-api-key",
    project_name="my-agent-project"
)

agent = LlmAgent(
    name="monitored_agent",
    observability=[phoenix]
)
```

---

## 🎯 Real-World Examples

### Customer Support Agent

```python
from google.ai.adk import LlmAgent, tool
from google.ai.adk.tools import Database

@tool
def get_order_status(order_id: str) -> str:
    """Get order status from database."""
    # Database lookup logic
    return f"Order {order_id}: Shipped"

@tool
def create_support_ticket(issue: str) -> str:
    """Create support ticket."""
    # Ticket creation logic
    return f"Ticket created: #{issue[:10]}"

support_agent = LlmAgent(
    name="support_assistant",
    model="gemini-pro",
    instructions="""
    You are a customer support agent. Help customers with:
    - Order status inquiries
    - Product questions  
    - Issue resolution
    Be friendly, helpful, and professional.
    """,
    tools=[get_order_status, create_support_ticket]
)
```

### Research & Analysis Pipeline

```python
from google.ai.adk import Sequential, LlmAgent
from google.ai.adk.tools import Search, CodeExecution

# Research agent
researcher = LlmAgent(
    name="researcher",
    instructions="Research topics thoroughly using web search.",
    tools=[Search()]
)

# Analysis agent  
analyst = LlmAgent(
    name="analyst",
    instructions="Analyze research data and generate insights.",
    tools=[CodeExecution()]
)

# Report writer
writer = LlmAgent(
    name="writer", 
    instructions="Create comprehensive reports from analysis."
)

# Create pipeline
research_pipeline = Sequential([
    researcher,
    analyst, 
    writer
])

# Execute
result = research_pipeline.run(
    "Analyze the current state of renewable energy adoption"
)
```

---

## 🔗 Resources & Next Steps

### Official Resources
- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [API Reference](https://google.github.io/adk-docs/api-reference/)
- [Sample Agents](https://github.com/google/adk-samples)
- [Community Forum](https://google.github.io/adk-docs/community/)

### SDKs & Tools
- [Python SDK](https://github.com/google/adk-python)
- [Java SDK](https://github.com/google/adk-java)
- [CLI Tools](https://google.github.io/adk-docs/get-started/installation/)

### Learning Path
1. **Start**: Complete the [Quick Start Guide](https://google.github.io/adk-docs/get-started/quickstart/)
2. **Practice**: Build the [tutorial agents](https://google.github.io/adk-docs/tutorials/)
3. **Deploy**: Try [Cloud deployment](https://google.github.io/adk-docs/deploy/)
4. **Scale**: Implement [multi-agent systems](https://google.github.io/adk-docs/agents/multi-agents/)

### Related Tools in Digital Palace
- [AI Agent Frameworks Comparison](../tools/ai-tools-master-directory.md#ai-agent-frameworks)
- [AI Agents Implementation Guide](./ai-agents.md)
- [Production Deployment Guide](./deployment.md)

---

**🚀 Ready to build your first Google ADK agent?** Start with the [Quick Start](#-quick-start) section above!
