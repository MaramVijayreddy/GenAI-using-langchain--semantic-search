from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_core.embeddings import Embeddings
import os

load_dotenv()


class HuggingFaceAPIembeddings(Embeddings):

    def __init__(self):
        self.client = InferenceClient(
            api_key=os.getenv("HF_TOKEN")
        )
        self.model = "sentence-transformers/all-MiniLM-L6-v2"

    def embed_documents(self, texts):
        return [
            self.client.feature_extraction(
                text,
                model=self.model
            ).tolist()
            for text in texts
        ]

    def embed_query(self, text):
        return self.client.feature_extraction(
            text,
            model=self.model
        ).tolist()


embeddings = HuggingFaceAPIembeddings()

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
text="Virat Kholi is the most famous cricketer"
vectors = embeddings.embed_documents(documents)

vector2=embeddings.embed_query(text)
#print(vector2)
print(str(vectors))