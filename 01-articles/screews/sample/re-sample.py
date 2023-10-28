import os
import argparse
import openai
import json
from tqdm import tqdm as tqdm

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--sampling_type", type=str, default="subques") # choose between cot or subques
    parser.add_argument("--sample_path", type=str, default="./results/subques_sample_instruct.jsonl")
    parser.add_argument("--result_path", type=str, default="./results/subques_resample_instruct.jsonl")
    parser.add_argument("--sample_prompt_path", type=str, default="./prompts/subques_sample.txt")
    parser.add_argument("--resample_prompt_path", type=str, default="./prompts/subques_resample.txt")
    parser.add_argument("--openai_key", type=str, default="")

    return parser.parse_args()

#read prompt file
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
    problem['resample'] = output
    out.write(json.dumps(problem, ensure_ascii=False) + '\n')

# save results to a file
def store_result_subques(out, problem, output, resampled):
    problem['resample'] = output
    problem['resampled'] = resampled
    out.write(json.dumps(problem, ensure_ascii=False) + '\n')

def resample_cot(SAMP_PATH, RES_PATH, PROMPT_PATH):

    BASE_PROMPT = read_prompt(PROMPT_PATH)
    
    with open(RES_PATH, "a") as out:
        for sample in tqdm(get_dataset(SAMP_PATH)):
            question = sample["question"]
            prediction = sample["prediction"]
            instruction = "You are a math teacher. Do you think the reasoning process for the given problem is correct? Let's check the 'Answer' in details, and then decide 'Yes' or 'No' and then write the correct 'Final Answer'"
            prompt = f"{BASE_PROMPT}\nQuestion: {question}\nAnswer: {prediction}\n{instruction}\nAnswer: "

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

def resample_or_not(CHECK_PROMPT, main_ques, prev_qa, qa_pair):
    print ("Checking if resample or not!")
    prompt_guide = "You are a math teacher. Do you think the reasoning process for the given problem is correct? Let’s check the 'Answer' in details, and then decide 'Yes' or 'No' and then write the correct 'Final Answer'."
    prompt = f"{CHECK_PROMPT}\nHere is a math question and its solution.\nProblem: {main_ques}\n{prev_qa}\nQuestion: {qa_pair[0]}\nAnswer:{qa_pair[1]}\n{prompt_guide}\nAnswer: "
    
    not_responded_yet = True
    while not_responded_yet:
        try:
            response = openai.Completion.create(
                        model="gpt-3.5-turbo-instruct",
                        prompt=prompt,
                        max_tokens=10,
                        temperature=0
                    )
            not_responded_yet = False
        except:
            print("retrying\n")

    output = response.choices[0]["text"]
    return output

def sampling_subques(SAMPLE_PROMPT, main_ques, prev_qa, qa_pair):
    print ("Sampling next step")
    prompt = f"{SAMPLE_PROMPT}\nProblem: {main_ques}\n{prev_qa}\nQ: {qa_pair[0]}\nA:"    
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
    return output

def resample_subques(SAMP_PATH, RES_PATH, SAMPLE_PROMPT_PATH, RESAMPLE_PROMPT_PATH):
    
    SAMPLE_PROMPT = read_prompt(SAMPLE_PROMPT_PATH)
    RESAMPLE_PROMPT = read_prompt(RESAMPLE_PROMPT_PATH)

    with open(RES_PATH, "a") as out:
        for samp in tqdm((get_dataset(SAMP_PATH))):
            main_ques = samp['question']
            qa_pairs = samp['prediction']
            output, resampled= [], []
            resampling, correctness = False, True
            prev_qa = ""
            for qa_pair in qa_pairs:
                sample_confidence = True
                if sample_confidence:
                    resampling = True
                    if correctness:
                        output_samp = resample_or_not(RESAMPLE_PROMPT, main_ques, prev_qa, qa_pair)
                        yes_no = output_samp.split("Final Answer:")[0]
                        # ans = output_samp.split("Final Answer:")[1]
                        if "No," in yes_no:
                            correctness = False
                            ans = sampling_subques(SAMPLE_PROMPT, main_ques, prev_qa, qa_pair)
                            resampled.append([1])
                        else:
                            ans = qa_pair[1]
                            resampled.append([0])
                    else:
                        ans = sampling_subques(SAMPLE_PROMPT, main_ques, prev_qa, qa_pair)
                        resampled.append([1])
                prev_qa += f"{qa_pair[0]} {ans}\n"
                output.append([qa_pair[0], ans])
            store_result_subques(out, samp, output, resampled)

def main(args):
    # call inference function for sampling
    openai.api_key = args.openai_key
    if args.sampling_type == "cot":
        resample_cot(args.sample_path, args.result_path, args.resample_prompt_path)
    elif args.sampling_type == "subques":
        resample_subques(args.sample_path, args.result_path, args.sample_prompt_path, args.resample_prompt_path)
    else:
        print ("Choose between 'cot' or 'subques' strategy for resampling!")


if __name__ == "__main__":
    args = get_args()
    assert args.sample_path != "", "Please provide the data path for GSM8K"
    if args.sample_prompt_path == "":
        print ("Sampling in Zero Shot Setting!")

    if args.sampling_type == "subques":
        assert args.resample_prompt_path != "", "Please provide the resampling path for GSM8K"

    main(args)
