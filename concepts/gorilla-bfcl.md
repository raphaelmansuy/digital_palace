# Berkeley Function Calling Leaderboard (BFCL) / Gorilla LLM Leaderboard

The [Berkeley Function Calling Leaderboard (BFCL)](https://gorilla.cs.berkeley.edu/leaderboard.html) is a public benchmark and leaderboard for evaluating large language models (LLMs) on their ability to perform function/tool calling and agentic reasoning. Developed by UC Berkeley, it provides a rigorous, real-world evaluation of LLMs' tool use, multi-turn interactions, and agentic capabilities.

---

## Key Features

- **Function Calling Evaluation:** Tests LLMs on their ability to call functions (tools) accurately, both natively and via prompt-based workarounds
- **Agentic Evaluation:** Includes multi-turn and holistic agentic tasks, not just single function calls
- **Real-World Data:** Benchmarks are based on real-world use cases and updated regularly
- **Open Leaderboard:** Publicly ranks models by accuracy, cost, and latency
- **Transparent Methodology:** Detailed blogs and open-source code/data for reproducibility

---

## Evaluation Methodology

- **Datasets:** Real-world function calling and agentic tasks
- **Metrics:** Overall accuracy, cost (USD), latency (seconds), and sub-category breakdowns
- **Native vs. Prompted:** Distinguishes between models with native function calling and those using prompt-based approaches
- **Multi-Turn & Web Search:** Latest versions include multi-turn and web search agentic evaluation

---

## Resources & References

- [BFCL Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [BFCL-v1: AST as Evaluation Metric](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html)
- [BFCL-v2: Enterprise & OSS Functions](https://gorilla.cs.berkeley.edu/blogs/12_bfcl_v2_live.html)
- [BFCL-v3: Multi-Turn Interactions](https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html)
- [BFCL-v4: Agentic Evaluation](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html)
- [Code & Data](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard)
- [BFCL Results](https://github.com/HuanzhiMao/BFCL-Result)
- [Discord Community](https://discord.gg/grXXvj9Whz)

---

## Citation

```bibtex
@inproceedings{patil2025bfcl,
  title={The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models},
  author={Patil, Shishir G. and Mao, Huanzhi and Cheng-Jie Ji, Charlie and Yan, Fanjia and Suresh, Vishnu and Stoica, Ion and E. Gonzalez, Joseph},
  booktitle={Forty-second International Conference on Machine Learning},
  year={2025},
}
```

---

## See Also

- [Tool Use](./tool-use.md)
- [LLMs](./llms.md)
- [Agentic Coding](./amp.md)
- [AI Testing & Validation](./ai-testing.md)

---

[Back to Concepts Hub](./README.md)
