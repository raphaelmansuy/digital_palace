# BertViz

BertViz is an interactive tool for visualizing attention in Transformer language models such as BERT, GPT2, or T5. It provides multiple views that offer unique lenses into the attention mechanism, helping researchers and developers understand how these models process and attend to input sequences.

---

## Key Features

- **Multiple Visualization Views:** Head view, model view, and neuron view for different perspectives on attention
- **Interactive Exploration:** Click and hover to explore attention patterns across layers and heads
- **HuggingFace Integration:** Supports most HuggingFace Transformer models out of the box
- **Jupyter/Colab Support:** Easy integration into notebooks for interactive analysis
- **Encoder-Decoder Support:** Works with models like BART, T5, and MarianMT
- **Customizable Display:** Dark/light modes, layer/head filtering, and HTML export options

---

## Visualization Views

### Head View

Visualizes attention for one or more attention heads in the same layer. Shows how individual heads attend to different parts of the input.

### Model View

Provides a bird's-eye view of attention across all layers and heads, allowing comparison of attention patterns throughout the model.

### Neuron View

Visualizes individual neurons in the query and key vectors, showing how they contribute to attention computation.

---

## Installation

```bash
pip install bertviz
```

For Jupyter Notebook support:

```bash
pip install jupyterlab ipywidgets
```

---

## Quick Start

### Basic Usage

```python
from transformers import AutoTokenizer, AutoModel, utils
from bertviz import model_view

utils.logging.set_verbosity_error()  # Suppress warnings

# Load model and tokenizer
model_name = "microsoft/xtremedistil-l12-h384-uncased"
model = AutoModel.from_pretrained(model_name, output_attentions=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Prepare input
input_text = "The cat sat on the mat"
inputs = tokenizer.encode(input_text, return_tensors='pt')
outputs = model(inputs)
attention = outputs[-1]  # Get attention weights

# Convert to tokens and visualize
tokens = tokenizer.convert_ids_to_tokens(inputs[0])
model_view(attention, tokens)
```

### Colab Usage

```python
!pip install bertviz
# Then use the same code as above
```

---

## Advanced Usage

### Encoder-Decoder Models

```python
from transformers import AutoTokenizer, AutoModel
from bertviz import model_view

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")
model = AutoModel.from_pretrained("Helsinki-NLP/opus-mt-en-de", output_attentions=True)

encoder_input_ids = tokenizer("She sees the small elephant.", return_tensors="pt", add_special_tokens=True).input_ids
with tokenizer.as_target_tokenizer():
    decoder_input_ids = tokenizer("Sie sieht den kleinen Elefanten.", return_tensors="pt", add_special_tokens=True).input_ids

outputs = model(input_ids=encoder_input_ids, decoder_input_ids=decoder_input_ids)

encoder_text = tokenizer.convert_ids_to_tokens(encoder_input_ids[0])
decoder_text = tokenizer.convert_ids_to_tokens(decoder_input_ids[0])

model_view(
    encoder_attention=outputs.encoder_attentions,
    decoder_attention=outputs.decoder_attentions,
    cross_attention=outputs.cross_attentions,
    encoder_tokens=encoder_text,
    decoder_tokens=decoder_text
)
```

### Neuron View Example

```python
from bertviz.transformers_neuron_view import BertModel, BertTokenizer
from bertviz.neuron_view import show

model_type = 'bert'
model_version = 'bert-base-uncased'
model = BertModel.from_pretrained(model_version, output_attentions=True)
tokenizer = BertTokenizer.from_pretrained(model_version, do_lower_case=True)

sentence_a = "The cat sat on the mat"
sentence_b = "The cat lay on the rug"

show(model, model_type, tokenizer, sentence_a, sentence_b, layer=2, head=0)
```

---

## Options and Customization

- **Display Mode:** `display_mode="light"` or `"dark"` (default)
- **Layer Filtering:** `include_layers=[5, 6]` to show only specific layers
- **Head Filtering:** `include_heads=[3, 5]` to show only specific heads
- **Default Selection:** `layer=2, heads=[3,5]` for initial display
- **Sentence Pairs:** `sentence_b_start=index` for BERT-style sentence pair visualization
- **HTML Export:** `html_action='return'` to get HTML for saving

---

## Limitations

- Designed for shorter inputs; may be slow with very long texts or large models
- Neuron view limited to BERT, GPT-2, and RoBERTa (requires custom model versions)
- Attention visualization doesn't necessarily explain model predictions directly
- Colab may disconnect with very long inputs

---

## Citation

```bibtex
@inproceedings{vig-2019-multiscale,
    title = "A Multiscale Visualization of Attention in the Transformer Model",
    author = "Vig, Jesse",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P19-3007",
    doi = "10.18653/v1/P19-3007",
    pages = "37--42",
}
```

---

## External Links

- [BertViz GitHub Repository](https://github.com/jessevig/bertviz)
- [Interactive Colab Tutorial](https://colab.research.google.com/drive/1hXIQ77A4TYS4y3UthWF-Ci7V7vVUoxmQ?usp=sharing)
- [Paper: A Multiscale Visualization of Attention in the Transformer Model](https://www.aclweb.org/anthology/P19-3007.pdf)
- [PyPI Package](https://pypi.org/project/bertviz/)

---

## See Also

- [LLMs](./llms.md)
- [Embeddings](./embeddings.md)
- [Presentation Tools](./presentation-tools.md)
- [Frameworks](./frameworks.md)

---

## License

Apache License 2.0

[Back to Concepts Hub](./README.md)
