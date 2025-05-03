# 📊 Enterprise Chat Assistant with RAG + Groq + Multi-PDF Support

This project is an advanced enterprise-ready Retrieval-Augmented Generation (RAG) chat assistant. It allows users to upload multiple PDF documents, ask questions about their content, and receive answers powered by Groq LLMs. The assistant maintains chat history and supports exporting Q&A sessions as CSV files.

---

## 🚀 Features

- **Multi-PDF Upload:** Upload and process multiple PDF documents at once.
- **RAG Pipeline:** Uses Retrieval-Augmented Generation for accurate, context-aware answers.
- **Groq LLM Integration:** Leverages Groq's high-performance language models.
- **Chat History:** Maintains a session-based chat history.
- **Export Q&A:** Download your chat history as a CSV file.
- **Streamlit UI:** User-friendly web interface.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Techofast-Official/Chatbot.git
   cd Chatbot
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # source venv/bin/activate   # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root with your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

---

## 🏃 Usage

1. **Start the Streamlit app:**
   ```bash
   streamlit run app_main.py
   ```

2. **Open your browser:**  
   Go to the local URL provided by Streamlit (usually http://localhost:8501).

3. **Upload PDFs:**  
   Use the sidebar to upload one or more PDF files.

4. **Ask Questions:**  
   Type your questions in the input box and get answers based on your documents.

5. **Download Chat History:**  
   Use the download button to export your Q&A as a CSV file.

---

## 📁 Project Structure

```
Chatbot/
│
├── app_main.py         # Streamlit app entry point
├── qa_chain.py         # RAG chain setup with Groq LLM
├── doc_ingest.py       # PDF ingestion and vector store creation
├── utils.py            # Utility functions (e.g., chat history export)
├── requirements.txt    # Python dependencies
└── .env                # Environment variables (not included in repo)
```

---

## 📝 Notes

- Make sure your Groq API key is valid and has sufficient quota.
- For best results, use clear and specific questions related to your uploaded documents.
- This project uses [LangChain](https://github.com/langchain-ai/langchain) for chaining and retrieval logic.

---

## 📜 License

This project is for educational and internal enterprise use. Please check individual package licenses for more details.

---

## 🤝 Contributions

Feel free to open issues or submit pull requests for improvements!
