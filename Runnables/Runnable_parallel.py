from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel


load_dotenv()
model1 = ChatMistralAI(model ='mistral-small')
model2 = ChatMistralAI(model = 'mistral-large-latest')

prompt1 = PromptTemplate(
    template = 'generate a linkedin post about the following topic : {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='generate a tweet about following topic : {topic}',
    input_variables=['topic']
)
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt2,model1,parser),
    'linkedin':RunnableSequence(prompt1,model2,parser)
})

result = (parallel_chain.invoke({'topic': 'DevOps'}))
print(result)