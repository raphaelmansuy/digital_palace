"""
This script shows how to use the Python implementation of METEOR.
"""
from nltk.translate import meteor_score
from nltk import word_tokenize

import nltk
# Calculate the BLEU score
nltk.download('wordnet', download_dir='/usr/local/share/nltk_data')


reference = "The quick brown fox jumps over the lazy dog"
candidate = "The fast brown fox jumps over the lazy dog"

tokenized_reference = word_tokenize(reference)
tokenized_candidate = word_tokenize(candidate)

score = meteor_score.meteor_score([tokenized_reference], tokenized_candidate)

print(score)
