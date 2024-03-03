---
promptId: 'qua200mm'
name: '🖼️ Generate a 200mm lens photo'
description: 'Extremely zoomed in photo, tons of background blur, & will look like it was photographed from a far distance and then zoomed in a lot (good for photos of flying birds, small animals).'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2,quality,lens'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}}, 200mm lens