from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st


load_dotenv()
model = ChatMistralAI(model='mistral-small')

st.header('Research Assistant')

topic = st.selectbox("Choose your paper", ["Attention is all you need","BErt","GPT-3","Diffusion Models Beat GANs on Image Synthesis"])
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

tempelate

if st.button('summarize') :
    result = model.invoke(user_input)
    st.write(result.content)

