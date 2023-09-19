"""
A simple example of how to use the rouge_scorer package.
"""

from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
scores = scorer.score('The quick brown dog jumps over the lazy fox.',
                      'The quick brown fox jumps over the lazy dog.')
print(scores)
