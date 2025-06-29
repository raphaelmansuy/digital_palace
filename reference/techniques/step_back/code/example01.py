from litellm import completion


def generate_step_back_prompt(problem):
    """Generates a prompt to take a step back from the original problem."""

    prompt = f"""
# Original Problem:
"{problem}"

# Step Back: 
What are the key steps and concepts needed to solve this math word problem? 

# Explain the key steps:

# Solve the original problem:
To solve the original problem, I will...
"""
    return prompt


def process_response(response):
    """
    Processes the response from the completion function.
    """
    for chunk in response:
        try:
            if "choices" in chunk and chunk["choices"]:
                choice = chunk["choices"][0]
                if choice["finish_reason"] == "stop":
                    print("\n")
                    break
                if "delta" in choice and "content" in choice["delta"]:
                    content = choice["delta"]["content"]
                    if content:
                        end = "\n" if content.endswith("\n") else ""
                        print(content, end=end)
            else:
                print("")
        except Exception as e:
            print(f"An error occurred: {e}")


def generate_message(prompt):
    """
    Generates the message for the completion function.
    """
    message = {"role": "user", "content": prompt}
    return message


def main():
    """
    Main function to generate the prompt, call the completion function,
    and process the response.
    """

    problem = """
    “A man spends one-eighth of his money on rent,
    and four times that amount on food and clothing. 
    He has $ 9,000.00 left. How much did he have at the beginning? """

    prompt = generate_step_back_prompt(problem)
    print(prompt)
    message = generate_message(prompt)
    try:
        response = completion(model="gpt-3.5-turbo",
                              messages=[message], stream=True, temperature=0.5)
        process_response(response)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
