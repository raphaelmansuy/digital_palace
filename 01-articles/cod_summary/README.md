# Harnessing the Power of AI to Rapidly Extract Key Insights

Reading and digesting long articles, research papers, or books can be time-consuming.

 Recently, I came across an intriguing new technique called Chain of Density (CoD) that leverages large language models like GPT-3 to produce dense, informative summaries.

  In this post, I'll explain how CoD works and share code for generating summaries with this method.

## The Challenge of Balancing Detail and Readability

Creating a summary that fully captures the key details of a source document, while remaining easy to read and digest, is a difficult balancing act. Summaries that are too sparse miss important information. But pack too much detail into a small space, and the summary becomes dense and confusing.

The ideal summary hits a sweet spot - dense enough to be informative, yet light enough to read smoothly. This balance is especially critical when dealing with long articles or papers. You want to boil down the key details into a tight summary you can review rapidly.

![The reading Lama](./assets/illustration.png)

## Introducing Chain of Density (CoD)

Recently, researchers at Columbia University, MIT, and Salesforce published a paper describing Chain of Density (CoD), a new technique for generating optimally dense GPT-based summaries. CoD takes advantage of GPT-3's few-shot prompting capabilities to iteratively densify an initial sparse summary.

**Here's an overview of how CoD works**:

1. GPT-4 generates an initial verbose, entity-sparse summary. This summary intentionally includes minimal specific details - just enough context to make sense.

2. GPT-4 then identifies 1-3 "Missing Entities" from the source document that are relevant, specific, novel (not already covered), faithful to the original content, and concise (under 5 words).

3. Next, GPT-4 rewrites the previous summary to fuse in the Missing Entities within the same word limit. This forces abstraction, fusion, and compression to make room for the additional details.

4. Steps 2-3 are repeated up to 5 times, resulting in increasingly dense summaries with more entities covered per token.

The end result is a highly informative yet easy to digest summary, optimized for density through iterative refinement.

## Walkthrough of the CoD Process

To see CoD in action, let's walk through a sample document summarization:

**Document:**

*Jenson Button's McLaren collided with Pastor Maldonado's Lotus during the Chinese Grand Prix while competing for 13th place. The crash forced Maldonado's retirement and resulted in a penalty for Button, who was demoted to 14th place. The incident unfolded in front of Fernando Alonso, who managed to avoid the collision and moved up two places.*

**CoD Step 1:**

*This article discusses an incident that occurred during the Chinese Grand Prix involving two racing drivers, Jenson Button and Pastor Maldonado. The two were competing for the 13th place when Button collided with Maldonado's vehicle, causing damage to both cars. The incident resulted in a penalty for Button, who was demoted to 14th place. Maldonado, on the other hand, had to retire from the race due to the damage his car sustained.*

**Missing Entities:** Jenson Button; Pastor Maldonado; Chinese Grand Prix

**CoD Step 2:**

*During the Chinese Grand Prix, Jenson Button, driving for McLaren, collided with Pastor Maldonado's Lotus, while they were vying for 13th place. The crash caused Maldonado to retire and Button to receive a penalty, dropping him to 14th. The incident unfolded in front of Fernando Alonso, who managed to avoid the collision and move up two places.*

You can see how Step 2 fuses in the missing entities like the drivers' teams and the race name, while tightening up the wording to avoid increasing the length. Each subsequent step would repeat this process of identifying missing details and densifying the summary.

## Implementing CoD Summarization in Python

I've developed a Python module that implements the CoD prompting approach for generating dense GPT-3 summaries. It includes:

- `gen_prompt()`: Generates the iterative CoD prompt with verbosity guidelines and formatting.

- `cod_summarize()`: Calls the OpenAI API to generate summaries for a given number of densification steps.

- `cli`: Provides a CLI for summarizing text files using CoD.

The key steps are:

1. Construct a prompt explaining the CoD process and constraints.

2. Pass the document and previous summary to GPT-3.

3. Parse GPT-3's response for the missing entities and new summary.

4. Repeat for the desired number of densification iterations.

Here is a sample run generating a 5-step CoD summary:

```
$ python cod.py summarize paper.txt --steps 5
Generating summary... number 1  
Generating summary... number 2
Generating summary... number 3  
Generating summary... number 4
Generating summary... number 5

{
  "summary": "On lap 49 of the incident-packed Chinese Grand Prix, Jenson Button's McLaren hit Pastor Maldonado's Lotus, causing damage and Maldonado's retirement. Button received a five-second penalty and two superlicense points, falling to 14th. Fernando Alonso, who witnessed the crash, advanced two places, while Button was lapped by Nico Rosberg and Alonso by Ferrari's Sebastian Vettel and Kimi Raikkonen."
}
```

