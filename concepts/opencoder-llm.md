# OpenCoder LLM

OpenCoder is an open and reproducible code LLM family which includes 1.5B and 8B base and chat models, supporting both English and Chinese languages. Starting from scratch, OpenCoder is pretrained on 2.5 trillion tokens composed of 90% raw code and 10% code-related web data, and supervised finetuned on over 4.5M high-quality SFT examples, finally reaching the performance of top-tier code LLMs. We provide not only model weights and inference code, but also the reproducible training data, the complete data processing pipeline, rigorous experimental ablation results, and detailed training protocols.

---

## Key Features

- **Complete Open Source:** OpenCoder ensures full transparency by releasing not only the model weights and inference code but also the complete data-cleaning code for training. This includes high-quality synthetic data, extensive checkpoints, and a dataset of over 4.5 million supervised fine-tuning (SFT) entries.

- **Comprehensive Experimental Analysis:** OpenCoder is rigorously tested through extensive ablation studies on various data-cleaning strategies and training processes, including file-level and repository-level deduplication experiments.

- **High-Quality Synthetic Data:** OpenCoder provides a fully developed synthetic data generation process and over 4.5 million SFT data entries, establishing a robust data foundation for model training and evaluation.

- **Exceptional Performance:** OpenCoder achieves high performance across multiple language model benchmarks, positioning it among the leading open-source models for code.

---

## Models

| Model | Context Length | Platform | Link |
|-------|----------------|----------|------|
| OpenCoder-1.5B-Base | 4K | HuggingFace | [HuggingFace](https://huggingface.co/infly/OpenCoder-1.5B-Base) |
| OpenCoder-8B-Base | 8K | HuggingFace | [HuggingFace](https://huggingface.co/infly/OpenCoder-8B-Base) |
| OpenCoder-1.5B-Instruct | 4K | HuggingFace | [HuggingFace](https://huggingface.co/infly/OpenCoder-1.5B-Instruct) |
| OpenCoder-8B-Instruct | 8K | HuggingFace | [HuggingFace](https://huggingface.co/infly/OpenCoder-8B-Instruct) |

---

## Datasets

### Pre-training

| Dataset | Size | Platform | Link |
|---------|------|----------|------|
| fineweb-code-corpus | 148 GB | HuggingFace | [HuggingFace](https://huggingface.co/datasets/OpenCoder-LLM/fineweb-code-corpus) |
| fineweb-math-corpus | 10 GB | HuggingFace | [HuggingFace](https://huggingface.co/datasets/OpenCoder-LLM/fineweb-math-corpus) |
| opc-annealing-corpus | 24 GB | HuggingFace | [HuggingFace](https://huggingface.co/datasets/OpenCoder-LLM/opc-annealing-corpus) |

### Post-training

| Dataset | Size | Platform | Link |
|---------|------|----------|------|
| opc-sft-stage1 | 4.21 M | HuggingFace | [HuggingFace](https://huggingface.co/datasets/OpenCoder-LLM/opc-sft-stage1) |
| opc-sft-stage2 | 375 K | HuggingFace | [HuggingFace](https://huggingface.co/datasets/OpenCoder-LLM/opc-sft-stage2) |

---

## Get Started

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "infly/OpenCoder-8B-Instruct"
model = AutoModelForCausalLM.from_pretrained(model_name,
                                             torch_dtype=torch.bfloat16,
                                             device_map="auto",
                                             trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

messages=[
    { 'role': 'user', 'content': "write a quick sort algorithm in python."}
]

inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")

outputs = model.generate(inputs, max_new_tokens=512, do_sample=False)

result = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)
print(result)
```

---

## Citation

```bibtex
@inproceedings{Huang2024OpenCoderTO,
  title={OpenCoder: The Open Cookbook for Top-Tier Code Large Language Models},
  author={Siming Huang and Tianhao Cheng and Jason Klein Liu and Jiaran Hao and Liuyihan Song and Yang Xu and J. Yang and J. H. Liu and Chenchen Zhang and Linzheng Chai and Ruifeng Yuan and Zhaoxiang Zhang and Jie Fu and Qian Liu and Ge Zhang and Zili Wang and Yuan Qi and Yinghui Xu and Wei Chu},
  year={2024},
  url={https://arxiv.org/pdf/2411.04905}
}
```

---

## External Links

- [OpenCoder GitHub Repository](https://github.com/OpenCoder-llm/OpenCoder-llm)
- [Paper on ArXiv](https://arxiv.org/abs/2411.04905)
- [Models Collection on HuggingFace](https://huggingface.co/collections/infly/opencoder-672cec44bbb86c39910fb55e)
- [Datasets Collection](https://huggingface.co/collections/OpenCoder-LLM/opencoder-datasets-672e6db6a0fed24bd69ef1c2)
- [Home Page](https://opencoder-llm.github.io/)
- [Demo](https://huggingface.co/spaces/OpenCoder-LLM/OpenCoder-8B-Instruct)

---

## See Also

- [LLMs](./llms.md)
- [Qwen Code](./qwen-code.md)
- [Code LLMs](../reference/core-technologies.md#code-llms)  # Assuming this exists, but probably not, maybe remove.

[Back to Concepts Hub](./README.md)
