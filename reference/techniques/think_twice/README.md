# Improving AI's Theory of Mind Through Perspective-Taking

> How a new prompting technique helps large language models reason about beliefs and mental states


As the CTO of an AI startup studio, I'm always on the lookout for cutting edge research that could improve our products and services. One area that has captured my interest lately is *theory of mind* - the ability to attribute mental states like beliefs, desires, and intentions to oneself and others. While humans perform this type of reasoning effortlessly in social situations, it remains a major challenge for even the most advanced AI systems. 

That's why I was so intrigued when I came across a new paper from Carnegie Mellon University titled ["Think Twice: Perspective-Taking Improves Large Language Models' Theory-of-Mind Capabilities"](https://arxiv.org/abs/2311.10227). The researchers demonstrate a simple yet effective technique for enhancing large language models' (LLMs) ability to reason about others' mental states, achieving substantial performance gains on theory of mind benchmarks. 

In this post, I'll give an overview of the paper, explain why theory of mind and perspective-taking are so important for AI, walk through how the new prompting technique works, discuss the implications, and share my thoughts on how these findings could be applied to improve products and services that rely on natural language processing. There's a lot of ground to cover, so let's dive in!

![Improving AI's Theory of Mind Through Perspective-Taking](./assets/think01.png)

## What is Theory of Mind and Why Does it Matter?

Before getting into the details of this new research, it's helpful to take a step back and understand what theory of mind is and why it's such an important capability. 

### The Complex Cognitive Skill of Mental State Reasoning

Theory of mind refers to the human ability to attribute mental states - beliefs, desires, intentions, knowledge, etc. - to oneself and others. It allows us to explain and predict people's behavior in terms of underlying mental states that may be different from our own. 

For example, theory of mind is what enables us to understand that someone holding an umbrella wants to stay dry, even though we may know the weather forecast calls for sunny skies. Or that a child who thinks broccoli is candy will be disappointed when they taste some. 

This kind of mental state reasoning comes so naturally to humans that we often take it for granted. But it's actually an extremely complex cognitive skill that develops over time in childhood. Some neurodiverse individuals, like those with autism spectrum disorder, can also struggle with theory of mind.

### A Major Obstacle for Artificial Intelligence

Given how effortless theory of mind is for people, you might expect that it would be easy for artificial intelligence as well. But that turns out not to be the case - it remains a major obstacle even for the most capable AI systems.

The challenge lies in the need for common sense reasoning about how the world works along with the ability to model nested beliefs and mental states. For example, to understand that "Sally thinks that Bob wants her cookie", an AI system has to keep track of Sally's belief about Bob's desire. This kind of complex mental state reasoning does not come naturally to neural networks.

As a result, modern AI systems struggle on even simple theory of mind tasks. For instance, they have difficulty with false belief scenarios where someone holds an incorrect belief because they lack knowledge about changes to the world. This limitation presents a major roadblock to developing AI that can perceive and interact with people in natural, human-like ways.

### The Promise of More Social, Empathetic AI 

There is both great need and great potential for AI that can reason about mental states. As AI becomes incorporated into more social domains like healthcare, education, and customer service, theory of mind becomes crucial for natural and effective human-AI interaction.

More capable mental state reasoning could enable AI assistants that understand user intents and goals for more helpful interactions. It could also allow AI systems to model psychological factors like beliefs, desires, and emotions when making recommendations or predictions about human behavior. 

But perhaps the greatest promise is for AI that is more empathetic - able to understand that others may think, feel, and experience the world differently. In a future with pervasive AI, making systems more social and relatable through advances in theory of mind will be essential.

This new research tackles the theory of mind challenge for AI head-on, demonstrating an intriguing prompting technique that yields substantial improvements on benchmark theory of mind tests.

## The Limitations of Current Approaches 

To appreciate the contribution of this new work, it helps to understand the limitations of current approaches to eliciting reasoning capabilities from large language models. The researchers argue existing prompting strategies fall short when it comes to complex mental state reasoning.

### Inside the Black Box of Large Language Models

Large language models (LLMs) like GPT-3 and PaLM have demonstrated impressive natural language processing capabilities. But their inner workings remain largely opaque. To elicit desired behaviors from these black box systems, researchers use prompting - carefully crafting text prompts that provide context and instructions. 

The right prompt can coax an LLM to engage in reasoning for question answering. But designing effective prompts is more art than science, requiring intuition and trial-and-error. When it comes to complex reasoning about mental states, existing prompting strategies seem to hit a wall.

### The Limits of Single-Prompt Reasoning

A common prompting approach is to feed the LLM a story as context, ask a question that requires reasoning about a character's mental state, and have the model generate a short answer. For example:

```
Bob put his sunglasses in the drawer. While Bob was out, Jane moved the sunglasses from the drawer into the cabinet.

Where does Bob think his sunglasses are?

The drawer
```

This *single-inference pass* strategy relies on the LLM reasoning about Bob's false belief in one shot. But on theory of mind benchmarks, LLMs struggle to keep track of agents' perspectives and reliably answer mental state reasoning questions correctly when prompted this way.

### Chain of Thought Hitting a Wall 

An enhancement to single-prompt reasoning is the *chain of thought* prompting strategy, which instructs the LLM to show its work by explaining its reasoning step-by-step:

```
Bob put his sunglasses in the drawer. While Bob was out, Jane moved the sunglasses from the drawer into the cabinet.

Where does Bob think his sunglasses are? 

Thought: Let's think step by step.
Bob put his sunglasses in the drawer. 
While Bob was out, Jane moved the sunglasses from the drawer into the cabinet.
Bob doesn't know Jane moved his sunglasses.
So Bob still thinks his sunglasses are in the drawer.
Answer: The drawer
```

While this technique has improved LLMs' performance on some reasoning tasks, researchers find it has limited applicability to theory of mind. The inference steps shown rarely reflect reasoning about mental states.

So what's missing? Why do single-prompt and chain of thought strategies fall short when it comes to modeling beliefs and perspectives? That brings us to the key insight behind this new research.

## A New Theory-of-Mind Prompting Strategy

The researchers draw inspiration from cognitive science to propose a new prompting strategy that significantly improves LLMs' theory of mind capabilities. Their approach is grounded in a prominent theory of how humans perform mental state reasoning.

### Simulation Theory 

In cognitive science, *simulation theory* aims to explain how people are able to reason about others' mental states. A core tenet is that we use perspective-taking before answering questions about someone's state of mind. 

The theory states that to reason about what someone else believes or wants, we first imagine ourselves in their situation - essentially stepping into their shoes and simulating being them. We imagine having their beliefs and perceptions. Only then do we answer questions about their mental state from their simulated perspective.

This perspective-taking process allows us to understand how the world appears from someone else's point of view so that we can infer their beliefs, predict their behavior, and explain their actions.

### A Two-Step Prompting Approach 

Drawing inspiration from simulation theory, the researchers design a two-step prompting strategy:

1. Perspective-Taking: Ask the LLM to summarize the story from the viewpoint of a character, filtering out events they didn't witness.

2. Question-Answering: Have the LLM answer a theory of mind reasoning question about that character's mental state, given the perspective-filtered context.

This approach prompts the model to simulate the character's limited perspective before reasoning about their mental state. The researchers dub their method SIMTOM, short for SIMulated TOM.

Here's an example of how it works:

```
Perspective-Taking: What does Bob know about what happened?

Bob put his sunglasses in the drawer.

Question-Answering: Where does Bob think his sunglasses are?

Bob put his sunglasses in the drawer.  

The drawer
```

By adding an explicit perspective-taking step, the researchers aim to guide the LLM towards more human-like simulation of someone else's point of view. This primes the model for more accurate mental state reasoning compared to single-prompt and chain of thought approaches.

Next, let's look at how dramatically this new technique improves LLMs' performance on theory of mind benchmarks.


## SIMTOM Yields Dramatic Performance Gains 

To test their new prompting strategy, the researchers evaluated four state-of-the-art LLMs on two established theory of mind benchmark tasks using single-prompt, chain of thought, and SIMTOM prompting. The results are striking.

### Substantial Improvement on Challenging Benchmarks

The benchmarks used are designed to be very difficult for LLMs:

- **ToMI**: Reading comprehension stories and questions about characters with false beliefs.
- **BigToM**: More naturalistic situations that require inferring others' beliefs and actions.

Both benchmarks aim to isolate pure theory of mind reasoning, free of biases or reliance on world knowledge. 

Across all four LLMs tested, SIMTOM prompting dramatically improved accuracy on these theory of mind reasoning challenges compared to standard prompting approaches:

* +**29.5%** absolute accuracy gain for GPT-3.5 over single-prompt on ToMI false belief questions
* +**14.2%** gain over chain of thought on ToMI for GPT-3.5  
* +**23%** gain over single-prompt on BigToM false belief for 7B Llama
* +**20.5%** gain over chain of thought on BigToM for 13B Llama

These substantial gains demonstrate the effectiveness of SIMTOM's perspective-taking approach for eliciting stronger theory of mind capabilities.

### Robust Across Diverse Models

Critically, SIMTOM's benefits hold across the spectrum of models tested:

* Smaller 7B and 13B Llamas 
* Mid-sized GPT-3.5
* Giant 175B GPT-4

This suggests the improvements stem from the human-inspired prompting strategy rather than model scale or architecture. The robustness across models is important as it indicates prompting techniques like SIMTOM could be widely adopted.

### Closing the Gap to Human Baseline

Humans reliably solve over 90% of the ToMI and BigToM questions. With SIMTOM prompting, the LLMs' accuracies approach this human baseline:

* GPT-3.5 reaches 87.75% on ToMI false belief 
* GPT-4 achieves 92% on BigToM false belief

These results reveal prompting strategy is just as important as scale when it comes to improving LLMs' reasoning and generalization. SIMTOM represents a significant step forward in eliciting stronger theory of mind capabilities comparable to human performance.

Building on these impressive results, the researchers perform detailed analysis and ablations to further illuminate why SIMTOM works so well. These additional experiments underscore the importance of perspective-taking for theory of mind in LLMs.

## Why Perspective Matters for Theory of Mind

By taking apart SIMTOM and testing variations, the researchers gain key insights into the mechanisms underlying improved theory of mind capabilities:

### The Separate Perspective-Taking Step is Key

When perspective-taking is interleaved with question answering in a single prompt, performance gains diminish significantly. Keeping it as a distinct first step is critical.

### LLMs Can Learn to Perspective-Take  

With just a few examples to prime perspective-taking, LLMs can filter context even better. This lifts performance further, suggesting perspective-taking is a learnable capability that can be improved.

### Oracle Perspective-Taking Approaches Human Accuracy

When given human-generated filtered context summarizing just what a character knows, LLMs can achieve over 95% accuracy on the benchmarks. This implies perspective-taking is currently the key obstacle, and perfecting it could allow LLMs to perform theory of mind as well as people.

### Takeaway: Perspective is Paramount

Together, these findings strongly indicate that perspective-taking is central to high-quality mental state reasoning in LLMs. They align with the cognitive science inspiration for SIMTOM - that simulating others' limited perspectives is core to human-like theory of mind capabilities.

By directing LLMs to explicitly take perspective through prompting, significant performance gains ensue. This lends credence to simulation theory as a model for achieving more human-like social intelligence in AI systems.

## Implications for Building AI with Theory of Mind

Stepping back, these research findings have exciting implications both for near-term applications and for the longer term development of artificial general intelligence.

### Ready to Integrate into NLP Applications

Unlike methods requiring additional training, SIMTOM is ready to integrate with any existing LLM. The simple prompting strategy improves performance out-of-the-box, no fine-tuning needed.

Product teams can swiftly prototype SIMTOM prompting with their conversational AI to enhance mental state reasoning. Even minor gains in theory of mind capabilities could benefit applications like dialogue agents and personal assistants.

### Unlocks More Social, Empathetic AI

Looking farther ahead, SIMTOM provides a blueprint for coaxing substantially stronger theory of mind from increasingly capable LLMs in the future. 

As models become more adept at simulating human perspectives, we inch closer to AI that can truly relate to people and interact with grace, empathy, and social intelligence. Theory of mind remains one of the grand challenges on the path to more human-like AI.

### Insights to Advance Cognitive Science

On a more philosophical level, this research also demonstrates how AI can contribute back to advancing cognitive science. SIMTOM's success aligns with simulation theory's explanation for how people reason about others' minds.

The fact that guided prompting can elicit perspective-taking and belief reasoning in LLMs gives credence to hypotheses about human cognitive mechanisms. Advances in neuro-symbolic AI may someday further illuminate the origins of social intelligence.

## Time Will Tell

This research represents an exciting step, but there is still a long road ahead to achieve human-like theory of mind in artificial intelligence. As with any single study, follow-up work is needed to further probe the limitations and validate benefits.

But based on these initial results, I believe perspective-taking merits much deeper investigation as a promising direction for improving LLMs' theory of mind capabilities. The team at Carnegie Mellon plans to release their code to allow wider testing of SIMTOM prompting. I'm looking forward to seeing what the community builds from this intriguing starting point.

The more AI can learn to think from diverse human perspectives, simulating our inner mental worlds, the smarter it will become about navigating the social world. While the end goal of artificial general intelligence remains far off, papers like this give me hope that the journey continues step by step - or perhaps I should say prompt by prompt.

To learn more, be sure to [read the full research paper](https://arxiv.org/abs/2311.10227) and let me know your thoughts! I believe these kinds of advances will be key to unlocking the full potential of artificial intelligence to work in harmony with people. The quest for more human-like AI continues.

So in summary, the key points are:

- Theory of mind is essential for human-like reasoning but very difficult for AI
- Existing prompting strategies have fallen short on complex mental state reasoning
- New research shows a perspective-taking approach improves LLMs' theory of mind capabilities 
- SIMTOM prompting yields dramatic performance gains across models and benchmarks
- Analysis reveals the importance of separate perspective-taking to high-quality theory of mind
- Practical implications for improving AI assistants and progress towards AGI

Let me know what you think! I'm keen to discuss how techniques like this could impact the future of artificial intelligence.

## Citations

Wilf, Alex, Sihyun Shawn Lee, Paul Pu Liang, and Louis-Philippe Morency. "Think Twice: Perspective-Taking Improves Large Language Models’ Theory-of-Mind Capabilities." arXiv preprint arXiv:2311.10227 (2023).