from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini pro model
model = genai.GenerativeModel("gemini-pro")

def get_gemini_res(qs):
    res = model.generate_content(qs)
    return res.text

# Initialize streamlit
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Corrected line
input_text = st.text_input("Input", key="input")

submit = st.button("Ask a question")

# When submit
if submit:
    res = get_gemini_res(input_text)
    st.subheader("The Response is")
    st.write(res)
