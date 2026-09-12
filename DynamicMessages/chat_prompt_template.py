from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

from dotenv import load_dotenv

load_dotenv
chat_tempate=ChatPromptTemplate([
    ('system',"You are a helpful {domain} expert"),
    ('human',"EXplain in simple terms ,what is {topic}")
    ])

    
prompt=chat_tempate.invoke({'domain':'cricket','topic':'LBW'})
llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)


print(prompt)