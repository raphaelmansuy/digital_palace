# Demystifying Classifiers and Embeddings

## Information

| Author         | Created    | Updated    | Version |
| -------------- | ---------- | ---------- | ------- |
| Raphaël MANSUY | 07/09/2023 | 07/09/2023 | 0.0.1   |

## Introduction

Classifiers and embeddings are two important techniques used in machine learning for natural language processing tasks.

Classifiers are algorithms that assign data points to different categories or classes.

A simple example is a model that classifies fruits on a 2D plot of sweetness versus acidity. However, real-world classification tasks are often high-dimensional and require complex models and data representations.

There are many classifier architectures like neural networks, SVMs, random forests etc. that have tradeoffs in accuracy, interpretability and efficiency.

Embeddings are vector representations of words, sentences or images that capture semantic meaning and relationships. They are usually learned by training neural networks on large datasets rather than manually engineered. Embeddings serve as input features to classifiers and other downstream models, allowing them to operate on dense vectors rather than sparse raw inputs like text.

While conceptually distinct, classifiers and embeddings work closely together in modern NLP and computer vision systems. Embeddings provide meaningful representations as input to classifiers and other models. Choices of embedding and classifier architectures impact overall performance. There are still many open challenges in designing optimal embeddings and classifiers for real-world applications.

## A short introduction to classifiers and embeddings

Suppose we choose a space with 2 dimensions:

- x-axis: The level of sweetness
- y-axis: The level of acidity

And we try to encode a set of fruits according to theses characteristics.

| Fruit Name | Emoji |
| ---------- | ----- |
| Apple      | 🍎    |
| Orange     | 🍊    |
| Banana     | 🍌    |
| Grape      | 🍇    |

**Encoders**:

Encoders are algothms that take as input a discrete item, such as a word, and outputs a vector of continuous values.

- **For language analysis**: the vector values are learned in relation to other words in the vocabulary, so that words that share common contexts in the corpus are located in close proximity to one another in the vector space.
- **For pictures or comptuer vision tasks**: the vector values are learned in relation to other pictures in the dataset, so that pictures that share common features in the dataset are located in close proximity to one another in the vector space.

![Encoder function](./assets/fruit_encoder.excalidraw.png)

**Classifiers**:

Classifiers are algorithms that assign data points to different categories or classes. In this example, the classifier is a simple 2D plot of sweetness versus acidity that can be used to find the correct fruit. However, real-world classification tasks are often high-dimensional and require complex models and data representations.

![Fruit classifier](./assets/fruit_classifier.excalidraw.png)

**The full classification of fruits is shown below**:

