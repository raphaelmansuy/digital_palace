

## How to serve a gguf model file 

`llama-cpp-python` offers a web server which aims to act as a drop-in replacement for the OpenAI API. This allows you to use llama.cpp compatible models with any OpenAI compatible client (language libraries, services, etc).

[Documentation: llama-cpp-python](https://llama-cpp-python.readthedocs.io/en/latest/)
[Github](https://github.com/abetlen/llama-cpp-python)


```bash
pip install 'llama-cpp-python[server]' 
python3 -m llama_cpp.server --model models/7B/llama-model.gguf
```
