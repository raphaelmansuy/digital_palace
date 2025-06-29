# Quantalogic Flow for the Impatient

> **⚡ TL;DR**: Quantalogic Flow is a production-ready Python library for workflow automation that supports both YAML (declarative) and Python (fluent API) approaches. Perfect for LLM-powered pipelines, data processing, and enterprise automation.

## 🚀 **Quick Start (5 minutes)**

### Installation

```bash
pip install quantalogic-flow
```

### Instant Example - Fluent API

```python
from quantalogic_flow import Workflow, Nodes
import asyncio

@Nodes.define(output="data")
def read_data():
    return "hello world"

@Nodes.define(output="processed_data")
def process_data(data):
    return data.upper()

@Nodes.define()
def write_data(processed_data):
    print(processed_data)

workflow = (
    Workflow("read_data")
    .then("process_data")
    .then("write_data")
)

# Run it
result = asyncio.run(workflow.build().run({}))
# Output: HELLO WORLD
```

### Instant Example - YAML

```yaml
# simple_workflow.yaml
functions:
  read_data:
    type: embedded
    code: |
      def read_data():
          return "hello world"
  process_data:
    type: embedded
    code: |
      def process_data(data):
          return data.upper()

nodes:
  start:
    function: read_data
    output: data
  process:
    function: process_data
    inputs_mapping:
      data: "data"
    output: processed_data

workflow:
  start: start
  transitions:
    - from_node: start
      to_node: process
```

```python
from quantalogic_flow.flow.flow_manager import WorkflowManager
import asyncio

manager = WorkflowManager()
manager.load_from_yaml("simple_workflow.yaml")
workflow = manager.instantiate_workflow()
result = asyncio.run(workflow.build().run({}))
```

## 🎯 **Core Concepts**

| Concept | Description | Example |
|---------|-------------|---------|
| **Nodes** | Individual tasks (functions, LLMs, templates) | `@Nodes.define()` |
| **Workflows** | Connected sequence of nodes | `.then("next_node")` |
| **Context** | Shared data dictionary between nodes | `ctx["data"]` |
| **Input Mapping** | Connect node inputs to context keys | `inputs_mapping={"data": "raw_data"}` |

## 🔧 **Essential Patterns**

### 1. LLM Integration

```python
@Nodes.llm_node(
    model="gpt-4o-mini",
    system_prompt="You are a helpful assistant.",
    prompt_template="Explain: {{topic}}",
    output="explanation"
)
async def explain_topic(topic: str) -> str:
    pass

workflow = Workflow("explain_topic").node("explain_topic", 
    inputs_mapping={"topic": "user_input"})
```

### 2. Structured Data Extraction

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

@Nodes.structured_llm_node(
    system_prompt="Extract person info as JSON.",
    output="person",
    response_model=Person,
    prompt_template="Extract from: {{text}}"
)
async def extract_person(text: str) -> Person:
    pass
```

### 3. Conditional Branching

```python
workflow = (
    Workflow("start_node")
    .branch([
        ("high_path", lambda ctx: ctx["value"] > 10),
        ("low_path", lambda ctx: ctx["value"] <= 10)
    ])
)
```

### 4. Looping

```python
workflow = (
    Workflow("init")
    .start_loop()
    .node("increment")
    .end_loop(lambda ctx: ctx["count"] >= 5, "end")
)
```

### 5. Template Rendering

```python
@Nodes.template_node(
    output="message",
    template="Hello {{name}}, you have {{count}} items"
)
async def format_message(rendered_content: str, name: str, count: int):
    return rendered_content
```

## 🛠️ **Advanced Features**

### Dynamic Model Selection

```python
# In YAML
nodes:
  generate:
    llm_config:
      model: "lambda ctx: ctx['model_name']"
      prompt_template: "Write about {{topic}}"
```

### Sub-Workflows

```python
sub_workflow = Workflow("sub_start").then("sub_end")
workflow.add_sub_workflow("parent_node", sub_workflow, 
    inputs={"key": "value"}, output="result")
```

### Observers (Debugging)

```python
workflow.add_observer(lambda event: 
    print(f"{event.node_name} - {event.event_type}"))
```

## 🔍 **Debugging & Validation**

### Validate Before Running

```python
from quantalogic_flow.flow.flow_validator import validate_workflow_definition

issues = validate_workflow_definition(manager.workflow)
for issue in issues:
    print(f"Node '{issue.node_name}': {issue.description}")
```

### Generate Mermaid Diagrams

```python
from quantalogic_flow.flow.flow_mermaid import generate_mermaid_diagram

