---
promptId: 'modDetailed'
name: '🖼️ Generate a photo, with more precise details'
description: 'Adds more precise details to the output, instead of simple art, but can also make the art overwhelming/over the top in small details.'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2,modifier'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}}, Detailed