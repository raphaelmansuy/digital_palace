
# GPT in 60 lines of NumPy

## Summary

[Jay Mody's](https://jaykmody.com/) article, ["GPT in 60 Lines of NumPy"](https://jaykmody.com/blog/gpt-from-scratch/) published on January 30, 2023, provides a concise guide to implementing a Generative Pre-trained Transformer (GPT) using just 60 lines of NumPy code. The post is designed for readers with a basic understanding of Python, NumPy, and neural network training. It deliberately omits many features to maintain simplicity while offering a complete introduction to GPT architecture as an educational tool. The implementation involves loading trained GPT-2 model weights from OpenAI and generating text, showcasing the fundamental aspects of GPTs, including their generative capabilities, pre-training on diverse datasets, and transformer-based architecture.


```cardlink
url: https://jaykmody.com/blog/gpt-from-scratch/
title: "GPT in 60 Lines of NumPy | Jay Mody"
description: "Implementing a GPT model from scratch in NumPy."
host: jaykmody.com
favicon: https://jaykmody.com/favicons/favicon-32x32.png
image:  https://jaykmody.com/profile.png 
```


The article covers the GPT basics, input/output processing, text generation through autoregressive sampling, and the training process. It explains the GPT function signature, tokenization, and output probability predictions. The text generation section details autoregressive and sampling methods for creating sentences. Training is discussed with a focus on gradient descent and self-supervised learning, highlighting the importance of large-scale data and model parameters for effective pre-training.

Additionally, the post touches on fine-tuning for specific tasks without the need for retraining from scratch, leveraging transfer learning. It also introduces prompting as a method to guide GPT models in generating contextually relevant responses.

The technical setup for implementing the GPT model is provided, including code for basic neural network layers like GELU, softmax, layer normalization, and linear layers. The GPT architecture is broken down into embeddings, decoder stack, and projection to vocabulary, with detailed explanations of each component, including token and positional embeddings, transformer blocks, and the final output generation.

The article concludes with potential enhancements and optimizations for the GPT model, such as GPU/TPU support, backpropagation, batching, inference optimization, and various fine-tuning strategies to improve model performance and efficiency.

## Code

[https://github.com/jaymody/picoGPT](https://github.com/jaymody/picoGPT)

## Other articles from the author


```cardlink
url: https://jaykmody.com/blog/speculative-sampling/
title: "Speculative Sampling | Jay Mody"
description: "A review of"
host: jaykmody.com
favicon: https://jaykmody.com/favicons/favicon-32x32.png
image:  https://jaykmody.com/profile.png 
```



```cardlink
url: https://jaykmody.com/blog/stable-softmax/
title: "Numerically Stable Softmax and Cross Entropy | Jay Mody"
description: "Tricks to make softmax and cross entropy calculations numerically stable."
host: jaykmody.com
favicon: https://jaykmody.com/favicons/favicon-32x32.png
image:  https://jaykmody.com/profile.png 
```



```cardlink
url: https://jaykmody.com/blog/gpt-from-scratch/
title: "GPT in 60 Lines of NumPy | Jay Mody"
description: "Implementing a GPT model from scratch in NumPy."
host: jaykmody.com
favicon: https://jaykmody.com/favicons/favicon-32x32.png
image:  https://jaykmody.com/profile.png 
```

```cardlink
url: https://jaykmody.com/blog/attention-intuition/
title: "An Intuition for Attention | Jay Mody"
description: "Deriving the equation for scaled dot product attention."
host: jaykmody.com
favicon: https://jaykmody.com/favicons/favicon-32x32.png
image:  https://jaykmody.com/profile.png 
```


```cardlink
url: https://jaykmody.com/blog/distance-matrices-with-numpy/
title: "Computing Distance Matrices with NumPy | Jay Mody"
description: "Efficiently computing distances matrixes in NumPy."
host: jaykmody.com
favicon: https://jaykmody.com/favicons/favicon-32x32.png
image:  https://jaykmody.com/profile.png 
```
