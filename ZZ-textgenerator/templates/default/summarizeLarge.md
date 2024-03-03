---
promptId: summarizeLarge
name: 🗞️ Summarizes Large chunk of text
description: uses langchain chain to summarize large chunk of text
author: Noureddine
tags: writing, thinking, learning
version: 0.0.1
mode: insert
chain.type: map_reduce
splitter.chunkSize: 1000
splitter.chunkOverlap: 100
max_tokens: 1000
temperature: 0
chain.maxTokens: 1000
---
{{tg_selection}}
***
{{output}}