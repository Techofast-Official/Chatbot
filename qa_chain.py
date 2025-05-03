from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq  

def get_qa_chain(retriever):
    llm = ChatGroq(model="llama3-8b-8192", temperature=0)  # You can also use mixtral-8x7b-32768
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")
    return chain
