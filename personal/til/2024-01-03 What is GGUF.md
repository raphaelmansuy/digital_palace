# What is GGUF ?

[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

[# GGUF, the long way around by Vicky Boykis](https://vickiboykis.com/2024/02/28/gguf-the-long-way-around/)

 [GGUF (GPT-Generated Unified Format)](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)

**Article summary : Understanding and Using GGUF for Local LLM Inference**

**Introduction**

Large language models (LLMs) have become a cornerstone of modern AI, and their deployment can vary from cloud-based API endpoints to local inference on devices. For local inference, especially on Apple Silicon, GGUF (GPT-Generated Unified Format) is a file format optimized for this purpose. This tutorial will guide you through the basics of machine learning models, serialization, and how to use GGUF with `llama.cpp` for local LLM inference.

**What is a Machine Learning Model?**

A machine learning model is essentially a file or collection of files that contain the architecture, weights, and biases of a model. These are the result of a training process where the model learns from data. In the context of LLMs, we're often dealing with transformer models that process natural language data.

**Serialization of Machine Learning Models**

Serialization is the process of converting an in-memory model to a format that can be saved to disk. This allows the model to be reloaded and used later, which is crucial for long training processes or deploying models for inference.

**The Role of PyTorch and Pickle**

PyTorch is a popular framework for training machine learning models, and it uses Python's `pickle` module for serialization. However, `pickle` has security concerns because it can execute arbitrary code during deserialization.

**From Pickle to Safetensors**

To address the security issues of `pickle`, the `safetensors` library was developed. It's a safer and more efficient alternative for serializing tensor data, which is the primary data type in deep learning models.

**GGUF: A Format for Local Inference**

GGUF is a file format designed for efficient local inference of LLMs, particularly on Apple Silicon. It contains model metadata and tensor data in a single file, with a key-value structure that supports backward compatibility.

**Using `llama.cpp` with GGUF**

`llama.cpp` is a C/C++-based LLM inference engine that uses GGUF files for local inference. Here's a basic example of how to use it:

1. Compile `llama.cpp` with the command `make -j`.
2. Run the inference with `./main -m model.gguf -p "Your prompt here"`.

Replace `model.gguf` with the path to your GGUF file and `"Your prompt here"` with the text you want the model to process.

**Conclusion**

Understanding the evolution of machine learning model serialization and the development of GGUF is crucial for deploying LLMs locally, especially on devices with Apple Silicon. With `llama.cpp` and GGUF, you can efficiently run inference tasks on your local machine, leveraging the power of LLMs without relying on cloud services.

For more detailed information on GGUF and `llama.cpp`, refer to the official documentation and explore the codebase to gain a deeper understanding of the implementation and usage.