## The CoD Python Module

```python
""" A Python module for generating summaries of documents using the CoD prompt. """
import openai


VERBOSITY_GUIDELINES = """
The first summary should be long (4-5 sentences, ~80 words)
yet highly non-specific, containing little information beyond
the entities marked as missing.
Use overly verbose language and fillers (e.g., "this article discusses")
to reach ~80 words.
"""

FUSION_INSTRUCTIONS = """
- Make every word count: re-write the previous summary to improve flow
 and make space for additional entities.
- Make space with fusion, compression, and removal of uninformative phrases
like "the article discusses".
"""

ENTITY_CONSTRAINTS = """
A Missing Entity is:
- Relevant: to the main story
- Specific: descriptive yet concise (5 words or fewer)
- Novel: not in the previous summary
- Faithful: present in the Article
- Anywhere: located anywhere in the Article
"""

RESULT_FORMAT = """
  The result format is a JSON object with the following fields:
  {
    previous_summary: "The previous summary text",
    missing_entities: ["entity1", "entity2", "entity3"]
   "summary": "The summary text",
  }
"""


def gen_prompt(document: str) -> str:
    """
    Generate the CoD prompt for a document.
    """
    prompt = (
        f"Article: {{{document}}}\n"
        "You will generate increasingly concise, entity-dense summaries of "
        "the above Article.\n"
        f"{VERBOSITY_GUIDELINES}\n"
        f"{FUSION_INSTRUCTIONS}\n"
        'Step 1. Identify 1-3 informative Entities (";" delimited) from the '
        "Article which are missing from the previously generated summary.\n"
        "Step 2. Write a new, denser summary of identical length which covers "
        "every entity and detail from the previous summary plus the Missing "
        "Entities.\n"
        f"{VERBOSITY_GUIDELINES}\n"
        f"{RESULT_FORMAT}\n"

    )
    return prompt


def cod_summarize(document: str, steps: int, debug: bool = False) -> list:
    """
    Generate a summary of a document using the CoD prompt.
    :param document: The document to summarize.
    :type document: str
    :param steps: The number of steps to perform for summarization.
    :type steps: int
    :return: A list of summaries generated using the CoD prompt.
    :rtype: list of str
    """

    # Check if the inputs are valid
    if not isinstance(document, str) or not document:
        raise ValueError("Document must be a non-empty string")
    if not isinstance(steps, int) or steps < 1 or steps > 5:
        raise ValueError("Steps must be an integer between 1 and 5")

    # Initialize an empty list to store the summaries
    summaries = []

    # Loop through the number of steps
    for i in range(steps):
        # Construct the CoD prompt with the document and the previous summary

        prompt = gen_prompt(document)

        if i > 0:
            # Add the previous summary to the prompt
            prev_summary = summaries[-1]
            prompt += prev_summary

        # Call the OpenAI API with the prompt and other parameters
        try:
            print(f"Generating summary... number {i+1}")
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an AI assistant expert summary.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=1024,
            )
            summary = response.choices[0].message.content

            if debug:
                print(summary)

            # Append the summary to the list
            summaries.append(summary)
        except openai.error.OpenAIError as error:
            # Handle any errors from the API
            print(f"OpenAI error: {error}")
            break

    # Return the list of summaries
  return summaries
```

The [full code](https://github.com/user/cod) is available on GitHub. I encourage you to try it out on research papers, articles, or other documents you want to summarize!

## Optimizing Summaries for Your Needs

CoD provides a powerful technique for creating optimally dense summaries tuned to your specific needs. Here are some ways you can customize the process:

- Vary the number of densification steps based on your desired level of detail vs. concision.

- Focus on extracting entities relevant to your use case, like key figures or technical terms.

- Adjust the summary length parameter to control level of compression.

- Rerank and select the best step based on quantitative metrics like entity density.

- Distill CoD into your own summarization model via reinforcement learning.

I'm excited to continue experimenting with CoD and other prompting techniques to make AI work harder for me. What other creative ways could you apply CoD summarization? Let me know your thoughts and ideas in the comments!

## References

Paper : https://arxiv.org/abs/2309.04269

Github code : https://github.com/raphaelmansuy/thoughtdense
