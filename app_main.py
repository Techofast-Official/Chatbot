# app_main.py

import os
import streamlit as st
from qa_chain import get_qa_chain
from doc_ingest import ingest_documents
from utils import save_chat_to_csv
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Advanced Enterprise RAG Assistant", layout="wide")
st.title("📊Chat Assistant with RAG + Chat History + Multi-PDF Support")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar: Upload multiple PDFs
st.sidebar.header("📁 Upload Documents")
uploaded_files = st.sidebar.file_uploader(
    "Upload one or more PDFs", type="pdf", accept_multiple_files=True
)

# Process documents once and cache retriever
if uploaded_files and "retriever" not in st.session_state:
    with st.spinner("📚 Processing documents..."):
        st.session_state.retriever = ingest_documents(uploaded_files)  # Uses HuggingFaceEmbeddings
        st.session_state.qa_chain = get_qa_chain(st.session_state.retriever)

# Main interaction
question = st.text_input("💬 Ask something from your documents")

if question and "qa_chain" in st.session_state:
    with st.spinner("🔍 Generating answer..."):
        answer = st.session_state.qa_chain.run(question)
        st.session_state.chat_history.append({"question": question, "answer": answer})
        st.success(answer)

# Display chat history
if st.session_state.chat_history:
    st.subheader("🕓 Chat History")
    for item in st.session_state.chat_history[::-1]:
        st.markdown(f"**Q:** {item['question']}")
        st.markdown(f"**A:** {item['answer']}")

    # Download chat history
    st.download_button(
        "⬇️ Download Q&A CSV",
        save_chat_to_csv(st.session_state.chat_history),
        "chat_history.csv"
    )
elif not uploaded_files:
    st.info("Upload PDF files from the sidebar to begin.")
