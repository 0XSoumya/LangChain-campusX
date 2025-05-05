# a simple program to generate fun facts about a topic
# purpose is to demonstrate chains

from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

# creating prompt:
prompt = PromptTemplate(
    template = 'generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatMistralAI(model = 'mistral-small')
parser = StrOutputParser()

chain = prompt | model | parser # creating a simple chain

result = chain.invoke({'topic': 'baking'})

print(result)
            
chain.get_graph().print_ascii