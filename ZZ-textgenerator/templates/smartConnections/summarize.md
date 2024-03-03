---
promptId: summarize
name: 🗞️Summarize The Results of Smart Connections
description: summarize
author: Noureddine
tags:
  - smart-connections
version: 0.0.1
disableProvider: true
provider:
---
{{#script}}
```js
if(!app.plugins.plugins["smart-connections"]) 
	return error("Smart connection plugin not installed")
```
{{/script}}
***
This input template is currently disabled due to the 'disabledProvider' setting being set to true.

If you wish to utilize this template with a provider, such as Chatbot or another service, please follow these steps:
- Enable the provider by setting 'disabledProvider' to false.
- Cut and paste everything from the output template into this section.
- Replace the content in the output template with '{{output}}'.
- Remember to delete this instruction text.
***
{{#script}}
```js
const query = this.tg_selection;
const results = await app.plugins.plugins["smart-connections"].api.search(query);
const contextResults = await Promise.all(
  results.slice(0, 5).map(r => 
    app.plugins.plugins["smart-connections"].file_retriever(r.link, { lines: 10, max_chars: 1000 })
  )
);
const context = contextResults.join("\n---\n");

const summary = await gen(`
Query: 
${query}

Outcomes: 
${context}

Prompt:
Synthesize the results section, highlighting the relationship between the initial query and the outcomes. Structure the content using Markdown formatting to establish a clear information hierarchy. This should include titles, subtitles, and varying font sizes. For improved readability, bolden all verbs and specific action-oriented phrases. Ensure that the Markdown elements are properly used to organize the content systematically.

Summary: 

`)

return summary;
```
{{/script}}