[![Fruit classifier](./assets/acivity_vs_sweetness.png)

Specifically, the classifier here outputs two values - the x coordinate representing sweetness, and the y coordinate representing acidity. By mapping fruits to locations in this 2D space, the classifier is categorizing the fruits based on their levels of sweetness and acidity.

**Some key properties of this encoder**:

- **Inpu**t: Name of a fruit (Apple, Orange, etc)
- **Output**: 2D coordinates (x,y) representing sweetness and acidity levels
- **Mapping**: Assigns fruits to locations in 2D plot based on inherent properties of sweetness and acidity
- **Categories**: Divides fruits into regions of the 2D space based on sweetness and acidity levels

Classifiers play a key role in supervised learning, allowing models to learn patterns from data and then apply those learnings to categorize new data points. They are essential tools for tasks like image recognition, document classification, and many other applications.

## What are Embeddings ?

Embeddings in the context of machine learning are vector representations of words, sentences, or images that capture semantic meaning and relationships. They are learned by training neural networks on large datasets, rather than being manually engineered.

For computer vision tasks, embeddings are learned in relation to other images in the dataset. This allows similar images to be located close to each other in the vector space. For example, if two images have similar features, their embeddings will be close together.

In the context of Large Language Models (LLMs), embeddings represent words as vectors of numbers that encode their meaning and relationships to other words. LLMs understand that similar words have similar embeddings. Embeddings reduce the dimensionality of language, transforming sparse, high-dimensional text data into dense, low-dimensional vectors. This enables tasks like sentiment analysis.

**Some key properties of embeddings**:

- **Input**: Discrete item (word, user, product, etc)
- **Output**: Vector of continuous values
- **Mapping**: Assigns items to locations in vector space based on context
- **Categories**: Divides items into regions of the vector space based on context

**Key points embeddings in the context of LLMs (Large Language Models)**:

- Embeddings represent words as **vectors of numbers** that encode their **meaning and relationships** to other words
- This allows models to understand that **similar words** have **similar embeddings**.
- Embeddings **reduce the dimensionality of language**, transforming sparse, high-dimensional text data into **dense, low-dimensional vectors**
- This makes it feasible to **train models on huge datasets**.
- Embeddings capture semantics, meaning if two words have similar embeddings, the model understands they have **similar meanings**: this enables tasks like **sentiment analysi**s.
- Earlier models like **Word2Vec** generated **static embeddings**, but modern models like **BERT** learn **contextual embeddings** which better capture nuance
- Embeddings are combined through operations like **averaging** to obtain **sentence-level** and **document-level** representations

In the context of large language models (LLMs), embeddings play a crucial role in capturing the meanings of text and transforming text into a hyperspace with n dimensions of meaning.
By representing words as vectors of numbers that encode their meaning and relationships to other words, LLMs can understand that similar words have similar embeddings.

## Mathematical Manipulation of Meaning: How Vector Representations Revolutionize Language Analysis

Because words and sentences can be represented as vectors, language takes on a mathematical structure.

Vectors are mathematical objects that can be combined through operations like addition and multiplication.

So by transforming text into vectors, we unlock the ability to mathematically manipulate meaning for the first time.

We can take the vector for "king" and subtract the vector for "man" to get something close to the vector for "queen".

This reveals an underlying structure where related concepts are mapped to similar vectors.

By applying mathematical operations on these word and sentence vectors, we can now do algebra, calculus, and more on the latent meanings they represent.

This mathematical framework powers our ability to analyze and generate language in entirely new ways.

Vector representations are a profound leap forward, enabling us to mathematically reason about the semantics of language.

### Resources

| Short Name                                     | Description                                                                                                            | Link                                                                                                                                         |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Intuitive Guide to Word2vec                    | A guide to understanding Word2vec and its ability to capture semantic relationships between words                      | [Towards Data Science](https://towardsdatascience.com/light-on-math-machine-learning-intuitive-guide-to-understanding-word2vec-e0128a460f0f) |
| Word Vectors and Word Meanings                 | An article discussing whether word vectors capture the meaning of words and the theory of meaning that suits them best | [Towards Data Science](https://towardsdatascience.com/word-vectors-and-word-meaning-90493d13af76)                                            |
| What is a Vector Embedding?                    | A brief explanation of vector embeddings and their importance in machine learning and NLP                              | [DEV Community](https://dev.to/josethz00/what-is-a-vector-embedding-3335)                                                                    |
| Understanding Word Vectors                     | A GitHub gist that provides a tutorial on understanding word vectors and their applications                            | [GitHub](https://gist.github.com/aparrish/2f562e3737544cf29aaf1af30362f469)                                                                  |
| Word2Vec: Why Do We Need Word Representations? | An article explaining the need for word representations and the impact of Word2Vec on capturing semantic information   | [Serokell](https://serokell.io/blog/word2vec)                                                                                                |

## Word2vec

### Resources

| Short Name           | Description                                                              | Resources                                           |
| -------------------- | ------------------------------------------------------------------------ | --------------------------------------------------- |
| Word2vec             | A group of related neural network models used to produce word embeddings | [1][2][3][4][5][6][7][8][9][10][11][12][13][14][15] |
| Word embedding       | The process of mapping words to vectors of real numbers                  | [1][2][3][4][5][6][7][8][9][10][11][12][13][14][15] |
| Vector space         | A mathematical space where words are represented as vectors              | [1][2][3][4][5][6][7][8][9][10][11][12][13][14][15] |
| CBOW                 | Continuous Bag of Words model that predicts target words from context    | [2][7][8][11][12][13][14][15]                       |
| Skip-gram            | Model that predicts context words from target words                      | [2][7][8][11][12][13][14][15]                       |
| Hierarchical softmax | Efficient approximation of full softmax for training                     | [13]                                                |
| Negative sampling    | Alternative to softmax for training                                      | [13]                                                |

The key concepts related to word2vec are word embedding models like CBOW and skip-gram that map words to vector representations in a vector space. The vectors capture semantic relationships between words. These models are trained on large corpora to produce useful word embeddings.

Citations:

[1] https://en.wikipedia.org/wiki/Word2vec
[2] https://wiki.pathmind.com/word2vec
[3] https://www.guru99.com/word-embedding-word2vec.html
[4] http://jalammar.github.io/illustrated-word2vec/
[5] https://stackoverflow.com/questions/50906372/word2vec-and-abbreviations
[6] https://www.coveo.com/blog/word2vec-explained/
[7] https://towardsdatascience.com/word2vec-explained-49c52b4ccb71
[8] https://medium.com/@data_datum/nlp-concepts-word-embeddings-99337bf98b3
[9] https://towardsdatascience.com/a-beginners-guide-to-word-embedding-with-gensim-word2vec-model-5970fa56cc92
[10] https://mccormickml.com/2016/04/27/word2vec-resources/
[11] https://serokell.io/blog/word2vec
[12] https://www.tensorflow.org/text/tutorials/word2vec
[13] https://radimrehurek.com/gensim/models/word2vec.html
[14] https://builtin.com/machine-learning/nlp-word2vec-python
[15] https://www.analyticsvidhya.com/blog/2021/07/word2vec-for-word-embeddings-a-beginners-guide/
