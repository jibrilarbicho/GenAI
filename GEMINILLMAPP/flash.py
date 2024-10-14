from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv('GENAI_API_KEY'))
model=genai.GenerativeModel("gemini-1.5-flash")
from PIL import Image

def get_gemini_response(input,image):
    if input!="":
        reponse=model.generate_content([input,image])
    else:
      reponse=model.generate_content(image)
    return reponse.text
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input = st.text_input("Input:",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)



submit = st.button("Tell me about the image")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is: ")
    st.write(response)
