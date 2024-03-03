---
promptId: 'getPhoto'
name: '🖼️ Generate a photo'
description: 'select a text and photo about it will be generated using Dalle-2'
author: 'Noureddine'
tags: 'photo, dalle-2'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}}