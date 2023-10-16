# CodeChain: Improving Code Generation through Modular Self-Revision

Code generation using large language models (LLMs) has shown promising results recently. However, when evaluated on complex programming tasks, current LLMs still fall short compared to human developers. A key reason is LLMs' tendency to generate monolithic code blocks, lacking the modularization and abstraction that experienced programmers utilize.

To address this, the paper "CodeChain: Towards Modular Code Generation through Chain of Self-Revisions with Representative Sub-Modules" introduces a novel framework called CodeChain that elicits modular code generation through iterative self-revision.

![CodeChain](./assets/LAMAC03.png)

## The Limitations of Current LLMs in Code Generation

LLMs like Codex, AlphaCode, and CodeParrot can generate syntactically correct programs and solve simple coding tasks. However, their performance significantly drops on more complex problems from benchmarks like APPS and CodeContests.

For instance, Codex only achieves 0.92% pass@1 on APPS. The key limitations are:

- **Monolithic generation:** LLMs tend to generate solutions as one big code block, without decomposing them into logical sub-tasks and sub-modules.

- **Independent sampling:** LLMs generate many candidate solutions independently, hoping one passes all test cases. But each is unlikely to be fully correct.

In contrast, experienced programmers write modular code, decomposing problems into sub-tasks and reusing previously developed modules.

## Overview of CodeChain

To address the above limitations, CodeChain introduces two key ideas:

1. **Modular code generation:** Use "chain-of-thought" prompting to elicit modular solutions with outlined sub-modules.

2. **Self-revision with representative sub-modules:** Iteratively select representative sub-modules from all samples and use them to guide self-revision.

Here is a high-level overview of how CodeChain works:

1. Instruct the LLM to generate modularized code using chain-of-thought prompting.

2. Extract sub-modules from all generated samples and cluster them. Select representative sub-modules from each cluster.

3. Augment the original prompt with these sub-modules and instruct the LLM to revise its code.

4. Iterate self-revision rounds, each time using updated representative sub-modules.

This approach allows the LLM to collectively learn from all samples and reuse verified sub-modules, similar to how human programmers iterate on solutions.

## Eliciting Modular Code Generation

To elicit modular code, CodeChain uses **chain-of-thought (CoT) prompting**. The LLM is instructed to:

1. Outline required sub-modules as function headers and docstrings.

2. Implement each sub-module fully.

3. Integrate sub-modules into the final solution.

For example:

```
# Step 1: Outline sub-modules  

def count_words(text):
  """Count words in text"""

def filter_words(words):
  """Filter word list"""
  
# Step 2: Implement sub-modules

def count_words(text):
  return len(text.split())
  
def filter_words(words):
  filtered = []
  for w in words:
    if w.isalpha():
      filtered.append(w)
  return filtered
  
# Step 3: Final solution

text = input()
words = count_words(text)
filtered = filter_words(words)
print(len(filtered))
```

This structured prompting encourages the LLM to decompose problems and generate modular solutions.

## Self-Revision with Representative Sub-modules

While CoT prompting elicits modularity, the generated solutions can still be incorrect. To improve quality, CodeChain applies **self-revision** using the most representative sub-modules.

The key steps are:

1. Extract sub-modules from all samples and cluster them.

2. Select the centroid sub-module from each cluster as the representative.

3. Augment the original prompt with these sub-modules.

4. Instruct the LLM to regenerate code, reusing/adapting sub-modules.

5. Iterate self-revision rounds with updated representative sub-modules.

This allows the LLM to collectively learn from all samples, similar to how human programmers reuse verified modules. The most representative sub-modules provide useful hints to guide each revision round.

## Results

CodeChain achieves significant gains over baselines on APPS and CodeContests:

- On APPS, CodeChain + GPT-3.5 reaches **30.24% pass@1**, improving over Codex by 32x.

- On CodeContests, CodeChain + GPT-3.5 achieves **13.75% pass@1**, surpassing baselines by 10-13x.

Ablation studies show:

- CoT prompting alone reduces performance, but boosts gains from self-revision.

- Representative sub-modules are key for successful self-revision.

- Performance improves over multiple revision rounds, plateauing at round 4-5.

Overall, CodeChain sets a new state-of-the-art for complex code generation by eliciting and leveraging modularity through self-revision.

## Conclusion

CodeChain demonstrates a novel approach to improve code generation through:

1. Eliciting modularity with chain-of-thought prompting.

2. Guiding self-revision using representative sub-modules.

The techniques provide useful insights on how to unlock stronger code generation capabilities in LLMs.

There remain challenges in scaling up and generalizing the techniques. But CodeChain represents an important step towards enabling LLMs to generate complex, maintainable code like human programmers.

Check out the full paper for more details:

[CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules](https://arxiv.org/abs/2310.08992)

Hung Le, Hailin Chen, Amrita Saha, Akash Gokul, Doyen Sahoo, Shafiq Joty
