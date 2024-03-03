---
promptId: 'qua15mm'
name: '🖼️ Generate a 15mm wide-angle lens photo'
description: 'Very wide image with lots of information in the image.'
author: 'Prompt Engineering Guide'
tags: 'photo,dalle-2,quality,lens'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}},15mm wide-angle lens