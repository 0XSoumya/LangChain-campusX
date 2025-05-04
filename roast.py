import gradio as gr
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables (API keys etc.)
load_dotenv()

# Setting up the LangChain components
prompt = PromptTemplate(
    template='write 5 light hearted roasts about for someone named {name}',
    input_variables=['name']
)

model = ChatMistralAI(model='mistral-small')
parser = StrOutputParser()

# Create the chain
chain = prompt | model | parser

# Define the function Gradio will call
def generate_facts(name):
    result = chain.invoke({'name': name})
    return result

# Create the Gradio interface
iface = gr.Interface(
    fn=generate_facts,
    inputs=gr.Textbox(lines=1, placeholder="Enter a name"),
    outputs="text",
    title="🎯 roast",
    description="Enter any name ! Powered by LangChain + Mistral."
)

# Launch the Gradio app
if __name__ == "__main__":
    iface.launch()
