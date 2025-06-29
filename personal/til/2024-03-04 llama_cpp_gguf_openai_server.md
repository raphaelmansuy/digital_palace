

## How to serve a gguf model file 

`llama-cpp-python` offers a web server which aims to act as a drop-in replacement for the OpenAI API. This allows you to use llama.cpp compatible models with any OpenAI compatible client (language libraries, services, etc).

[Documentation: llama-cpp-python](https://llama-cpp-python.readthedocs.io/en/latest/)
[Github](https://github.com/abetlen/llama-cpp-python)


```bash
pip install 'llama-cpp-python[server]' 
python3 -m llama_cpp.server --model models/7B/llama-model.gguf --chat_format functionary-v2
```


Example:

```bash


MODEL="~/.cache/lm-studio/models/MaziyarPanahi/Llama-2-7b-chat-hf-function-calling-v2-GGUF/Llama-2-7b-chat-hf-function-calling-v2.Q2_K.gguf"

python3 -m llama_cpp.server --model $MODEL --chat_format functionary-v2

```


## How to serve a function calling model


You need first to download first an AI model supporting function calling:

Example:

https://huggingface.co/meetkai/functionary-7b-v2-GGUF

```bash
python3 -m llama_cpp.server --model ./models/functionary-7b-v2.1.q4_0.gguf --chat_format functionary-v2 --hf_pretrained_model_name_or_path meetkai/functionary-7b-v2-GGUF
```

