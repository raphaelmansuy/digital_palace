---
promptId: 'qua35mm'
name: '🖼️ Generate a 35mm lens photo'
description: 'Reasonable amount of background blur, reasonable zoom level.'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2,quality,lens'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}},35mm lens