from litellm import completion

messages = [{"role": "user", "content": "What is the capital of France?"}]

response = completion(model="gpt-3.5-turbo", messages=messages)

fisrt_choice = response["choices"][0]


print(response)
print(fisrt_choice.message.content)
