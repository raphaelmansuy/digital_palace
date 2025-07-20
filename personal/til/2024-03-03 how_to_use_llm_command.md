# TIL: How to Use the LLM Command-Line Tool (2024-03-03)

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> **Interact with multiple LLMs from the command line** – Use the LLM CLI tool to work with OpenAI, Anthropic, Google Gemini, local models, and more from a unified interface.

---

## The Pain Point

Managing multiple LLM APIs and local models with different interfaces, authentication methods, and command structures makes AI experimentation complex and time-consuming.

---

## Step-by-Step Guide

### 1. Install LLM

Install using your preferred package manager:

```bash
pip install llm
# or
brew install llm
# or
pipx install llm
# or
uv tool install llm
```

### 2. Set API Keys

Configure keys for different providers:

```bash
llm keys set openai
llm keys set gemini
llm keys set anthropic
```

### 3. Basic Usage

Run simple prompts:

```bash
llm "Ten fun names for a pet pelican"
```

### 4. Use System Prompts

Add context or instructions with system prompts:

```bash
cat myfile.py | llm -s "Explain this code"
```

*The LLM CLI tool unifies access to multiple language models with a simple, consistent interface for AI experimentation and automation.*

### 5. Create and Use Templates

Save reusable prompts with parameters:

```bash
# Create a template
llm 'Summarize this: $input' --save summarize
llm --system 'Summarize this text in the voice of $voice' \
  --model gpt-4 -p voice GlaDOS --save summarize

# Use a template
cat text1.txt | llm -t summarize
llm -t summarize -p input @myfile.txt

# List templates
llm templates
```

### 6. Advanced Features

Interactive chat:

```bash
llm chat -m gpt-4.1
```

Extract text from images:

```bash
llm "extract text" -a scanned-document.jpg
```

Work with embeddings:

```bash
llm embed "Text to embed"
llm similar "Find similar text"
```

Use local models via plugins:

```bash
llm install llm-ollama
llm -m llama3.2:latest "What is the capital of France?"
```

---

## Troubleshooting

- If API keys aren't working, verify with: `llm keys list`
- For model issues, check available models: `llm models list`
- Install plugins for local models: `llm install llm-ollama`
- Use `llm --help` for complete command reference

---

## Security Considerations

- Never share your API keys or secrets in public scripts or repositories.
- Use environment variables to manage sensitive credentials.
- Regularly review and rotate API keys for all providers.

---

## Related Resources

- [LLM Documentation](https://llm.datasette.io/)
- [LLM Plugin Directory](https://llm.datasette.io/en/stable/plugins/directory.html)
- [Simon Willison's Blog](https://simonwillison.net/tags/llm/)
- [GitHub Repository](https://github.com/simonw/llm)
- [llm CLI Reference](https://llm.datasette.io/en/stable/help.html)
- [llm Templates](https://llm.datasette.io/en/stable/templates.html)

---

*⚡ Pro tip: Use templates and system prompts to automate repetitive tasks and supercharge your terminal workflow!*
