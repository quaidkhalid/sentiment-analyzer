import streamlit as st
import openai

# (make sure to replace 'your-api-key' with your actual OpenAI API key)
openai.api_key = "your-api-key"

def get_response_chatgpt(text):
    prompt=f"Identify and return the sentiment either positive or negative in given text. text: {text}"
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages =[{"role":"system", "content":"You are a helpful sentiment analyzer that returns concise sentiment"},
                   {"role":"user", "content":prompt}
        ],
        temperature = 0.1
    )

    sentiment = response['choices'][0]['message']['content']
    return sentiment

    
st.title("ChatGPT text sentiment analyzer")
model = 'gpt-3.5-turbo'
text = st.text_input("Enter Text: ", value = "I love you.")

if st.button("submit"):
    with st.spinner("OpenAI processing in progress"):
        sentiment = get_response_chatgpt(text)
        st.success("OpenAI processing complete")
    
    st.write(f"sentiment: {sentiment}")
    # display sentiment to user





