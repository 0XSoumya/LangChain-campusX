from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage , AIMessage
# a basic code demo of messages in langchain
load_dotenv()

model = ChatMistralAI(model='mistral-small')

messages=[
    SystemMessage(content = 'you are a witty assistant that replies to queries in a witty and sarcastic tone'),
    HumanMessage(content = 'tell me about the pyramids')
]
response=model.invoke(messages)
print(response.content)