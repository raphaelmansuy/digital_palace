---
promptId: 'modFanart'
name: '🖼️ Generate a Fanart photo'
description: 'This gives the generation a cute young amateur graphic design feel, adding hearts to the image and so on.'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2, modifier'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}}, Fanart