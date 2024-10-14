from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
genai.configure(api_key=os.getenv('GENAI_API_KEY'))
model=genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input,image,prompt):
    try:
       reponse=model.generate_content([input,image[0],prompt])
       return reponse.text
    except Exception as e:
        st.error(f"Error generating content: {e}")
        return None

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
input_prompt="""You are Expert in understanding Invoices.We will 
upload image as Invoice and you will have to asnwer 
any question based on the uploaded invoice image. """
    
st.set_page_config(page_title="MultiLanguage Invoice Exactor")
st.header("MultiLanguage Invoice Exactor")
input = st.text_input("Input:",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")
if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is: ")
    st.write(response)


