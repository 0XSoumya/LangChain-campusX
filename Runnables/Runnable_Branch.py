from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence , RunnablePassthrough , RunnableParallel , RunnableLambda, RunnableBranch
load_dotenv()

model = ChatMistralAI(model = 'mistral-small')
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'write a detailed report on the topic : {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'summarize following text \n {text}',
    input_variables= ['text']  
)

report_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)
final_chain = RunnableSequence(report_chain,branch_chain)
result = final_chain.invoke({'topic':'future of AI'})
print(result)    
