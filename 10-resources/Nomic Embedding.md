![](assets/Pasted%20image%2020240226162014.png)


Nomic has introduced Nomic Embed, an open-source text embedding model that surpasses OpenAI's Ada-002 and text-embedding-3-small in performance. This model, which supports a context length of 8192, is fully reproducible and auditable, with its weights, training code, and data released under the Apache-2 license. Nomic Embed is available for production workloads through the Nomic Atlas Embedding API, including 1 million free tokens, and is also offered in a secure enterprise version.

Text embeddings are crucial for NLP applications, such as retrieval-augmented generation and semantic search, by encoding semantic information into vectors. Unlike OpenAI's Ada, which is closed source and non-auditable, Nomic Embed provides transparency and outperforms other open-source models that are either impractical due to size or underperforming.

Nomic Embed was trained using a multi-stage contrastive learning pipeline, starting with a BERT initialization and extending the context length to 2048. The model was trained using Deepspeed and FlashAttention, with several optimizations like Rotary Position Embeddings and SwiGLU activations.

The model was evaluated on the Massive Text Embedding Benchmark (MTEB) and other benchmarks, showing superior performance in the 100M parameter class unsupervised model category. It also demonstrated competitive results against models in the 7B parameter class and those trained specifically for benchmarks.

Nomic Embed's release aims to provide a performant, auditable text embedding model for enterprise use. The model and data are accessible through the Nomic Atlas Embedding API or by downloading the open-source model weights.


[https://blog.nomic.ai/posts/nomic-embed-text-v1](https://blog.nomic.ai/posts/nomic-embed-text-v1)

#embeddings #ai
