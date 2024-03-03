---
promptId: 'modAwardWinning'
name: '🖼️ Generate a Award-Winning Art photo'
description: 'Images in the dataset with captions like “Award-Winning Art” are usually extremely creative and original, so using this modifier can greatly improve the quality and inventiveness of your generations.'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2, modifier'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}}, Award-Winning Art