#a program that generates a report on a given topic and then provides its summary 
#purpose is to demonstrate a sequential chain with multiple stages

from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

first_prompt = PromptTemplate(
    template = 'generate a detailed report about {topic}',
    input_variables = ['topic']
)

second_prompt = PromptTemplate(
    template='summarize the following text {text}',
    input_variables=['text']
)

model = ChatMistralAI(model = 'mistral-small')

parser = StrOutputParser()

chain = first_prompt | model | parser | second_prompt | model | parser

result = chain.invoke({'topic' : 'global warming'})
print(result)