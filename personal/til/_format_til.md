# 📋 TIL Article Format Specification

This document defines the actionable format for a "Today I Learned" (TIL) article in this repository. Follow this template for consistency, clarity, and discoverability.

---

## 1. Header & Navigation
- Add a navigation badge linking back to the TIL Hub:
  ```markdown
  [![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)
  ```
- Title: Use a clear, descriptive H1 heading
  ```markdown
  # How to Import a HuggingFace Model (GGUF) for Ollama
  ```
- Optional: Add a short summary or quote for context
  ```markdown
  > Ollama lets you run, customize, and manage LLMs locally. You can import models from HuggingFace (in GGUF format) and use them with your own prompts and templates.
  ```

---

## 2. Section Structure
- Use clear section headings (H2 or H3) for each step or concept
- Recommended sections:
  - Step-by-step instructions (e.g., Step 1, Step 2, ...)
  - Tips & Best Practices
  - Resources
  - Summary or Key Takeaways

---

## 3. Code & Commands
- Use fenced code blocks for commands, scripts, or config files
  ```markdown
  ```bash
  ollama run stablelm-2-zephyr-1_6b-Q4_1
  ```
  ```
- Label code blocks with the language for syntax highlighting

---

## 4. Lists & Tips
- Use bullet points for actionable tips, best practices, and troubleshooting
- Keep lists concise and focused on practical advice

---

## 5. Resources Section
- Include a "Resources" section at the end with relevant links
  ```markdown
  ## 📚 Resources
  - [Ollama Docs: Import from GGUF](https://github.com/ollama/ollama#customize-a-model)
  - [Ollama Modelfile Reference](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)
  - [Ollama CLI Reference](https://github.com/ollama/ollama#cli-reference)
  - [HuggingFace Model Hub](https://huggingface.co/models)
  ```

---

## 6. Footer & Completion
- End with a brief summary, encouragement, or next steps
  ```markdown
  **You can now run custom HuggingFace models locally with Ollama!**
  ```

---

## 7. Formatting Guidelines
- Use Markdown only (no HTML)
- Prefer clarity and brevity
- Use emoji for section headers if desired
- Ensure all links and file paths are correct

---

## Example
See [2024-03-02 ollama_import_model.md](2024-03-02%20ollama_import_model.md) for a complete example.
