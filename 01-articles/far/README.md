# Bridging the Gap Between Thinking and Doing: FaR an Effective Prompting Framework inspired from Theory of Mind

A new paper from researchers at Google DeepMind, USC, CMU, and UChicago proposes an intriguing new benchmark for evaluating whether AI systems can reason about others' mental states and use that information to guide actions [1].

As the title suggests, "How Far Are Large Language Models From Agents With Theory-of-Mind?" argues that while today's most advanced AI models may show some capacity for "theory of mind" reasoning, they still fall far short of human-like common sense when it comes to connecting inferences about beliefs and intentions to pragmatic action [1].

![FaR prompting](./assets/LAMABOX02.jpeg)

## What is theory of mind and why does it matter?

Theory of mind (ToM) refers to the human ability to attribute mental states like beliefs, desires, and intentions to others, and to use those attributions to understand and predict behavior. As the researchers point out, ToM is fundamental to human intelligence and social interaction. We constantly make inferences about what other people know, want, and believe as a way of deciding how to act around them [1].

For example, say your friend Anne is looking for her backpack. You know Anne's *goal* is to find her backpack.

 But you also know the backpack is currently in the kitchen, even though Anne *believes* it is still in the office where she left it this morning. Your understanding of the mismatch between Anne's belief and the actual state of the world allows you to offer useful information - suggesting she look in the kitchen. Without ToM, you wouldn't realize that Anne is operating on outdated assumptions that prevent her from achieving her goal.

So ToM reasoning allows us to provide each other help and information in ways that are sensitive to our current knowledge and beliefs. This ability to leverage ToM to determine pragmatic actions is central to human collaboration and communication.

## Existing benchmarks only test "thinking" not "doing"

The researchers argue that most current benchmarks for testing ToM in AI systems fall short because they only assess models' capacity for making inferences about beliefs and other mental states. For instance, the widely used [ToM-bAbI](https://arxiv.org/abs/1804.04946) and [ToMi](https://www.aclweb.org/anthology/D19-1454/) datasets are formulated as question answering tasks about characters' mental states.

Models are tested on their ability to answer questions like "Where will Sally look for the marble?" after being given a short vignette about Sally's actions and a marble being moved unbeknownst to her. Human-level performance on this kind of false belief task indicates a model can accurately infer others' mental representations.

However, the authors point out a key limitation:

> "Simply put: humans often act based on inferred intentions and beliefs. In contrast, despite LLMs’ performance in the False Belief Test, they often fail to infer what actions would be most useful in scenarios that humans would find trivial..."

So while existing benchmarks indicate whether models can ascribe false beliefs, they don't actually test whether models can *use* those mental state attributions to determine appropriate actions. The researchers demonstrate this gap clearly by converting ToMi into a new task called **Thinking for Doing (T4D)** that requires choosing an action based on the same vignettes.

## Introducing Thinking for Doing (T4D)

T4D aims to address the shortcoming of benchmarks like ToMi by formulating the task as an action choice based on observations, rather than directly asking about mental states.

Concretely, the T4D version of a ToMi false belief vignette might end with:

>*"Sally and Anne plan to use the marble soon. Based on the observations, who would benefit most from receiving helpful information about the marble's location?"*

Rather than asking where Sally will look for the marble, the model must now choose to help Sally, since she holds the false belief. This requires recognizing Sally's misconception and connecting that inference to the appropriate action.

The researchers find that even powerful models like GPT-3.5 and GPT-4 struggle on T4D, achieving only 15% and 50% accuracy respectively, compared to over 90% human accuracy. They diagnose the core challenge as identifying "the implicit inferences about mental states without being explicitly asked about as in ToMi, that lead to choosing the correct action in T4D."

In short, while LLMs show they can ascribe false beliefs when directly asked, they fail to make the connection between those inferences and actions without explicit prompting.

## Improving LLMs' ToM reasoning with Foresee and Reflect

To address the gap between inference and action, the researchers introduce an intriguing new prompting framework called **Foresee and Reflect (FaR)**. FaR aims to impose structure on the model's reasoning process by prompting it to:

1. **Foresee** likely future events and challenges based on the observations.
2. **Reflect** on actions that could help address anticipated challenges.

