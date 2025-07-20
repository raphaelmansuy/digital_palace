# Framework for LLM Applications

## LangChain 🔗 🦜

LangChain is an open-source framework created to simplify the development of applications using large language models (LLMs). It provides tools and interfaces that make it easier to build LLM-powered apps that are:

- **Data-aware**: Easily connect LLMs to external data sources like databases, APIs, documents etc. LangChain has connectors for common data sources.

- **Modula**r: LangChain provides common interfaces around prompts, models, knowledge retrieval etc. These modules can be mixed and matched.

- **Customizable**: Support for different LLM models like GPT-3, Codex etc. Prompts can be optimized for specific apps.

- **Scalable**: LangChain makes it easy to deploy LLM apps on platforms like AWS Lambda. The apps can be scaled up as needed.

Some example use cases of LangChain include building chatbots, QA systems, summarization tools, code generation and more. The documentation contains code snippets and templates to build such applications.

Read more about LangChain [here](https://python.langchain.com).

## LLamaIndex 🦙

LLamaIndex provides a data framework to ingest and structure private or domain-specific data to be used with LLMs. It allows:

- **Connecting to data sources** like databases, APIs, files etc. using flexible connectors.

- **Indexing** the ingested data for easy retrieval and association.

- **Querying** the indexed data in natural language from an LLM.

- **Retrieving** relevant data as context for LLM prompts.

- **Caching** indexed data for low latency access.

LLamaIndex has client libraries that make it easy to integrate into LLM apps built with frameworks like LangChain. The data ingestion, indexing and retrieval happen under the hood.

Developers can use LLamaIndex to quickly add private/custom data to enhance existing LLMs. It avoids the need to retrain models, while allowing them to provide personalized and data-driven responses.

Read more about LLamaIndex [here](https://www.llamaindex.ai).

[A guide about how to start with LLamaIndex](../llama_index/README.md).

## Additional Resources

- **[Agents Towards Production (Nir Diamant, GitHub)](https://github.com/NirDiamant/agents-towards-production)** - Comprehensive, code-first playbook for building and deploying GenAI agents. Features hands-on tutorials for orchestration, memory, security, monitoring, deployment, and more. Ideal for teams seeking production-grade agent systems.
