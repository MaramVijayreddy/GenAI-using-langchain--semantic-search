from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import streamlit as st
from promptgenerator import template
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()


llm= HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation")

model=ChatHuggingFace(llm=llm)

st.header("Research Tool ")

paper_input=st.selectbox("Select Research Paper Name From Below",[ "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Deep Residual Learning for Image Recognition"])
style_input=st.selectbox("Select the Explanation mode",[
        "Beginner-friendly",
        "Technical",
        "Mathematical",
        "Code-oriented"])
length_input=st.selectbox("Select Explanation lenghth",["Short",
        "Medium",
        "Long"])

if st.button("Summarize"):
    chain=template | model
    result=chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input':length_input})
    st.write(result.content)
        