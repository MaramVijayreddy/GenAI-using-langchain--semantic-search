from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-3.8-flash",thinking_level="low")
result=model.invoke(input())

print(result.content[0]['text'])