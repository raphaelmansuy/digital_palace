Here is a step-by-step tutorial on how to use the liteLLM API in Python:

# Introduction to liteLLM

liteLLM is an API that provides a unified interface to call various large language models (LLMs) like GPT-3, Codex, and others. It handles authentication, prompting, decoding of responses and retries in case of failures automatically.

# Installation

Install liteLLM with pip:

```
pip install litellm
```

# Setup API Keys

You need to set up API keys for the LLM providers you want to access. Here is an example with OpenAI and Cohere keys:

```python
import os

os.environ["OPENAI_API_KEY"] = "sk-..."
os.environ["COHERE_API_KEY"] = "abcd1234..."
```

# Creating a Completion

To create a completion, you need to pass a list of messages and specify the model:

```python
from litellm import completion

messages = [{"role": "user", "content": "What is the capital of France?"}]

response = completion(model="gpt-3.5-turbo", messages=messages)

fisrt_choice = response["choices"][0]


print(response)
print(fisrt_choice.message.content)

```

This will call the GPT-3.5 Turbo model and print the response.

You can also call the Cohere models by changing the model name:

```python
response = completion("command-xlarge-nightly", messages)
```

# Handling Failures

The completion call can sometimes fail due to network or throttling issues. liteLLM provides a helper method `completion_with_retries` that will retry in case of failures:

```python
from litellm import completion_with_retries

response = completion_with_retries(model="gpt-3.5-turbo", messages=messages)
```

By default, it will retry up to 10 times with exponential backoff before failing.

# Calling Multiple Models

You can also fan out calls to multiple models easily:

```python
from litellm import completions

messages = [...]

models = ["gpt-3.5-turbo", "command-xlarge-nightly"]

responses = completions(messages=messages, models=models)

for response in responses:
   print(response)
```

This will call both models and return a list of responses that you can process.

# Conclusion

That covers the basics of using the liteLLM API! With just a few lines of code, you can access the latest LLMs and build powerful applications.

https://litellm.vercel.app/docs/tutorials/first_playground


