---
promptId: 'sitNature'
name: '🖼️ Generate a Nature photo'
description: 'Photographs in the dataset with these captions tend to showcase animals/nature in extraordinary positions and situations, works similarly to “Award-Winning” but is only for nature. This will also make animals/nature look more real and accurate.'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2, situational'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}}, Nature Photography