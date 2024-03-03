---
promptId: 'qua4K'
name: '🖼️ Generate a 4K/8K photo'
description: 'Images in the dataset with the caption “4K/8K” are of high production value therefore will look more professionally photographed if you add this modifier.'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2,quality'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}}, 4K/8K