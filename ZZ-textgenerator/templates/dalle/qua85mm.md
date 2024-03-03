---
promptId: 'qua85mm'
name: '🖼️ Generate a 85mm lens photo'
description: 'Quite zoomed in photo, a lot of background blur and detail on subject'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2,quality, lens'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}},85mm lens