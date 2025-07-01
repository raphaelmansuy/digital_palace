
[![Back to TIL Hub](https://img.shields.io/badge/←%20Back%20to-TIL%20Hub-blue?style=for-the-badge)](README.md)

# What is openinterpreter

### Installation

```bash
pip install open-interpreter
```


## Usage

```bash
interpreter --model gpt-3.5-turbo
interpreter --model claude-2
interpreter --model command-nightly
```


### Example

```text

Your task Write a python 3.11 program, with bs4

The program will do:

Download the latest article about "Articial Intelligence" submited today and saved it to a file called with format "YYYY-MM-DD-arxiv".md on https://arxiv.org/search/cs?query=artificial+intelligence&searchtype=all&abstracts=show&order=-submitted_date&size=200.


Format the list as table in markdown, columns for the table:

- arxiv number, and link
- title
- authors
- abstract
- submited date: 


https://arxiv.org/search/cs?query=artificial+intelligence&searchtype=all&abstracts=show&order=-submitted_date&size=200


Example of article in the page list:


"""
1. [arXiv:2402.13254](https://arxiv.org/abs/2402.13254)  [[pdf](https://arxiv.org/pdf/2402.13254), [other](https://arxiv.org/format/2402.13254)] 
    
     
    
    cs.CV cs.AI cs.CL cs.LG
    
    CounterCurate: Enhancing Physical and Semantic Visio-Linguistic Compositional Reasoning via Counterfactual Examples
    
    Authors: [Jianrui Zhang](https://arxiv.org/search/?searchtype=author&query=Zhang%2C+J), [Mu Cai](https://arxiv.org/search/?searchtype=author&query=Cai%2C+M), [Tengyang Xie](https://arxiv.org/search/?searchtype=author&query=Xie%2C+T), [Yong Jae Lee](https://arxiv.org/search/?searchtype=author&query=Lee%2C+Y+J)
    
    Abstract: We propose CounterCurate, a framework to comprehensively improve the visio-linguistic compositional reasoning capability for both contrastive and generative multimodal models. In particular, we identify two critical under-explored problems: the neglect of the physically grounded reasoning (counting and position understanding) and the potential of using highly capable text and image generation mode… ▽ More
    
    Submitted 12 March, 2024; v1 submitted 20 February, 2024; originally announced February 2024.
    
    Comments: 13 pages, 6 figures, 8 tables, Project Page: https://countercurate.github.io/
"""


```


