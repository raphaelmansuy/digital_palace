import os
import argparse
import openai
import json
from tqdm import tqdm as tqdm

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sampling_type", type=str, default="subques") # choose between cot or subques
    parser.add_argument("--data_path", type=str, default="./data/test_gsm8k_socratic.jsonl")
    parser.add_argument("--result_path", type=str, default="./results/subques_sample_instruct_testrun.jsonl")
    parser.add_argument("--prompt_path", type=str, default="./prompts/subques_sample.txt")
    parser.add_argument("--openai_key", type=str, default="")

    return parser.parse_args()

def read_prompt(PROMPT_PATH):
    with open(PROMPT_PATH, "r") as f:
        prompt = f.read()
    return prompt

# read data from the file
def get_dataset(PATH):
    with open(PATH, 'r') as dataset:
        data_list = list(dataset)
        for line in data_list:
            problem = json.loads(line)
            yield problem

# save results to a file
def store_result(out, problem, output):
    problem['prediction'] = output
    out.write(json.dumps(problem, ensure_ascii=False) + '\n')

def inference_cot(DATA_PATH, RES_PATH, PROMPT_PATH):

    BASE_PROMPT = read_prompt(PROMPT_PATH)
    
    with open(RES_PATH, "a") as out:
        for sample in tqdm(get_dataset(DATA_PATH)):
            question = sample["question"]
            # input_sample = [{"role": "user", "content": question}]
            prompt = f"{BASE_PROMPT}\nQuestion: {question}\nAnswer: "

            not_responded_yet = True
            while not_responded_yet:
                try:
                    response = openai.Completion.create(
                                model="gpt-3.5-turbo-instruct",
                                prompt=prompt,
                                max_tokens=256,
                                temperature=0
                            )
                    not_responded_yet = False
                except:
                    print("retrying\n")

            output = response.choices[0]["text"]
            store_result(out, sample, output)


def inference_subques(DATA_PATH, RES_PATH, PROMPT_PATH):

    BASE_PROMPT = read_prompt(PROMPT_PATH)

    with open(RES_PATH, "a") as out:
        for sample in tqdm(get_dataset(DATA_PATH)):
            main_ques = sample['question']
            qa_pairs = sample['answer'].split('\n')
            all_output = []
            prompt = f"{BASE_PROMPT}\nProblem: {main_ques}"
            for  qa_pair in qa_pairs[:-1]:
                question, _ = qa_pair.split(' ** ')
                prompt += f"\nQ: {question}\nA:"
            
                not_responded_yet = True
                while not_responded_yet:
                    try:
                        response = openai.Completion.create(
                                model="gpt-3.5-turbo-instruct",
                                prompt=prompt,
                                max_tokens=256,
                                temperature=0
                            )
                        not_responded_yet = False
                    except:
                        print("retrying\n")
                output = response.choices[0]["text"].split("\nQ:")[0]
                prompt += " " + output
                all_output.append([question, output])
            store_result(out, sample, all_output)

def main(args):
    # call inference function for sampling
    openai.api_key = args.openai_key
    if args.sampling_type == "cot":
        inference_cot(args.data_path, args.result_path, args.prompt_path)
    elif args.sampling_type == "subques":
        inference_subques(args.data_path, args.result_path, args.prompt_path)
    else:
        print ("Choose between 'cot' or 'subques'")



if __name__ == "__main__":
    args = get_args()
    assert args.data_path != "", "Please provide the data path for GSM8K"
    assert args.sampling_type !="", "Please choose between 'cot' or 'subques'"
    if args.prompt_path == "":
        print ("Sampling in Zero Shot Setting!")

    main(args)
