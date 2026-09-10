from huggingface_hub import InferenceClient
from langchain_core.embeddings import Embeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HF_TOKEN")


class SimiliartyCheck(Embeddings):
    def __init__(self):
            self.client = InferenceClient(
                api_key=os.getenv("HF_TOKEN")
            )
            self.model = "sentence-transformers/all-MiniLM-L6-v2"
            
    def embed_documents(self, texts):
            return [
              self.client.feature_extraction(
                  text,model=self.model
              ).tolist() for text in texts]
    def embed_query(self, text):
    
            return self.client.feature_extraction(
                text,model=self.model).tolist()


embeddings=SimiliartyCheck()


documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]


query="tell me about Bumarah"


doc_embeddings=embeddings.embed_documents(documents)


query_embeddings = embeddings.embed_query(query)

scores=cosine_similarity([query_embeddings],doc_embeddings)[0]

index,scores=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]


print("QUery:", query)
print("Most similar text:",documents[index])
print("similarity score:",scores)