from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from colorama import init, Fore, Style
from pyfiglet import Figlet


load_dotenv()

init(autoreset=True)  # For colored text on Windows/Linux

model = ChatMistralAI(model = 'mistral-small')

# following code is only for aesthetics
print(Fore.YELLOW + "-----------------------------------------------\n")
figlet = Figlet(font='slant')  # you can change font styles if you want
ascii_header = figlet.renderText('Mistral Chat')
print(Fore.CYAN + Style.BRIGHT + ascii_header)
print(Fore.CYAN + "💬 Welcome to Mistral Chat! (type 'exit' to leave) 💬")
print(Fore.YELLOW + "-----------------------------------------------\n")

chat_history=[
    SystemMessage(content='you are a helpful assistant who gives concise answers to the queries')

]


while True:
    query = input(Fore.GREEN + '👤You :' + Style.RESET_ALL)
    chat_history.append(HumanMessage(content= query))
    if query.lower() == 'exit' :
        print(Fore.RED + "\n 🤖 Mistral :Goodbye! 👋")
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(Fore.BLUE + Style.BRIGHT + '🤖 Mistral: ' + Style.RESET_ALL + response.content)