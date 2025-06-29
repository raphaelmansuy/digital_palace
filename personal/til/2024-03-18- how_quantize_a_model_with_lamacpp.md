
## Quantizing Large Language Models with llama.cpp

Quantization is a technique to reduce the memory footprint and computational demands of LLMs while maintaining performance. This tutorial walks through the steps to quantize a model using llama.cpp.

### Prerequisites
- Install git-lfs to download large files:
```bash 
brew install git-lfs
git lfs install
```

### Steps

1. Clone the llama.cpp project and run make:
```bash
git clone https://github.com/ggerganov/llama.cpp 
cd llama.cpp
make
```

2. Download a model from HuggingFace, e.g. Nous-Hermes-2-Mistral-7B-DPO:
```bash
git clone https://huggingface.co/NousResearch/Nous-Hermes-2-Mistral-7B-DPO nous-hermes-2-mistral-7B-DPO
mv nous-hermes-2-mistral-7B-DPO models/
```

3. Convert the model to the standard GGML FP16 format:
```bash
python3 convert.py models/nous-hermes-2-mistral-7B-DPO/
```

4. Quantize the model to n-bits using various methods:
- 4-bit quantization (Q4_K_M):
```bash 
./quantize ./models/nous-hermes-2-mistral-7B-DPO/ggml-model-f16.gguf ./models/nous-hermes-2-mistral-7B-DPO/ggml-model-Q4_K_M.gguf Q4_K_M
```
- 3-bit quantization (Q3_K_M):  
```bash
./quantize ./models/nous-hermes-2-mistral-7B-DPO/ggml-model-f16.gguf ./models/nous-hermes-2-mistral-7B-DPO/ggml-model-Q3_K_M.gguf Q3_K_M
```
- 2-bit quantization (Q2_K):
```bash
./quantize ./models/nous-hermes-2-mistral-7B-DPO/ggml-model-f16.gguf ./models/nous-hermes-2-mistral-7B-DPO/ggml-model-Q2_K.gguf Q2_K  
```

5. Evaluate the quantized model:
- Run batched bench to compare performance:
```bash
./batched-bench ./models/nous-hermes-2-mistral-7B-DPO/ggml-model-Q4_K_M.gguf 2048 0 999 128,256,512 128,256 1,2,4,8,16,32
```
- Calculate perplexity (takes ~1 hour):  
```bash
./perplexity -m ./models/nous-hermes-2-mistral-7B-DPO/ggml-model-Q2_K.gguf -f /path/to/test-data.parquet
```

6. Run inference on the quantized model:
```bash
./main -m ./models/nous-hermes-2-mistral-7B-DPO/ggml-model-Q4_K_M.gguf -n 128  
```

By following these steps, you can quantize large language models to reduce memory usage and improve inference speed while preserving performance. Experiment with different quantization methods to find the optimal balance for your use case.

