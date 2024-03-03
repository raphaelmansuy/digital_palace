---
promptId: 'modArtStation'
name: '🖼️ Generate a Trending on ArtStation photo'
description: 'This modifier will sample extra training data from the most-liked artwork from the website ArtStation. Images which trend on ArtStation are usually very visually-appealing as it means the ArtStation community enjoys those images, so filtering the data to produce images similar to those will greatly increase the quality of the generated art.'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2, modifier'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}}, Trending on ArtStation