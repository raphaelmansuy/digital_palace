import argparse
from litellm import completion
import json
from tqdm import tqdm


model = "gpt-3.5-turbo"


def get_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--sampling_type", type=str, default="cot")
    parser.add_argument("--resample_path", type=str,
                        default="./results/cot_sample_subques_resample.jsonl")
    parser.add_argument("--result_path", type=str,
                        default="./results/cot_sample_subques_resample_selection.jsonl")
    parser.add_argument("--prompt_path", type=str,
                        default="./prompts/cot_selection.txt")
    parser.add_argument("--hetero", type=bool, default=False)
    return parser.parse_args()

# read prompt file


def read_prompt(prompt_path):
    '''
    Read prompt file
    '''
    with open(prompt_path, "r", encoding="utf-8") as file:
        prompt = file.read()
    return prompt

# read data from the file


def get_dataset(path_name):
    """
    Read data from the file
    """
    with open(path_name, 'r', encoding="utf-8") as dataset:
        data_list = list(dataset)
        for line in data_list:
            problem = json.loads(line)
            yield problem

# save results to a file


def store_result(out, problem, output):
    """
    Save results to a file
    """
    problem['selection'] = output
    out.write(json.dumps(problem, ensure_ascii=False) + '\n')


# Selection function for CoT
def selection_cot(samp_path, res_path, prompt_path, hetero):
    """
    Selection function for CoT (Chain of Thought)
    """
    base_prompt = read_prompt(prompt_path)
    with open(res_path, "a", encoding='utf-8') as out:
        for sample in tqdm(get_dataset(samp_path)):
            question = sample["question"]
            answerA = sample["prediction"]
            if hetero:
                answerB = sample["het_resample"]
            else:
                answerB = sample["resample"].split("Final Answer: ")[-1]

            instruction = "You are an expert math teacher. You are provided with a question and two answers. Lets check the 'Answer choices' step by step, and then decide which answer is correct '(A)' or '(B)'"
            prompt = f"{base_prompt}\n{instruction}\nQuestion: {question}\nAnswer choices:\n(A) {answerA}\n(B) {answerB}\n"

            # Call Littellm model
            response = model.generate(prompt, max_tokens=2, temperature=0)

            output = response.text
            if "A" in output:
                final = answerA
            elif "B" in output:
                final = answerB
            else:
                final = output

            store_result(out, sample, final)


def selection_subques(SAMP_PATH, RES_PATH, PROMPT_PATH, HETERO):

    BASE_PROMPT = read_prompt(PROMPT_PATH)

    with open(RES_PATH, "a", encoding="utf-8") as out:
        for sample in tqdm(get_dataset(SAMP_PATH)):
            question = sample["question"]
            answerA = " ".join([qa[1].split("The answer is ")[
                               0] for qa in sample["prediction"][:-1]]) + sample["prediction"][-1][1]
            if HETERO:
                answerB = sample["het_resample"]
            else:
                answerB = " ".join([qa[1].split("The answer is ")[
                                   0] for qa in sample["resample"][:-1]]) + sample["resample"][-1][1]
            instruction = "You are an expert math teacher. You are provided with a question and two answers. Lets check the 'Answer choices' step by step, and then decide which answer is correct '(A)' or '(B)'"
            prompt = f"{BASE_PROMPT}\n{instruction}\nQuestion: {question}\nAnswer choices:\n(A) {answerA}\n(B) {answerB}\nAnswer: ("

            not_responded_yet = True
            while not_responded_yet:
                try:
                    response = completion(
                        model="gpt-3.5-turbo-instruct",
                        message=[{"content": prompt, "role": "user"}],
                        max_tokens=2,
                        temperature=0
                    )
                    not_responded_yet = False
                except Exception as error:
                    print(error)
                    print("retrying\n")

            output = response.choices[0]["text"]
            if "A" in output:
                final = sample["prediction"]
            elif "B" in output:
                final = sample["resample"]
            else:
                print("Neither A nor B", output)
                final = output
            store_result(out, sample, final)


def main(args):
    """ 
    Main function to call inference function for sampling
    """
    # call inference function for sampling
    openai.api_key = args.openai_key
    if args.sampling_type == "cot":
        selection_cot(args.resample_path, args.result_path,
                      args.prompt_path, args.hetero)

    elif args.sampling_type == "subques":
        selection_subques(args.resample_path, args.result_path,
                          args.prompt_path, args.hetero)
    else:
        print("Choose between 'cot' or 'subques'")


if __name__ == "__main__":
    args = get_args()
    assert args.resample_path != "", "Please provide the resampled output path for GSM8K"
    if args.prompt_path == "":
        print("Sampling in Zero Shot Setting!")

    main(args)