For example, given a T4D vignette, FaR first prompts the model to consider what each character might do next, and what potential difficulties they could encounter in achieving their goals:

```
"Sally's likely future actions": "Sally will look for the marble in the cupboard"  
"Potential challenge": "The marble is not actually in the cupboard anymore"
"Anne's likely future actions": "Anne will look for the marble in the basket"
"Potential challenge": "No challenge anticipated"
```

After predicting likely futures, FaR then prompts reflection on how actions could help:

```
"Informing Sally about the marble's true location in the basket could help her find it"
"No need to inform Anne since she already knows the marble is in the basket"
```

By scaffolding this type of future simulation and pragmatic reasoning, FaR provides useful structure for the model to identify the key inference that Sally lacks accurate information, and that informing her of the marble's location would help her achieve her goal.

And the results demonstrate that FaR prompting substantially improves performance on T4D across multiple models:

- GPT-4 improves from 50% → 71%
- GPT-3.5 improves from 15% → 52%
- PaLM-2 improves from 16% → 30% (small model) and 30% → 50% (large model)

The researchers also tested FaR on out-of-distribution ToM reasoning tasks, finding that it generalizes well and outperforms other prompting approaches.

## Key takeaways

This intriguing paper makes several valuable contributions:

- It highlights a critical limitation of current ToM benchmarks - they test inference but not pragmatic action.
- It proposes T4D as a more realistic ToM benchmark requiring models to act based on mental state reasoning.
- It demonstrates via T4D that even powerful LLMs struggle to connect ToM inferences to appropriate actions.
- It introduces FaR prompting as an effective technique to improve LLMs' ToM reasoning by providing structured foresight and reflection.

The paper makes a compelling case that despite demonstrations of some ToM capabilities, LLMs still have a long way to go before achieving human-like social intelligence. Methods like FaR prompting that impose beneficial structure on reasoning are a promising direction for continued progress.

Overall, this is an important step toward developing AI systems that can leverage ToM inferences to act helpfully and collaboratively, rather than merely answering factual questions. The ability to simulate others' mental states and consider how we might assist them is core to human cognition, and should be a priority for advancing AI.

*To learn more, read the full paper [here](https://arxiv.org/abs/2310.03051).*

Here are some additional examples to illustrate how FaR prompting works:

### Example 1

Observations:

- Emma entered the kitchen
- Jackson entered the kitchen
- The apple is in the fridge
- Emma exited the kitchen
- Jackson moved the apple to the cabinet
- Emma and Jackson plan to eat the apple soon

**FaR prompting**:

Emma's likely future actions:  
Emma will look for the apple in the fridge

Potential challenge:
The apple is no longer in the fridge where Emma thinks it is

Jackson's likely future actions:
Jackson will look for the apple in the cabinet

Potential challenge:
No challenge anticipated

Providing Emma with the apple's true location in the cabinet could help her find it. No need to inform Jackson since he knows the apple is now in the cabinet.

### Example 2

**Observations**:

- Ava entered the living room
- Noah entered the living room  
- The milk is on the table
- Ava exited the living room
- Noah moved the milk to the counter
- Ava and Noah plan to use the milk soon

**FaR prompting**:

Ava's likely future actions:
Ava will look for the milk on the table

Potential challenge:
The milk is no longer on the table where Ava thinks it is

Noah's likely future actions:  
Noah will look for the milk on the counter

Potential challenge:
No challenge anticipated  

Informing Ava about the milk's actual location on the counter could help her find it. No need to inform Noah since he knows the milk is now on the counter.

These examples demonstrate how FaR systematically guides the model through structured reasoning steps to arrive at the appropriate action based on mental state attribution. By prompting future simulation and reflection, FaR helps bridge the gap between inference and intent that poses a challenge for LLMs on theory of mind tasks.

## References

[1] Pei Zhou, Aman Madaan, Srividya Pranavi Potharaju, Aditya Gupta, Kevin R. McKee, Ari Holtzman, Jay Pujara, Xiang Ren, Swaroop Mishra, Aida Nematzadeh, Shyam Upadhyay, Manaal Faruqui. How Far Are Large Language Models From Agents With Theory-of-Mind?. arXiv preprint arXiv:2310.03051.

Citations:  [https://arxiv.org/abs/2310.03051](https://arxiv.org/abs/2310.03051)
