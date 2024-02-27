from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_res(qs):
    res=chat.send_message(qs,stream=True)
    return res
#intitalize our streamlit

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

#Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
    res=get_gemini_res(input)
    #add query and res
    st.session_state['chat_history'].append(("You",input))
    st.subheader("Response is")
    for chunk in res:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("The chat history is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")