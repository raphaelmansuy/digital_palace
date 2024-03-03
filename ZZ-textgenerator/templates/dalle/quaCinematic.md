---
promptId: 'quaCinematic'
name: '🖼️ Generate a cinematic movie photo'
description: 'Adds a very atmospheric movie-like feel to the image, with great color tones and image composure, and can also add nice background blur and pretty camera angles.'
author: 'Prompt Engineering Guide'
tags: 'photo, dalle-2,quality'
version: '0.0.1'
output: '\n![]({{requestResults.data.0.url}})'
provider: 'custom'
endpoint: 'https://api.openai.com/v1/images/generations'
body: '{"n": 1, "size": "1024x1024", "prompt": "{{escp prompt}}"}'
---
{{selection}}, Cinematic Movie Photograph