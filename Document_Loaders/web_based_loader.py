#useful to load content from static websites
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader, WebBaseLoader
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

# creating prompt:
prompt = PromptTemplate(
    template = 'answer the question {question} based on following text: {text}',
    input_variables=['question','text']
)

model = ChatMistralAI(model = 'mistral-small')
parser = StrOutputParser()

url = 'https://www.amazon.in/dp/B0DSKQ1JBN/ref=sspa_dk_detail_5?s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw'
loader  = WebBaseLoader(url)
docs = loader.load()

chain = prompt | model | parser # creating a simple chain

result = chain.invoke({'question': ' what price is this phone', 'text': 'docs'})

print(result)

