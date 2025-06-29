# 📄 Research Paper Collection

## Foundation Papers (Must-Read)

### Transformer Architecture

#### Attention Is All You Need (2017)
- **Authors**: Vaswani et al. (Google)
- **Venue**: NIPS 2017
- **Impact**: Introduced the Transformer architecture
- **Key Contributions**: Self-attention mechanism, parallel processing
- **Why Important**: Foundation of modern LLMs (GPT, BERT, etc.)
- **Link**: [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)

#### BERT: Pre-training of Deep Bidirectional Transformers (2018)
- **Authors**: Devlin et al. (Google)
- **Venue**: NAACL 2019
- **Impact**: Bidirectional language understanding
- **Key Contributions**: Masked language modeling, next sentence prediction
- **Why Important**: Revolutionary NLP fine-tuning approach
- **Link**: [arXiv:1810.04805](https://arxiv.org/abs/1810.04805)

### Large Language Models

#### Language Models are Few-Shot Learners (GPT-3, 2020)
- **Authors**: Brown et al. (OpenAI)
- **Venue**: NeurIPS 2020
- **Impact**: Demonstrated emergent abilities at scale
- **Key Contributions**: In-context learning, scaling laws
- **Why Important**: Showed potential of large-scale language models
- **Link**: [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)

#### Training language models to follow instructions (InstructGPT, 2022)
- **Authors**: Ouyang et al. (OpenAI)
- **Venue**: NeurIPS 2022
- **Impact**: Aligned LLMs with human preferences
- **Key Contributions**: RLHF, human feedback training
- **Why Important**: Foundation for ChatGPT and instruction-following models
- **Link**: [arXiv:2203.02155](https://arxiv.org/abs/2203.02155)

#### PaLM: Scaling Language Modeling with Pathways (2022)
- **Authors**: Chowdhery et al. (Google)
- **Venue**: arXiv 2022
- **Impact**: 540B parameter model with strong reasoning
- **Key Contributions**: Chain-of-thought reasoning, breakthrough performance
- **Why Important**: Demonstrated reasoning capabilities at scale
- **Link**: [arXiv:2204.02311](https://arxiv.org/abs/2204.02311)

### Retrieval-Augmented Generation

#### Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020)
- **Authors**: Lewis et al. (Facebook)
- **Venue**: NeurIPS 2020
- **Impact**: Combined retrieval with generation
- **Key Contributions**: RAG architecture, knowledge-grounded generation
- **Why Important**: Foundation for modern knowledge-augmented systems
- **Link**: [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

#### Dense Passage Retrieval for Open-Domain Question Answering (2020)
- **Authors**: Karpukhin et al. (Facebook)
- **Venue**: EMNLP 2020
- **Impact**: Dense retrieval for QA systems
- **Key Contributions**: Dense embeddings for passage retrieval
- **Why Important**: Improved retrieval for RAG systems
- **Link**: [arXiv:2004.04906](https://arxiv.org/abs/2004.04906)

## Recent Breakthroughs (2023-2024)

### Advanced Reasoning

#### Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (2022)
- **Authors**: Wei et al. (Google)
- **Venue**: NeurIPS 2022
- **Impact**: Improved reasoning through step-by-step thinking
- **Key Contributions**: CoT prompting, reasoning chain generation
- **Why Important**: Unlocked reasoning capabilities in LLMs
- **Link**: [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)

#### Tree of Thoughts: Deliberate Problem Solving with Large Language Models (2023)
- **Authors**: Yao et al. (Princeton)
- **Venue**: NeurIPS 2023
- **Impact**: Structured reasoning beyond chains
- **Key Contributions**: Tree search for LLM reasoning
- **Why Important**: Advanced problem-solving strategies
- **Link**: [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)

### Multimodal Models

#### GPT-4V(ision) System Card (2023)
- **Authors**: OpenAI Team
- **Venue**: Technical Report 2023
- **Impact**: Multimodal understanding capabilities
- **Key Contributions**: Vision-language integration, safety considerations
- **Why Important**: Breakthrough in multimodal AI
- **Link**: [OpenAI Technical Report](https://cdn.openai.com/papers/GPTV_System_Card.pdf)

#### CLIP: Learning Transferable Visual Representations (2021)
- **Authors**: Radford et al. (OpenAI)
- **Venue**: ICML 2021
- **Impact**: Vision-language understanding
- **Key Contributions**: Contrastive learning, zero-shot classification
- **Why Important**: Foundation for vision-language models
- **Link**: [arXiv:2103.00020](https://arxiv.org/abs/2103.00020)

### AI Agents & Planning

#### ReAct: Synergizing Reasoning and Acting in Language Models (2022)
- **Authors**: Yao et al. (Princeton)
- **Venue**: ICLR 2023
- **Impact**: Reasoning and acting framework
- **Key Contributions**: Interleaved thinking and acting
- **Why Important**: Foundation for AI agent frameworks
- **Link**: [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)

#### Toolformer: Language Models Can Teach Themselves to Use Tools (2023)
- **Authors**: Schick et al. (Meta)
- **Venue**: NeurIPS 2023
- **Impact**: Self-taught tool usage
- **Key Contributions**: Autonomous tool learning, API integration
- **Why Important**: Bridge between LLMs and external tools
- **Link**: [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

## Specialized Domains

### Fine-tuning & Adaptation

#### LoRA: Low-Rank Adaptation of Large Language Models (2021)
- **Authors**: Hu et al. (Microsoft)
- **Venue**: ICLR 2022
- **Impact**: Efficient fine-tuning method
- **Key Contributions**: Parameter-efficient adaptation
- **Why Important**: Practical fine-tuning for large models
- **Link**: [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)

#### QLoRA: Efficient Finetuning of Quantized LLMs (2023)
- **Authors**: Dettmers et al. (University of Washington)
- **Venue**: NeurIPS 2023
- **Impact**: Quantized model fine-tuning
- **Key Contributions**: 4-bit quantization with LoRA
- **Why Important**: Accessible fine-tuning on consumer hardware
- **Link**: [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)

### Model Evaluation

#### Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models (BIG-bench, 2022)
- **Authors**: Srivastava et al. (Google et al.)
- **Venue**: arXiv 2022
- **Impact**: Comprehensive LLM evaluation
- **Key Contributions**: Diverse task benchmark, capability assessment
- **Why Important**: Standard for LLM evaluation
- **Link**: [arXiv:2206.04615](https://arxiv.org/abs/2206.04615)

#### Measuring Mathematical Problem Solving With the MATH Dataset (2021)
- **Authors**: Hendrycks et al. (UC Berkeley)
- **Venue**: NeurIPS 2021
- **Impact**: Mathematical reasoning benchmark
- **Key Contributions**: Competition-level math problems
- **Why Important**: Tests advanced reasoning capabilities
- **Link**: [arXiv:2103.03874](https://arxiv.org/abs/2103.03874)

### Safety & Alignment

#### Constitutional AI: Harmlessness from AI Feedback (2022)
- **Authors**: Bai et al. (Anthropic)
- **Venue**: arXiv 2022
- **Impact**: Self-supervised safety training
- **Key Contributions**: AI feedback for alignment
- **Why Important**: Scalable safety approach
- **Link**: [arXiv:2212.08073](https://arxiv.org/abs/2212.08073)

## Implementation Papers

### Practical Systems

#### LangChain: Building applications with LLMs through composability (2022)
- **Authors**: Chase et al.
- **Venue**: Technical Report
- **Impact**: Framework for LLM applications
- **Key Contributions**: Composable LLM chains
- **Why Important**: Practical application development
- **Link**: [GitHub Documentation](https://github.com/langchain-ai/langchain)

#### LlamaIndex: A data framework for your LLM application (2022)
- **Authors**: Liu et al.
- **Venue**: Technical Report
- **Impact**: Data connectivity for LLMs
- **Key Contributions**: Index-based data access
- **Why Important**: Practical RAG implementation
- **Link**: [GitHub Documentation](https://github.com/run-llama/llama_index)

### Deployment & Optimization

#### FlashAttention: Fast and Memory-Efficient Exact Attention (2022)
- **Authors**: Dao et al. (Stanford)
- **Venue**: NeurIPS 2022
- **Impact**: Efficient attention computation
- **Key Contributions**: Memory-efficient attention algorithm
- **Why Important**: Practical efficiency improvements
- **Link**: [arXiv:2205.14135](https://arxiv.org/abs/2205.14135)

#### vLLM: Easy, Fast, and Cheap LLM Serving (2023)
- **Authors**: Kwon et al. (UC Berkeley)
- **Venue**: SOSP 2023
- **Impact**: Efficient LLM serving
- **Key Contributions**: PagedAttention, high-throughput serving
- **Why Important**: Production LLM deployment
- **Link**: [arXiv:2309.06180](https://arxiv.org/abs/2309.06180)

## Reading Lists by Focus Area

### For LLM Developers
1. **Foundation**: Attention Is All You Need
2. **Applications**: GPT-3 Paper (Few-shot learning)
3. **Fine-tuning**: LoRA, QLoRA
4. **Reasoning**: Chain-of-Thought, Tree of Thoughts
5. **Systems**: FlashAttention, vLLM

### For AI Researchers
1. **Architecture**: Transformer papers
2. **Scaling**: GPT-3, PaLM
3. **Reasoning**: CoT, ToT, ReAct
4. **Evaluation**: BIG-bench, MATH
5. **Safety**: Constitutional AI, InstructGPT

### For RAG Developers
1. **Foundation**: RAG paper
2. **Retrieval**: Dense Passage Retrieval
3. **Implementation**: LlamaIndex documentation
4. **Optimization**: Retrieval-focused papers
5. **Evaluation**: RAG evaluation benchmarks

### For Business Applications
1. **Capabilities**: GPT-3, GPT-4 papers
2. **Alignment**: InstructGPT
3. **Safety**: Constitutional AI
4. **Implementation**: LangChain, practical systems
5. **Evaluation**: Business-relevant benchmarks

## Paper Discovery Resources

### Venues to Follow

#### Top-Tier Conferences
- **NeurIPS**: Neural Information Processing Systems
- **ICML**: International Conference on Machine Learning
- **ICLR**: International Conference on Learning Representations
- **ACL**: Association for Computational Linguistics
- **EMNLP**: Empirical Methods in NLP

#### AI Company Publications
- **OpenAI**: GPT series, CLIP, DALL-E
- **Google/DeepMind**: Transformer, BERT, PaLM, Gemini
- **Anthropic**: Claude, Constitutional AI
- **Meta**: LLaMA, RAG, Toolformer

### Discovery Tools
- **Papers With Code**: Implementation tracking
- **arXiv Sanity**: Paper organization and search
- **Connected Papers**: Visual paper relationships
- **Semantic Scholar**: Academic search engine
- **Google Scholar**: Citation tracking

### Reading Strategies

#### For Busy Practitioners
1. Read abstract and conclusion first
2. Focus on methodology and results
3. Check implementation availability
4. Look for practical applications
5. Follow citation networks

#### For Deep Understanding
1. Read paper multiple times
2. Implement key algorithms
3. Compare with related work
4. Analyze experimental setup
5. Replicate results if possible

---

*Last updated: December 2024*
*Papers reviewed: 50+ foundational papers*
*Regular updates with new publications*
