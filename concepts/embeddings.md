# Embeddings

Embeddings are numerical vector representations of words, sentences, or documents that capture semantic meaning and relationships. They are essential for search, retrieval, clustering, and enabling LLMs to understand and process language at scale.

---

## 📖 Learn More

- [Embeddings & Vector Operations](../reference/core-technologies.md#embeddings--vector-operations)
- [What are Embeddings? (Vicki Boykis Book)](https://vickiboykis.com/what_are_embeddings/)
- [Design Patterns for LLM Applications](../reference/techniques/dessign_patterns_for_llm_applications/README.md#what-is-embedding)
- [Fine-tuning and Advanced Embeddings](https://finetuning.baulab.info/)
- [Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka)
- [Integrating Long-Term Memory with Gemini 2.5 (Philipp Schmid)](https://www.philschmid.de/gemini-with-memory) — Example of using embeddings for long-term conversational memory

---

## 🛠️ Key Frameworks & Tools

- [Weaviate](https://weaviate.io/) — Vector database
- [Qdrant](https://qdrant.tech/) — Vector similarity search
- [LlamaIndex](https://www.llamaindex.ai/) — Embedding integration
- [Cohere](https://txt.cohere.com/int8-binary-embeddings/) — Binary embeddings
- [PGVector CloudSQL GCP](https://github.com/sciences44/pgvector_cloudsql_gcp) — PostgreSQL with PGVector on Google Cloud SQL (Infrastructure-as-Code)

---

## 🧠 Core Concepts

- **Vector Search:** [Vector & Search Technologies](../reference/core-technologies.md#vector--search-technologies)
- **Chunking & Retrieval:** [RAG Systems](./rag.md)
- **Document Processing:** [Document Processing](../reference/core-technologies.md#document-processing)

---

## 🚀 Best Practices & Next Steps

- Start with [Embeddings & Vector Operations](../reference/core-technologies.md#embeddings--vector-operations)
- Explore [What are Embeddings?](https://vickiboykis.com/what_are_embeddings/)
- See [Learning Pathways](./learning-pathways.md) for skill progression

[Back to Concepts Hub](./README.md)

---

## 🚀 Gemini Embedding (Google, 2025)

**Gemini Embedding** (`gemini-embedding-001`) is Google’s state-of-the-art, multilingual embedding model, now generally available via the [Gemini API](https://ai.google.dev/gemini-api/docs/embeddings) and Vertex AI. It supports 100+ languages, code, and advanced domains, and consistently ranks at the top of the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard).

**Key features:**
**Key features:**

- Matryoshka Representation Learning (MRL): Flexible output dimensions (3072, 1536, 768, etc.)
- High performance on retrieval, classification, clustering, and RAG
- Free and paid tiers ([pricing](https://ai.google.dev/gemini-api/docs/pricing)), generous [rate limits](https://ai.google.dev/gemini-api/docs/rate-limits)
- [Technical report (arXiv)](https://arxiv.org/abs/2503.07891)

**Quickstart Example:**

**Quickstart Example:**

```python
from google import genai
client = genai.Client()
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents="What is the meaning of life?")
print(result.embeddings)
```

**Resources:**
**Resources:**

- [Official announcement](https://developers.googleblog.com/en/gemini-embedding-available-gemini-api/)
- [Embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [Quickstart notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb)
- [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard)
- [arXiv technical report](https://arxiv.org/abs/2503.07891)


**Best practice:** Use the recommended output dimensions (3072, 1536, or 768) for optimal quality and efficiency. See the docs for advanced usage, batch mode, and integration with vector databases.
