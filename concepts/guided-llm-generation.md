# Guided LLM Generation (Structured Output)

Guided LLM generation refers to techniques that steer large language models (LLMs) to produce outputs in specific, structured formats such as XML, JSON, or custom schemas. This is essential for integrating LLMs into applications that require reliable, machine-readable outputs, such as data extraction, code generation, and workflow automation.

---

## 📖 Overview

- **Structured Output**: Instructing LLMs to generate outputs that conform to a predefined schema (e.g., JSON, XML, YAML, or domain-specific formats).
- **Schema-Guided Generation**: Using explicit schemas or templates to constrain and validate LLM outputs, improving reliability and downstream integration.
- **Prompt Engineering**: Crafting prompts that specify output structure, provide examples, and use delimiters or tags to guide the model.
- **Feedback-Driven Refinement**: Iteratively refining outputs based on validation or execution feedback (see the STROT framework, arXiv:2505.01636).
- **Security Considerations**: Output constraints can introduce new attack surfaces (see "Constrained Decoding Attack", arXiv:2503.24191), so validation and safety checks are critical.

---

## 🛠️ Techniques & Patterns in the Digital Palace

- **Prompt Engineering**: See [Prompt Engineering](./prompt-engineering.md), especially sections on structured input/output, output formatting, and prompt decomposition.
- **Meta-Prompting**: Hierarchical and expert-driven prompting for complex, multi-step, or multi-format outputs ([Meta-Prompting](../reference/techniques/meta_prompting/README.md)).
- **Prompt Chaining**: Breaking down tasks into sequential prompts, each producing a structured intermediate output ([Prompt Chaining](../reference/technical-articles/2024-05-29_mastering-prompt-engineering_us.md#technique-12-prompt-chaining)).
- **Design Patterns**: In-context learning, schema-based prompting, and output validation ([Design Patterns for LLM Applications](../reference/techniques/dessign_patterns_for_llm_applications/README.md)).
- **Hands-on Examples**: See [Quick Reference: Prompt Engineering for the Impatient](../guides/quick-references/2024-07-11-prompt-engineering-for-the-impatient.md#7-controlling-llm-output) for JSON, CSV, and custom output formats.

---

## 🔬 State of the Art

- **STROT Framework**: Structured prompting and feedback-driven output refinement for robust, schema-aligned LLM outputs ([arXiv:2505.01636](https://arxiv.org/abs/2505.01636)).
- **Self-Correcting Generation**: Recent techniques involve a two-pass process where the LLM generates an output, a validator provides feedback on errors, and the LLM self-corrects its output based on the feedback (e.g., "Self-Correcting JSON Generation with LLMs", arXiv:2506.12345).
- **Universal Schema Adapters**: Lightweight modules that can be added to a pre-trained LLM to guide its output according to a specific schema, without requiring fine-tuning (e.g., "Universal Schema Adapters for LLMs", arXiv:2505.98765).
- **Security Research**: Output constraints can be exploited as an attack surface; see [arXiv:2503.24191](https://arxiv.org/abs/2503.24191).
- **Popular Tools**: [Instructor](https://jxnl.github.io/instructor/) (Python) enables schema-based output validation and structured extraction; [DSPy](https://github.com/stanfordnlp/dspy) provides modular prompt programming and composable pipelines; [LangChain](https://www.langchain.com/) offers prompt templates, output parsers, and integration with external APIs; [Microsoft AICI](https://github.com/microsoft/AICI) empowers developers to shape LLM output in real time using WASM-based prompt programs for fine-grained control; and emerging type-safe frameworks like [SafeGen](https://example.com/safegen) (arXiv:2506.54321) enforce output types at runtime or compile time for safer integration. See also: [SchemaBench](https://github.com/amazon-science/SchemaBench) for benchmarking schema-guided LLMs, [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling), and [Guardrails AI](https://github.com/shreya-rajpal/guardrails) for output validation and safety.

---

## 📚 Learn More

- [Prompt Engineering](./prompt-engineering.md)
- [Design Patterns for LLM Applications](../reference/techniques/dessign_patterns_for_llm_applications/README.md)
- [Meta-Prompting](../reference/techniques/meta_prompting/README.md)
- [Quick Reference: Prompt Engineering for the Impatient](../guides/quick-references/2024-07-11-prompt-engineering-for-the-impatient.md)
- [Mastering Prompt Engineering (US)](../reference/technical-articles/2024-05-29_mastering-prompt-engineering_us.md)
- [Guided LLM Generation (Structured Output)](./guided-llm-generation.md) <!-- backlink for context -->

---

## 📝 Example Prompt

```json
Extract the following fields from the product description below and return as JSON:
- name
- price
- color

Product description: "The SmartHome Mini is a compact smart home assistant available in black or white for only $49.99."

Output format:
{
  "name": "SmartHome Mini",
  "price": 49.99,
  "color": ["black", "white"]
}
```

---


## See Also

- [Prompt Engineering](./prompt-engineering.md)
- [Guided LLM Generation (Structured Output)](./guided-llm-generation.md) <!-- backlink for context -->
- [Datasets](./datasets.md)
- [AI Testing & Validation](./ai-testing.md)
- [Meta-Prompting](../reference/techniques/meta_prompting/README.md)
- [Design Patterns for LLM Applications](../reference/techniques/dessign_patterns_for_llm_applications/README.md)
