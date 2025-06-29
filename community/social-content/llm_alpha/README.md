# Leveraging ALPHAZERO-LIKE TREE-SEARCH To Unlock The Full Potential Of Large Language Models

Recent advances in large language models have demonstrated their impressive capabilities in natural language tasks. 

However, most LLMs today still employ simple decoding strategies like greedy search or beam search during text generation. 

While effective, these decoding methods lack the lookahead and strategic planning of more advanced search algorithms.

A promising approach to enhance LLMs is to leverage principled search techniques like Monte Carlo Tree Search (MCTS), which has proven revolutionary in game-playing agents like AlphaGo and AlphaZero. 

By constructing a search tree of future possible actions and evaluations, MCTS allows an agent to "look ahead" many moves and pick the most promising path.

Recent works have adapted MCTS for improving LLM reasoning by guiding multi-step inference. However, existing methods rely heavily on prompting large, advanced LLMs to provide accurate evaluations within the search tree. This limits their scalability and general applicability.

A new technique called ALPHAZERO-LIKE TREE-SEARCH for LLMs (TS-LLM) provides a more flexible framework to unlock the benefits of structured search. TS-LLM introduces two key innovations:

1. It trains an auxiliary neural network to evaluate nodes in the search tree, instead of relying on internal LLM evaluations. This allows TS-LLM to guide any LLM's decoding, without needing scale or prompting.

2. The tree search process can be used to improve an LLM's parameters through policy iteration, in addition to enhancing inference. TS-LLM essentially uses search to provide supervised training signal.

Through comprehensive experiments, TS-LLM achieved significant gains over baselines on reasoning, planning, and alignment tasks. For example, on a mathematical game called Game24, TS-LLM solved 63% of problems correctly, compared to just 13% for unaided greedy decoding. TS-LLM also worked for LLMs ranging from 125M to 7B parameters.

Notably, TS-LLM succeeded on tasks requiring search trees with up to 64 layers. This showcases structured search as a promising technique to better exploit large LLMs' latent capabilities. With most models still using simple decoding, TS-LLM illustrates the headroom for more advanced search algorithms to unlock LLMs' full potential.

The "ALPHAZERO-LIKE TREE-SEARCH" published UCL and  paper provides an excellent walkthrough of this approach: https://arxiv.org/abs/2309.17179 Key aspects include:

- Formulating text generation as a Markov Decision Process to allow tree search.
- Architecting the search tree, with sentence or token level expansions.
- Training a neural value network to evaluate nodes, using RL-style methods.
- Conducting MCTS or similar search guided by the value network.
- Aggregating results from multiple searches to improve robustness.  
- Iteratively improving the LLM policy based on search results.

For NLP researchers and practitioners, TS-LLM is an intriguing demonstration of how structured search can enhance LLMs. While engineering challenges remain in scaling up, this points to a promising direction for the field. With most progress in LLMs now driven by scale, algorithmic innovations like TS-LLM suggest we still have much to unlock from existing models as well.

I'm keen to see how tree search and other advanced decoding methods can make LLMs even more capable and reliable. Please reach out if you have thoughts on TS-LLM or other techniques to improve LLMs!
