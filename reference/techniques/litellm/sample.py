import os
from litellm import completion

## set ENV variables
os.environ["OPENAI_API_KEY"] = "sk-litellm-7_NPZhMGxY2GoHC59LgbDw" # [OPTIONAL] replace with your openai key
os.environ["COHERE_API_KEY"] = "sk-litellm-7_NPZhMGxY2GoHC59LgbDw" # [OPTIONAL] replace with your cohere key
os.environ["ANTHROPIC_API_KEY"] = "sk-litellm-7_NPZhMGxY2GoHC59LgbDw" # [OPTIONAL] replace with your cohere key


messages = [{ "content": "Hello, how are you?","role": "user"}]

# openai call
response = completion(model="claude-2", messages=messages)

print(response)

# cohere call
response = completion("command-nightly", messages)

print(response)



