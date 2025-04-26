from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(model = 'mistral-small')


while True:
    query = input('You :')
    
    if query == 'exit' :
        break
    response = model.invoke(query)
    print('Mistral :', response.content)
