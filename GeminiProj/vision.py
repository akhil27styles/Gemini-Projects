from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini pro model
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_res(input,image):
    if input!="":
        res=model.generate_content([input,image])
    else:
        res=model.generate_content(image)
    return res.text

# Initialize streamlit
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Corrected line
input= st.text_input("Input", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="uploaded Image",use_column_width=True)


submit = st.button("Ask me about this image")

# When submit
if submit:
    res = get_gemini_res(input,image)
    st.subheader("The Response is")
    st.write(res)
