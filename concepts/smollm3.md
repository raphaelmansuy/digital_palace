# SmolLM3: Small, Multilingual, Long-Context Reasoner (2025)

[Official Hugging Face Blog Post →](https://huggingface.co/blog/smollm3)

## Overview

**SmolLM3** is a fully open, 3B parameter language model released by Hugging Face in July 2025. It is designed for efficiency, multilingual support, and long-context reasoning, outperforming other 3B models and competing with larger 4B models like Qwen3 and Gemma3. SmolLM3 is notable for its:

- **Dual-mode reasoning**: Supports both reasoning (`/think`) and non-reasoning (`/no_think`) modes
- **Multilingual capabilities**: English, French, Spanish, German, Italian, Portuguese
- **Long context**: Handles up to 128k tokens using NoPE and YaRN
- **Open recipe**: Full training methodology, data mixtures, and engineering blueprint are public
- **Tool calling**: Supports XML and Python tool formats for agentic workflows
- **MLX support**: Official 5-bit quantized MLX port available ([see here](https://huggingface.co/mlx-community/SmolLM3-3B-5bit))

## Key Features

- **Architecture**: Transformer decoder with grouped-query attention (GQA), NoPE, and intra-document masking
- **Training**: 11T tokens, three-stage pretraining, mid-training for long context and reasoning, SFT, and APO alignment
- **Performance**: SoTA at 3B scale, competitive with 4B models, strong on knowledge, reasoning, math, coding, and multilingual benchmarks
- **Open Source**: Model weights, training configs, and evaluation code are available

## Resources

- [Official Blog Post](https://huggingface.co/blog/smollm3)
- [Base Model](https://hf.co/HuggingFaceTB/SmolLM3-3B-Base)
- [Instruct/Reasoning Model](https://hf.co/HuggingFaceTB/SmolLM3-3B)
- [Model Collection (quantized)](https://huggingface.co/collections/HuggingFaceTB/smollm3-686d33c1fdffe8e635317e23)
- [GitHub: Pretraining & Evaluation Code](https://github.com/huggingface/smollm)
- [MLX 5-bit Quantized Model (official port)](https://huggingface.co/mlx-community/SmolLM3-3B-5bit)
- [Awni Hannun X Announcement](https://x.com/awnihannun/status/1942686003455762544?s=12&t=TDcEu-9VmV2EvPkDUefXPg)

## How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "HuggingFaceTB/SmolLM3-3B"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

messages = [
    {"role": "system", "content": "/think"},
    {"role": "user", "content": "Explain gravity simply."}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt")
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0]))
```

- Use `/think` for reasoning mode, `/no_think` for direct answers.
- Tool calling: pass `xml_tools` or `python_tools` as arguments.

## Further Reading
- [SmolLM3 Blog Post](https://huggingface.co/blog/smollm3) (full methodology, benchmarks, and engineering details)
- [SmolLM3 GitHub](https://github.com/huggingface/smollm)

---

**Related:** [LLMs](./llms.md) | [2025 AI Updates](../reference/2025-ai-updates.md) | [Open Source Models](https://huggingface.co/models)
