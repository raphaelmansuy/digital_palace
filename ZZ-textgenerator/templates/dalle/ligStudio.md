---
promptId: 'ligStudio'
name: '🖼️ Generate a Studio Lighting photo'
description: 'Dark/light background is imposed behind the subject, lighting accentuates details of the figure in the foreground.'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2,lighting'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}},Studio Lighting