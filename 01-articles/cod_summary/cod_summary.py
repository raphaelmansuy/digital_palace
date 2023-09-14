""" A Python module for generating summaries of documents using the CoD prompt. """
import sys
import json
import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

# openai.organization = "skynet"


def cod_summarize(document, steps):
    """
    Generate a summary of a document using the CoD prompt.
    :param document: The document to summarize.
    :type document: str
    :param steps: The number of steps to perform for summarization.
    :type steps: int
    :return: A list of summaries generated using the CoD prompt.
    :rtype: list
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
        prompt = f"Article: {{{document}}}\n"
        prompt += "You will generate increasingly concise, entity-dense summaries of the above Article. Repeat the following 2 steps 5 times.\n"
        prompt += "Step 1. Identify 1-3 informative Entities (\";\" delimited) from the Article which are missing from the previously generated summary.\n"
        prompt += "Step 2. Write a new, denser summary of identical length which covers every entity and detail from the previous summary plus the Missing Entities.\n"
        prompt += "A Missing Entity is:\n"
        prompt += "- Relevant: to the main story.\n"
        prompt += "- Specific: descriptive yet concise (5 words or fewer).\n"
        prompt += "- Novel: not in the previous summary.\n"
        prompt += "- Faithful: present in the Article.\n"
        prompt += "- Anywhere: located anywhere in the Article.\n"

        if i > 0:
            # Add the previous summary to the prompt
            prev_summary = summaries[-1]["Denser_Summary"]
            prompt += f"Previous Summary: {{{prev_summary}}}\n\n"

        # Call the OpenAI API with the prompt and other parameters
        try:
            
            print("Generating summary...")

            response = openai.ChatCompletion.create(
                engine="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.5,
            )
            
            print(response)

            # Parse the response and extract the summary
            result = response.choices[0].text.strip()
            summary = json.loads(result)[i]

            # Append the summary to the list
            summaries.append(summary)
        except openai.error.OpenAIError as error:
            # Handle any errors from the API
            print(f"OpenAI error: {error}")
            break

    # Return the list of summaries
    return summaries


def main():
    """
    The main function of the module.
    """

    # Check if a file is provided as input
    if len(sys.argv) < 2:
        print("Usage: python main.py <file>")
        return

    # Read the contents of the file
    file_path = sys.argv[1]
    with open(file_path, "r", encoding="utf-8") as file:
        document = file.read()

    # Call the cod_summarize function
    try:
        summaries = cod_summarize(document, 5)
        print(summaries)
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
