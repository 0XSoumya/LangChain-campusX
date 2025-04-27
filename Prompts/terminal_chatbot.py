from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatMistralAI(model = 'mistral-small')

chat_history=[
    SystemMessage(comtent='you are a helpful assistant who gives concise answers to the queries'),

]

while True:
    query = input('You :')
    chat_history.append(HumanMessage(content= 'query'))
    if query == 'exit' :
        break
    response = model.invoke(chat_history)
    chat_history.append(response.content)
    print('Mistral :', response.content)
print(chat_history)