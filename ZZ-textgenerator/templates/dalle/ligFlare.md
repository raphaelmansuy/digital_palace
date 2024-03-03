---
promptId: 'ligFlare'
name: '🖼️ Generate a Lens Flare photo'
description: 'Adds a streak of light onto an image generation, creating the appearance of a bright light source being just outside of the frame.'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2,lighting'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}},Lens Flare