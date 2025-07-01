
[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

# How to Import a HuggingFace Model (GGUF) for Ollama

> Ollama lets you run, customize, and manage LLMs locally. You can import models from HuggingFace (in GGUF format) and use them with your own prompts and templates.

---

## 🪄 Step 1: Download the GGUF Model File

Use the [HuggingFace CLI](https://huggingface.co/docs/huggingface_hub/guides/download) to download a GGUF model:

```bash
huggingface-cli download stabilityai/stablelm-2-zephyr-1_6b stablelm-2-zephyr-1_6b-Q4_1.gguf --local-dir . --local-dir-use-symlinks False
```
Replace the model and file name as needed. (You can also download manually from the HuggingFace model page.)

---

## 📝 Step 2: Create a Modelfile

Create a file named `Modelfile` with the following content:

```Dockerfile
FROM ./stablelm-2-zephyr-1_6b-Q4_1.gguf

TEMPLATE "<|system|>{{ .System }}<|endoftext|><|user|>{{ .Prompt }}<|endoftext|><|assistant|>"
```
You can customize the `TEMPLATE` or add [parameters](https://github.com/ollama/ollama/blob/main/docs/modelfile.md#parameters) as needed.

---

## 🏗️ Step 3: Build the Model in Ollama

Run:

```bash
ollama create stablelm-2-zephyr-1_6b-Q4_1 -f Modelfile
```
Replace the model name and Modelfile path as needed.

---

## 🚀 Step 4: Run and Test Your Model

```bash
ollama run stablelm-2-zephyr-1_6b-Q4_1:latest
```
Or just:
```bash
ollama run stablelm-2-zephyr-1_6b-Q4_1
```

---

## 🧑‍💻 Tips & Best Practices

- **Model names**: Use lowercase, no spaces, and avoid special characters.
- **Modelfile**: You can add `PARAMETER` lines to set temperature, system prompts, etc.
- **List models**: `ollama list`
- **Show info**: `ollama show <model>`
- **Remove model**: `ollama rm <model>`
- **Update model**: `ollama pull <model>`
- **Copy model**: `ollama cp <model> <newname>`
- **Troubleshooting**: Check [Ollama issues](https://github.com/ollama/ollama/issues) for common problems.

---

## 📚 Resources

- [Ollama Docs: Import from GGUF](https://github.com/ollama/ollama#customize-a-model)
- [Ollama Modelfile Reference](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)
- [Ollama CLI Reference](https://github.com/ollama/ollama#cli-reference)
- [HuggingFace Model Hub](https://huggingface.co/models)

---

**You can now run custom HuggingFace models locally with Ollama!**

