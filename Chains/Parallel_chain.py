# a program that generates notes on a topic along with quiz
# purpose is to demonstrate parallel chains in langchain

from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()

model_1 = ChatMistralAI(model = 'mistral-large-latest')
model_2 = ChatMistralAI(model = 'mistral-small')

prompt_1 = PromptTemplate(
    template='generate concise yet comprehensive notes on following : {text} \n',
    input_variables=['text']
    )
prompt_2 = PromptTemplate(
    template='generate a quiz with 10 questions based on following text: {text}',
    input_variables=['text']
)

prompt_3 = PromptTemplate(
    template='merge the provided notes and quiz into a single  document \n notes -> {notes} and quiz -> {quiz}',
    input_variables= ['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt_1 | model_1 | parser,
    'quiz' : prompt_2 | model_2 | parser
})

merger = prompt_3 | model_1 | parser

chain = parallel_chain | merger
text =""" Support Vector Machines in Machine Learning"""
result = chain.invoke({'text' : text})
print(result)