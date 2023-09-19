"""
This example shows how to use BERTScore to compute precision, recall, and F1
"""
import torch
from bert_score import score

cands = ['The quick brown dog jumps over the lazy fox.']
refs = ['The quick brown fox jumps over the lazy dog.']

P, R, F1 = score(cands, refs, lang='en', verbose=True)
print(F1)
