"""
 This script shows how to compute BLEU score for a single sentence.
"""

from nltk.translate.bleu_score import sentence_bleu

reference = [['The', 'quick', 'brown', 'fox',
              'jumps', 'over', 'the', 'lazy', 'dog']]
candidate = ['The', 'quick', 'brown', 'dog',
             'jumps', 'over', 'the', 'lazy', 'fox']
score = sentence_bleu(reference, candidate)

print(score)
