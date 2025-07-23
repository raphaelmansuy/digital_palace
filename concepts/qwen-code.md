# Qwen Code

Qwen Code is a command-line AI workflow tool adapted from [Gemini CLI](https://github.com/google-gemini/gemini-cli), optimized for [Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) models. It enables codebase understanding, editing, workflow automation, and advanced parser support for agentic coding tasks.

---

## Key Features

- **Code Understanding & Editing:** Query and edit large codebases beyond traditional context window limits.
- **Workflow Automation:** Automate operational tasks like handling pull requests and complex rebases.
- **Enhanced Parser:** Optimized for Qwen-Coder models.

---

## Quick Start

1. **Prerequisites:** [Node.js v20+](https://nodejs.org/en/download)

2. **Install:**

   ```sh
   npm install -g @qwen-code/qwen-code
   qwen --version
   qwen
   ```

   Or from source:

   ```sh
   git clone https://github.com/QwenLM/qwen-code.git
   cd qwen-code
   npm install
   npm install -g .
   ```

3. **API Configuration:**

   ```sh
   export OPENAI_API_KEY="your_api_key_here"
   export OPENAI_BASE_URL="your_api_base_url_here"
   export OPENAI_MODEL="your_api_model_here"
   ```

---

## Usage Examples

- Explore codebases: `qwen` in your project directory
- Refactor functions: `> Refactor this function to improve readability and performance`
- Automate workflows: `> Analyze git commits from the last 7 days, grouped by feature and team member`

---

## Related Projects

- [Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder): Agentic code model with long-context and multi-language support
- [Gemini CLI](https://github.com/google-gemini/gemini-cli): Original CLI workflow tool

---

## Troubleshooting & Contributing

- [Troubleshooting Guide](https://github.com/QwenLM/qwen-code/blob/main/docs/troubleshooting.md)
- [Contributing Guide](https://github.com/QwenLM/qwen-code/blob/main/CONTRIBUTING.md)

---

## License

[Apache-2.0](https://github.com/QwenLM/qwen-code/blob/main/LICENSE)

---

## External Links

- [Qwen Code GitHub](https://github.com/QwenLM/qwen-code)
- [Qwen3-Coder GitHub](https://github.com/QwenLM/Qwen3-Coder)
- [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli)

---

## See Also

- [AI Agents](./ai-agents.md)
- [Tool Use](./tool-use.md)
- [Workflow Automation](./workflow-automation.md)

---

## Inference Provider: Alibaba Cloud DashScope

Qwen3-Coder can be accessed via Alibaba Cloud’s DashScope platform using an OpenAI-compatible API endpoint.

- **Endpoint:** `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
- **Model Name:** `qwen3-coder-plus`
- **API Key:** Register and obtain your API key from [Alibaba Cloud Model Studio](https://modelstudio.console.alibabacloud.com/)

**Example Python usage:**

```python
from openai import OpenAI
client = OpenAI(
    api_key="YOUR_DASHSCOPE_API_KEY",
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen3-coder-plus",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Help me create a web page for an online bookstore."}
    ]
)
print(completion.choices[0].message.content.strip())
```

For local inference, download the model from [Hugging Face](https://huggingface.co/Qwen) or [ModelScope](https://modelscope.cn/organization/qwen) and deploy using frameworks like Transformers, vLLM, TGI, or SGLang.

---

## Inference Provider: OpenRouter

Qwen3-Coder is also available for hosted inference via [OpenRouter](https://openrouter.ai/qwen/qwen3-coder):

- **Model:** Qwen3-Coder-480B-A35B-Instruct
- **Context Length:** Up to 1M tokens
- **Pricing:** $1/M input tokens, $5/M output tokens (see OpenRouter for latest)
- **API:** Use OpenRouter's API to access the model directly, no need for Alibaba Cloud or DashScope.

For details and integration instructions, visit the [OpenRouter Qwen3-Coder page](https://openrouter.ai/qwen/qwen3-coder).

---
