# simple code to demonstrate runnable sequences

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'explain the following joke : {joke}',
    input_variables=['joke']
)

model = ChatMistralAI(model = 'mistral-small')
parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser,prompt2,model,parser)

print(chain.invoke({'topic':'AI'}))