from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

model= GoogleGenerativeAI(model='gemini-3.5-flash-lite')

result=model.invoke("WHo is the cm of telangana")

print(result)