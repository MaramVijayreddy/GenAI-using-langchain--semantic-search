from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation")

model=ChatHuggingFace(llm=llm)
load_dotenv()

messages=[
    SystemMessage(content="you are a helpful ai agaent"),
    HumanMessage(content="tell me about your self")
    
]
result=model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)
