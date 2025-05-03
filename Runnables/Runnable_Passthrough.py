from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatMistralAI(model ='mistral-small')

prompt1 = PromptTemplate(
    template = 'generate a joke about the following topic : {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='explain following joke : {topic}',
    input_variables=['topic']
)
parser = StrOutputParser()

joke_generator = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'generate': RunnablePassthrough(),
    'explain' : RunnableSequence(prompt2,model,parser)
})
final_chain = RunnableSequence(joke_generator,parallel_chain)
result = final_chain.invoke({'topic': 'space'})
print(result)