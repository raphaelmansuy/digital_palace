---
promptId: speakAlloy
name: "🗞️TTS: speak in alloy's voice"
description: speaks the selected text
author: Noureddine
tags:
  - TTS
  - alloy
version: 0.0.1
disableProvider: true
---
{{#script}}
```js
const AUDIO_TEXT = this.selection;
if(!AUDIO_TEXT || AUDIO_TEXT?.length < 3) 
throw new Error("You need to select some text before running this template")
```
{{/script}}


```handlebars
You can structure your code here and then use the input or output template to retrieve("get" helper) the processed data, enhancing readability.
```
***
If you wish to utilize this template with a provider, such as Chatbot or another service, please follow these steps:
- Enable the provider by setting 'disabledProvider' to false.
- Cut and paste everything from the output template into this section.
- Replace the content in the output template with '{{output}}'.
- Remember to delete this instruction text.
***
{{#script}}
```js
const OPENAI_API_KEY = plugin.getApiKeys().openAIChat 

async function generateAudioAndSaveToVault(text) {
  try {
    // Set up the request headers and body
    const requestOptions = {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${OPENAI_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'tts-1',
        input: text,
        voice: 'alloy'
      })
    };

    // Make the request to OpenAI's API
    const response = await fetch('https://api.openai.com/v1/audio/speech', requestOptions);

    if (!response.ok) {
      throw new Error(`OpenAI API request failed with status ${response.status}`);
    }

    // Get the audio buffer from the response
    const audioBuffer = await response.arrayBuffer();

    // Generate a random file name
    const randomFileName = `generated-audio-${Math.random().toString(36).substring(2, 15)}.mp3`;
    const filePath = `mp3/${randomFileName}`; // Prepend the "mp3" directory to the file name

    // Use Obsidian's Vault API to save the audio file in MP3 format
    const vault = app.vault; // Assuming this script has access to `app` from Obsidian environment

    // Check if the "mp3" directory exists, if not, create it
    let mp3Dir = vault.getAbstractFileByPath('mp3');
    if (!mp3Dir) {
      await vault.createFolder('mp3');
    }
    
    // Check if file exists, if so, remove it before writing new content
    let existingFile = vault.getAbstractFileByPath(filePath);
    if (existingFile && existingFile instanceof TFile) {
      await vault.delete(existingFile);
    }
    
    await vault.createBinary(filePath, audioBuffer);

    // Insert a link to the new audio file into the current note
    const editor = app.workspace.getMostRecentLeaf().view.editor;
    return `![Generated Audio](${filePath})\n`;
  } catch (error) {
    console.error('Error generating or saving audio:', error);
  }
}

// Call the function to generate audio and save it in the vault
const AUDIO_TEXT = this.selection;
return await generateAudioAndSaveToVault(AUDIO_TEXT);
```
{{/script}}
