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

template = PromptTemplate(
    template= """
Please summarize the research paper titled "{topic}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input} 

1. Mathematical Details: 
    - explain the mathematical concepts presented in the paper.
    - provide intuitive code snippets where required.

2. Analogies:
    - use relatable analogies to simplify complex ideas.

If you do not have enough data, say that instead of guessing.
Ensure the summary is clear, concise, and aligned with the specified style.
"""
)

prompt = template.invoke({
    'topic' : topic,
    'style_input' : style_input,
    'length_input': length_input
})

if st.button('summarize') :
    result = model.invoke(prompt)
    st.write(result.content)