print(generate_mermaid_diagram(manager.workflow, title="My Workflow"))
```

## 🌟 **LLM Provider Setup**

### Environment Variables

```bash
export OPENAI_API_KEY="sk-your-openai-key"
export GEMINI_API_KEY="your-gemini-key"
export DEEPSEEK_API_KEY="ds-your-deepseek-key"
```

### Supported Models

| Provider | Model Example | Use Case |
|----------|--------------|----------|
| OpenAI | `openai/gpt-4o-mini` | Fast, cost-effective |
| OpenAI | `openai/gpt-4o` | Advanced reasoning |
| Gemini | `gemini/gemini-2.0-flash` | Creative tasks |
| DeepSeek | `deepseek/deepseek-chat` | Conversational |
| Anthropic | `anthropic/claude-3.5-sonnet` | Balanced performance |

## 📊 **Real-World Example: Story Generator**

```python
from quantalogic_flow import Workflow, Nodes
from pydantic import BaseModel

class ToneModel(BaseModel):
    tone: str  # "light" or "dark"

@Nodes.llm_node(
    model="gpt-4o-mini",
    system_prompt="You are a creative writer.",
    prompt_template="Create a story outline for a {{genre}} story.",
    output="outline"
)
async def generate_outline(genre: str) -> str:
    pass

@Nodes.structured_llm_node(
    system_prompt="Analyze the tone of this story outline.",
    prompt_template="Determine if this is light or dark: {{outline}}",
    response_model=ToneModel,
    output="tone_analysis"
)
async def analyze_tone(outline: str) -> ToneModel:
    pass

@Nodes.llm_node(
    model="gpt-4o-mini",
    system_prompt="You are a writer.",
    prompt_template="Write a chapter for this {{tone}} story: {{outline}}",
    output="chapter"
)
async def write_chapter(outline: str, tone: str) -> str:
    pass

workflow = (
    Workflow("generate_outline")
    .then("analyze_tone")
    .then("write_chapter", inputs_mapping={
        "tone": "tone_analysis.tone"
    })
)

# Run the workflow
context = {"genre": "fantasy"}
result = asyncio.run(workflow.build().run(context))
print(result["chapter"])
```

## 🔄 **Conversion Tools**

### YAML to Python

```python
from quantalogic_flow.flow.flow_generator import generate_executable_script

manager = WorkflowManager()
manager.load_from_yaml("workflow.yaml")
generate_executable_script(manager.workflow, {}, "script.py")
```

### Python to YAML

```python
from quantalogic_flow.flow.flow_extractor import extract_workflow_from_file

workflow_def, globals = extract_workflow_from_file("script.py")
WorkflowManager(workflow_def).save_to_yaml("workflow.yaml")
```

## 🎨 **Best Practices**

### ✅ Do's

- **Start Small**: Begin with 2-3 nodes to understand context flow
- **Validate Early**: Use `validate_workflow_definition()` before running
- **Use Observers**: Add debugging observers for complex workflows
- **Secure Keys**: Store API keys in `.env` files
- **Document YAML**: Add comments explaining node purposes

### ❌ Don'ts

- Don't skip validation on complex workflows
- Don't hardcode API keys in code
- Don't create circular dependencies
- Don't ignore context data types

## 🔗 **Quick Reference Links**

| Resource | Purpose | Link |
|----------|---------|------|
| **GitHub Repo** | Source code and examples | [quantalogic/quantalogic](https://github.com/quantalogic/quantalogic/tree/main/quantalogic_flow) |
| **PyPI Package** | Installation and releases | [quantalogic-flow](https://pypi.org/project/quantalogic-flow) |
| **YAML Reference** | Complete YAML syntax guide | [flow_yaml.md](https://github.com/quantalogic/quantalogic/blob/main/quantalogic_flow/flow_yaml.md) |
| **Examples** | Real-world use cases | [Examples directory](https://github.com/quantalogic/quantalogic/tree/main/quantalogic_flow/examples) |

## 🚀 **Next Steps**

1. **Install**: `pip install quantalogic-flow`
2. **Try Examples**: Copy-paste the story generator example
3. **Explore YAML**: Create your first declarative workflow
4. **Add LLMs**: Integrate with your favorite AI models
5. **Scale Up**: Build complex multi-step automation pipelines

---

*Part of the [QuantaLogic ecosystem](https://github.com/quantalogic/quantalogic) - combining structured workflows with dynamic AI agents*

**Last Updated**: January 2025  
**Version**: Compatible with quantalogic-flow 0.91+
