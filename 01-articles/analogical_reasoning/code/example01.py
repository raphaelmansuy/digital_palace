from litellm import completion


def generate_analog_prompt(problem: str) -> str:
    """
    Generates the prompt for the completion function.
    """
    prompt = f"""
    # Problem: "{problem}" ?

    # Relevant problems:

    Recall 3 distinct relevant math problems. For each problem:
    
    - Describe the problem after "Q: "
    - Provide the reasoning and solution after "A: "

    Q1:
    A1:

    Q2:
    A2:

    Q3:
    A3:

    # Explain your reasoning:
      
      - First, I will ...
      - Next, I need to ...
      - Finally, I will ...

    # Solve the initial problem:
    
    To find a solution to the problem: "{problem}", we need to...
    
      
    """
    return prompt


def generate_message(prompt):
    """
    Generates the message for the completion function.
    """
    message = {"role": "user", "content": prompt}
    return message


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


def main():
    """
    Main function to generate the prompt, call the completion function,
    and process the response.
    """

    problem = """
    “A man spends one-eighth of his money on rent,
    and four times that amount on food and clothing. 
    He has $ 9,000.00 left. How much did he have at the beginning? """

    prompt = generate_analog_prompt(problem)
    print(prompt)
    message = generate_message(prompt)
    try:
        response = completion(model="gpt-3.5-turbo",
                              messages=[message], stream=True, temperature=0.9)
        process_response(response)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
