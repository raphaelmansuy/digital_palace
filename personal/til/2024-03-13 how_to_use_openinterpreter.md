
# 2024-03-13: Using Open Interpreter for AI Code Execution

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> Open Interpreter lets language models run code locally, enabling them to work with your computer, filesystem, and internet to complete complex tasks through natural language conversation.

## The Pain Point

Traditional AI assistants can only generate code but can't execute it or interact with your system. When you need to:

- Process local files or data
- Automate complex multi-step tasks
- Web scrape or download content
- Analyze data and generate reports
- Interact with your system and applications

You typically have to copy-paste code manually and handle execution yourself, breaking the conversational flow.

## Step-by-Step Guide

### 1. Install Open Interpreter

```bash
# Install via pip
pip install open-interpreter

# Or install with additional dependencies
pip install open-interpreter[local]
pip install open-interpreter[server]
```

### 2. Basic Usage with Different Models

```bash
# Use with OpenAI GPT models (requires OPENAI_API_KEY)
interpreter

# Specify different models
interpreter --model gpt-4
interpreter --model gpt-3.5-turbo

# Use with Claude (requires ANTHROPIC_API_KEY)
interpreter --model claude-3-sonnet
interpreter --model ollama/mistral
```

### 3. Configure API Keys

```bash
# Set environment variables
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key"

# Or set them in session
interpreter --model gpt-4 --api_key your-key-here
```

### 4. Example Tasks

#### Web Scraping and Data Processing

```bash
interpreter
```

Then give instructions like:

```text
Download the latest AI research papers from arXiv about "artificial intelligence" 
submitted today. Save them to a file called "YYYY-MM-DD-arxiv.md" and format 
as a markdown table with columns:
- arXiv number and link
- title  
- authors
- abstract
- submitted date

Use this URL: https://arxiv.org/search/cs?query=artificial+intelligence&searchtype=all&abstracts=show&order=-submitted_date&size=200
```

#### File Processing

```text
Analyze all Python files in the current directory, count lines of code, 
identify imports, and create a summary report in JSON format.
```

#### Data Analysis

```text
Load the CSV file 'sales_data.csv', clean the data, create visualizations 
of monthly trends, and save the plots as PNG files.
```

## Troubleshooting

### Permission Errors

- Run interpreter with appropriate permissions for file operations
- Check that API keys are correctly set in environment variables
- Ensure local models are properly installed and accessible

### Model Not Responding

- Verify internet connection for cloud models
- Check API key validity and quota limits
- For local models, ensure sufficient RAM and GPU resources

### Code Execution Issues

- Review generated code before allowing execution
- Use `--safe_mode` for untrusted operations  
- Check file paths and permissions for file operations

## Related Resources

- [Open Interpreter GitHub](https://github.com/KillianLucas/open-interpreter) - Main repository and documentation
- [Open Interpreter Docs](https://docs.openinterpreter.com/) - Comprehensive usage guide
- [Ollama](https://ollama.ai/) - Local model runtime for privacy-focused usage
- [LM Studio](https://lmstudio.ai/) - Alternative local model interface
