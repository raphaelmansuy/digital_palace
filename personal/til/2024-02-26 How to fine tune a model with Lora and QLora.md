# 2024-02-26: Fine-Tuning Custom LLMs with LoRA and QLoRA

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

> LoRA (Low-Rank Adaptation) and QLoRA enable parameter-efficient fine-tuning of large language models by decomposing weight matrices into smaller trainable components, dramatically reducing memory requirements while maintaining model performance.

## The Pain Point

Fine-tuning large language models traditionally requires:

- Enormous computational resources and memory
- Training all model parameters (billions of weights)
- High costs for cloud GPU instances
- Long training times for full model fine-tuning
- Risk of catastrophic forgetting of pre-trained knowledge

LoRA solves this by allowing efficient fine-tuning with minimal additional parameters and memory.

## Step-by-Step Guide

### 1. Set Up the Environment

```bash
# Clone Lit-GPT repository for LoRA implementation
git clone https://github.com/Lightning-AI/lit-gpt
cd lit-gpt
pip install -r requirements.txt

# Install additional dependencies
pip install torch transformers datasets accelerate bitsandbytes
```

### 2. Choose and Prepare Your Base Model

```python
# Select a base model (not instruction-finetuned)
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "meta-llama/Llama-2-7b-hf"  # Example base model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
```

### 3. Configure LoRA Parameters

```python
# Key LoRA hyperparameters
lora_config = {
    "r": 16,           # Rank of adaptation (start with 8-16)
    "lora_alpha": 32,  # LoRA scaling parameter (usually 2x rank)
    "target_modules": ["q_proj", "v_proj", "k_proj", "o_proj"],  # Which layers to adapt
    "lora_dropout": 0.1,  # Dropout for LoRA layers
    "bias": "none",    # Whether to adapt bias parameters
}
```

### 4. Implement QLoRA for Memory Efficiency

```python
from transformers import BitsAndBytesConfig

# QLoRA configuration for 4-bit quantization
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

# Load model with quantization
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,
    device_map="auto"
)
```


### 5. Prepare Training Data

```python
# Example with Alpaca dataset
from datasets import load_dataset

dataset = load_dataset("tatsu-lab/alpaca")

def format_instruction(example):
    if example["input"]:
        return f"### Instruction:
{example['instruction']}

### Input:
{example['input']}

### Response:
{example['output']}"
    else:
        return f"### Instruction:
{example['instruction']}

### Response:
{example['output']}"

# Format and tokenize data
formatted_dataset = dataset["train"].map(
    lambda x: {"text": format_instruction(x)}
)
```

### 6. Configure Training with LoRA

```python
from peft import LoraConfig, get_peft_model, TaskType

# Apply LoRA to model
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    **lora_config  # Use config from step 3
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()  # Shows dramatic parameter reduction
```

### 7. Train the Model

```python
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="./lora-alpaca",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    warmup_steps=100,
    learning_rate=2e-4,  # Higher LR often works well with LoRA
    fp16=True,
    logging_steps=10,
    save_strategy="epoch",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=formatted_dataset,
    tokenizer=tokenizer,
)

trainer.train()
```

### 8. Save and Load LoRA Adapters

```python
# Save only the LoRA adapters (very small file)
model.save_pretrained("./lora-adapters")

# Load adapters later
from peft import PeftModel
base_model = AutoModelForCausalLM.from_pretrained(model_name)
lora_model = PeftModel.from_pretrained(base_model, "./lora-adapters")
```

## Troubleshooting

### Out of Memory Errors

- Reduce batch size and increase gradient accumulation steps
- Use QLoRA with 4-bit quantization
- Lower the LoRA rank (r parameter)
- Use gradient checkpointing: `gradient_checkpointing=True`

### Poor Fine-Tuning Results

- Increase LoRA rank (r) for more expressive power
- Adjust alpha parameter (try alpha = 2 * rank)
- Apply LoRA to more target modules
- Use learning rate scheduling with warmup

### Training Instability

- Lower learning rate (try 1e-4 instead of 2e-4)
- Add LoRA dropout for regularization
- Use AdamW optimizer with weight decay
- Monitor gradient norms and clip if necessary

## Related Resources

- [LoRA Paper](https://arxiv.org/abs/2106.09685) - Original Low-Rank Adaptation research
- [QLoRA Paper](https://arxiv.org/abs/2305.14314) - Quantized LoRA methodology
- [PEFT Library](https://github.com/huggingface/peft) - Parameter-Efficient Fine-Tuning toolkit
- [Lit-GPT Repository](https://github.com/Lightning-AI/lit-gpt) - Lightning AI's LoRA implementation
- [LoRA Insights Tutorial](https://lightning.ai/pages/community/lora-insights/) - Comprehensive LoRA guide by Sebastian Raschka

