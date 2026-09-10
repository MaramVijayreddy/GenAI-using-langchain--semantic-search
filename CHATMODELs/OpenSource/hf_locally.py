#to run these model locally you need a machine with space and advanced version machines
# as i dont have space in my madchine and dont want to download anything in further iam not running it or excecuting it 
#but these is the actual code to run the model locally without using an api




from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()
import os
os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm=HuggingFacePipeline.from_model_id(
    model_id='openai/gpt-oss-20b',
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100)

)
result=model=ChatHuggingFace(llm=llm)
model.invoke("who is the pm of austrial")
print(result.content)