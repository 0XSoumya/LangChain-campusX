from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence , RunnablePassthrough , RunnableParallel , RunnableLambda

load_dotenv()

prompt = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables=['topic']
)

def Word_count(text):
    return len(text.split())

model = ChatMistralAI(model = 'mistral-small')
parser = StrOutputParser()

joke_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'count': RunnableLambda(Word_count)
})

final_chain = RunnableSequence(joke_chain, parallel_chain)

result = final_chain.invoke({'topic':'math'})

final_result = """{} \n word count - {}""".format(result['joke'], result['count'])

print(final_result)