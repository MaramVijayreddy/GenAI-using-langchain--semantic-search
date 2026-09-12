from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv

llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation")

model=ChatHuggingFace(llm=llm)
load_dotenv()

chat_history=[
    SystemMessage(content="YOu are a Helpful ai assistant")]


while True:
    user_input=input('You:')
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input=='exit':
        break
    result=model.invoke(chat_history)#here we will be passinng the entire chat hitsory instead or user_input 
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)
print(chat_history)

