# basically introduction of if-else into chains

from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

class Feedback(BaseModel) :
    Sentiment: Literal['Positive', 'Negative'] = Field(description="return sentiment from the feedback")
    
model = ChatMistralAI(model = 'mistral-small')
parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

Prompt_1 = PromptTemplate(
    template = "classify sentiment in following text into negative or positive  \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction' :parser2.get_format_instructions()}
)

Prompt2 = PromptTemplate(
    template = "write an appropriate response for this positive feedback \n {feedback}",
    input_variables= ['feedback']
)

Prompt3 = PromptTemplate(
    template = "write an appropriate response for this negative feedback \n {feedback}",
    input_variables= ['feedback']
)

classifier_chain = Prompt_1 | model | parser2
branch_chain  = RunnableBranch(
    (lambda x:x.Sentiment == 'Posotive', Prompt2 | model | parser),
    (lambda x:x.Sentiment == 'Negative', Prompt3 | model | parser), 
    RunnableLambda (lambda x: "could not detect sentiment")
    )

chain = classifier_chain | branch_chain
result = chain.invoke({'feedback':'the camera should be better for the price, waste of money'})
print(result)