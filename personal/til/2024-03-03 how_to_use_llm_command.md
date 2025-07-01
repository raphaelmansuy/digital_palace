

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

# How to use the `llm` Command-Line Tool

> **llm** is a powerful CLI and Python library for interacting with OpenAI, Anthropic, Google Gemini, Meta Llama, and dozens of other LLMs—both via remote APIs and local models (Ollama, etc.).

---

## 🚀 Quick Start

Install with pip, Homebrew, pipx, or uv:

```bash
pip install llm
# or
brew install llm
# or
pipx install llm
# or
uv tool install llm
```

Set your API key (for OpenAI, Gemini, Anthropic, etc.):

```bash
llm keys set openai
llm keys set gemini
llm keys set anthropic
```

---

## 🧠 Basic Usage

- **Run a prompt:**
  ```bash
  llm "Ten fun names for a pet pelican"
  ```
- **Use a specific model:**
  ```bash
  llm -m "mistral:latest" "Write a haiku about clouds."
  llm -m stablelm-2-zephyr-1_6b-Q4_1 "Summarize this text: ..."
  ```
- **Set the default model:**
  ```bash
  llm models default stablelm-2-zephyr-1_6b-Q4_1
  ```
- **Use a system prompt:**
  ```bash
  cat myfile.py | llm -s "Explain this code"
  pbpaste | llm -s "summarize this:" -m mistral:latest | tee /dev/tty | pbcopy
  ```

---

## 📝 Templates

Templates let you save and reuse prompts with parameters.

- **Create a template:**
  ```bash
  llm 'Summarize this: $input' --save summarize
  llm -s 'Summarize this' --save summarize
  llm --system 'Summarize this text in the voice of $voice' \
    --model gpt-4 -p voice GlaDOS --save summarize
  ```
- **Use a template:**
  ```bash
  cat text1.txt | llm -t summarize
  llm -t summarize -p input @myfile.txt
  ```
- **List templates:**
  ```bash
  llm templates
  ```

---

## 🔧 Advanced Features

- **Interactive chat:**
  ```bash
  llm chat -m gpt-4.1
  ```
- **Extract text from images:**
  ```bash
  llm "extract text" -a scanned-document.jpg
  ```
- **Work with embeddings:**
  ```bash
  llm embed "Text to embed"
  llm similar "Find similar text"
  ```
- **Use plugins for local models:**
  ```bash
  llm install llm-ollama
  llm -m llama3.2:latest "What is the capital of France?"
  ```
- **Count tokens:**
  ```bash
  cat my-file.txt | ttok
  ```
- **Summarize a webpage:**
  ```bash
  curl -s https://www.nytimes.com/ | strip-tags .story-wrapper | llm -s 'summarize the news' -m stablelm2
  ```
- **Search in codebase and analyze:**
  ```bash
  symbex 'test*csv*' | llm --system 'based on these tests guess what this tool does'
  ```

---

## 📚 Resources

- [llm GitHub](https://github.com/simonw/llm)
- [llm Documentation](https://llm.datasette.io/en/stable/)
- [llm Plugins](https://llm.datasette.io/en/stable/plugins/index.html)
- [llm Templates](https://llm.datasette.io/en/stable/templates.html)
- [llm CLI Reference](https://llm.datasette.io/en/stable/help.html)

---

**llm brings the power of LLMs to your terminal—script, automate, and analyze with ease!**

**Using the system prompt**

```bash
 pbpaste | llm -s "summarize this:"  -m mistral:latest | tee /dev/tty | pbcopy
 ```

## Create template

**Using a prompt**

```bash 
llm 'Summarize this: $input' --save summarize
```

**Using a system prompt**

```bash 
llm  -s 'Summarize this' --save summarize
```

**Template with parameters**

```bash
llm --system 'Summarize this text in the voice of $voice' \
  --model gpt-4 -p voice GlaDOS --save summarize
  ```

**Using the template with parameter**

```bash
llm --system 'Summarize this text in the voice of $voice' \
  --model gpt-4 -p voice GlaDOS --save summarize
  ```
## Using a template

```bash
cat text1.text | llm -t summarize
```

### Save a template

```bash
llm -m stablelm-2-zephyr-1_6b-Q4_1 -s "Format as markown:" --save markdown
```


### Useful

**Format as markdown, but don't interpret the prompt**

```bash
pbpaste | llm -s "You are a prompt engineer, with 30 years of experience, Just format the input text using the markdown format. Text to format:"  -m mistral:latest | tee /dev/tty | pbcopy
```

**Summary of Webpage**

```bash
curl -s https://www.nytimes.com/ \

  | strip-tags .story-wrapper \

  | llm -s 'summarize the news' -m stablelm2
```

**Count the number of tokens**

```bash
cat my-file.txt | ttok
```

**Searching in a code base**

```bash
symbex 'test*csv*' | \
  llm --system 'based on these tests guess what this tool does'
  ```
  