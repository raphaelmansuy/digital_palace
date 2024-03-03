---
promptId: tts_listen
name: 🗞️TTS listen
description: listen to user reading
author: Noureddine
tags:
  - TTS
version: 0.0.1
disableProvider: true
---
```handlebars
You can structure your code here and then use the input or output template to retrieve("get" helper) the processed data, enhancing readability.
```
***
This input template is currently disabled due to the 'disabledProvider' setting being set to true.

If you wish to utilize this template with a provider, such as Chatbot or another service, please follow these steps:
- Enable the provider by setting 'disabledProvider' to false.
- Cut and paste everything from the output template into this section.
- Replace the content in the output template with '{{output}}'.
- Remember to delete this instruction text.
***

{{notice "listening.."}}
{{#script}}
```js

const OPENAI_API_KEY = plugin.getApiKeys().openAIChat;

async function sendAudioForTranscription(blob) {
    const formData = new FormData();
    formData.append('file', blob, 'audio.webm');
    formData.append('model', 'whisper-1');

    try {
        const response = await fetch('https://api.openai.com/v1/audio/transcriptions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${OPENAI_API_KEY}`,
            },
            body: formData
        });
        const jsonResponse = await response.json();
        if ("text" in jsonResponse) return updateTranscription(jsonResponse.text);

    } catch (err) {
        console.error('Error transcribing audio:', err);
        new Notice('Error transcribing audio');
        await stopTranscription();
    }
}

async function shouldSendAudio(blob) {
    return new Promise((resolve, reject) => {
        let audioContext = new AudioContext(options);
        let reader = new FileReader();

        reader.onload = async () => {
            try {
                let arrayBuffer = reader.result;
                let audioBuffer = await audioContext.decodeAudioData(arrayBuffer);

                let rawData = audioBuffer.getChannelData(0); // Get data of the first channel
                let blockSize = Math.floor(rawData.length / 100); // Divide into 100 blocks
                let filteredData = [];

                for (let i = 0; i < 100; i++) {
                    let blockStart = blockSize * i;
                    let sum = 0;

                    for (let j = 0; j < blockSize; j++) {
                        sum += Math.abs(rawData[blockStart + j]);
                    }

                    filteredData.push(sum / blockSize);
                }

                let threshold = 0.01; // Define your threshold for silence here
                let average = filteredData.reduce((a, b) => a + b) / filteredData.length;

                resolve(average >= threshold);
            } catch (err) {
                return false;
            }
        };

        reader.readAsArrayBuffer(blob);
    });
}


let mediaRecorder; // Global declaration of mediaRecorder
let audioChunks = []; // Global declaration of audioChunks
const options = { mimeType: "audio/webm" };
const startingTime = new Date();

async function stopTranscription() {
    if (mediaRecorder) {
        mediaRecorder.pause();
        mediaRecorder.stop(); // Stop the media recorder
        mediaRecorder = null; // Clear the mediaRecorder reference
        audioChunks = [];
        new Notice('Live transcription stopped');
    } else {
        new Notice('No active transcription to stop');
    }
}

function checkPassedTime() {
    // Calculate the time 10 seconds ago
    const tenSecondsAgo = new Date(startingTime.getTime() + 10 * 1000); // 10 seconds * 1000 milliseconds

    // Check if the current time has passed 10 seconds
    return new Date() > tenSecondsAgo;
}

function startTranscription() {
    return new Promise(async (resolve) => {
        if (!navigator.mediaDevices) {
            new Notice('Media devices not supported');
            return;
        }
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

        try {
            const redefineMediaRecorder = () => {
                mediaRecorder = new MediaRecorder(stream, options);
                mediaRecorder.ondataavailable = onData;

                mediaRecorder.onerror = async (err) => {
                    new Notice('mediaRecorder: ' + err.message);
                    console.error('mediaRecorder: ', err);

                    await stopTranscription();
                }

                mediaRecorder.start(5000); // Adjust the timeslice to control chunk size
            }

            redefineMediaRecorder()

            async function onData(e) {
                if (checkPassedTime()) return await stopTranscription();

                try {
                    audioChunks.push(e.data);


                    if (await shouldSendAudio(e.data)) {
                        mediaRecorder.pause();
                        mediaRecorder.stop();
                        // redefineMediaRecorder();
                        console.log("should send: ", e.data)
                        const combinedAudioBlob = new Blob(audioChunks, { 'type': 'audio/webm' });
                        await sendAudioForTranscription(combinedAudioBlob);
                        audioChunks = []; // Reset audioChunks after sending
                        resolve(res);
                    } else {
                        console.log("shouldn't send audio", e)
                    }
                } catch (err) {
                    new Notice('mediaRecorder(onDataAvailable): ' + err.message);
                    console.error('mediaRecorder(onDataAvailable): ', err);
                    await stopTranscription();
                }
            }
        } catch (err) {
            new Notice('Failed to start transcription: ' + err.message);
            await stopTranscription();
        }
    })
}


let res = "";
function updateTranscription(text) {
    res += text;
    console.log(text)
}

return await startTranscription()
```
{{/script}}
