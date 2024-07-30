
def inference(message, history):
    try:
        flattened_history = [item for sublist in history for item in sublist]
        full_message = " ".join(flattened_history + [message])
        messages_litellm = [{"role": "user", "content": full_message}] # litellm message format
        partial_message = ""
        for chunk in litellm.completion(model="gpt-3.5-turbo",
                                        messages=messages_litellm,
                                        max_new_tokens=512,
                                        temperature=.7,
                                        top_k=100,
                                        top_p=.9,
                                        repetition_penalty=1.18,
                                        stream=True):
            partial_message += chunk['choices'][0]['delta']['content'] # extract text from streamed litellm chunks
            yield partial_message
    except Exception as e:
        print("Exception encountered:", str(e))
        yield f"An Error occured please 'Clear' the error and try your question again"


gr.ChatInterface(
    inference,
    chatbot=gr.Chatbot(height=400),
    textbox=gr.Textbox(placeholder="Enter text here...", container=False, scale=5),
    description=f"""
    CURRENT PROMPT TEMPLATE: {model_name}.
    An incorrect prompt template will cause performance to suffer.
    Check the API specifications to ensure this format matches the target LLM.""",
    title="Simple Chatbot Test Application",
    examples=["Define 'deep learning' in once sentence."],
    retry_btn="Retry",
    undo_btn="Undo",
    clear_btn="Clear",
    theme=theme,
).queue().launch()        
