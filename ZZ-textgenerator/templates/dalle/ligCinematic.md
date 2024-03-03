---
promptId: 'ligCinematic'
name: '🖼️ Generate a Cinematic Lighting photo'
description: 'Movie-like imagery with dramatic shadowing and very strong vibrancy, it also seems to add sun rays whenever it can.'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2, lighting'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}}, Cinematic Lighting