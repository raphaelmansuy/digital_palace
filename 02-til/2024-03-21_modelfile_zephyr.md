### Downloading a GGUF file from 🤗

```bash
huggingface-cli download bartowski/Starling-LM-7B-beta-GGUF Starling-LM-7B-beta-Q6_K.gguf --local-dir .
```

### Example of Modelfile for Ollama and Zephyr Model

```text
FROM ./Starling-LM-7B-beta-Q6_K.gguf 
# Set prompt template with system, user and assistant roles
TEMPLATE """{{ .System }}<|end_of_turn|>GPT4 Correct User: {{ .Prompt}}<|end_of_turn|>GPT4 Correct Assistant:"""
PARAMETER temperature 0
# sets the context window size to 16384, this controls how many tokens the LLM can use as context to generate the next token
PARAMETER num_ctx 16384
# sets a custom system message to specify the behavior of the chat assistant
SYSTEM You are the best assistant ever.
PARAMETER stop <|endoftext|>
PARAMETER stop <|end_of_turn|>
PARAMETER stop Human:
PARAMETER stop Assistant:
```

### Creating the model

```bash
ollama create "Starling-LM-7B-beta-Q6_K" -f Modelfile
```

### Running the model

```bash
ollama run Starling-LM-7B-beta-Q6_K:latest
```

