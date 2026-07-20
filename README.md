# 🤖 Multimodal AI Chatbot

An intelligent AI-powered chatbot built with **Streamlit** and **Google Gemini 2.5 Flash** that supports conversational AI, image understanding, PDF question answering (RAG), web search, and built-in utility tools.

---

## ✨ Features

- 💬 AI Chat using Google Gemini 2.5 Flash
- 📄 Chat with PDF documents (RAG)
- 🖼️ Image Analysis using Gemini Vision
- 🌐 Web Search Integration
- 🧮 Built-in Calculator
- 📅 Date & Time Utility
- 🎨 Modern Dark/Light Theme
- 📱 Responsive Streamlit Interface
- ⚡ Fast and Interactive UI

---

## 🏗️ Project Structure

```text
multimodal-chatbot/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── assets/
│   ├── dark.css
│   └── light.css
│
├── services/
│   ├── calculator_service.py
│   ├── chat_service.py
│   ├── gemini_service.py
│   ├── image_service.py
│   ├── pdf_service.py
│   ├── rag_service.py
│   ├── search_service.py
│   └── tool_service.py
│
├── utils/
│   ├── theme.py
│   └── ui.py
│
└── README.md
```

---

## 🚀 Technologies Used

- Python 3
- Streamlit
- Google Gemini 2.5 Flash API
- Pillow
- PyMuPDF
- Sentence Transformers
- FAISS
- NumPy
- HTML
- CSS

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/umrao001/multimodal-chatbot.git
```

Move into the project directory

```bash
cd multimodal-chatbot
```

Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your own Google AI Studio API key.

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 💡 How to Use

### AI Chat

Ask any question and receive responses powered by Gemini.

### Image Analysis

1. Upload an image.
2. Ask questions about the image.
3. Gemini Vision analyzes the content.

### Chat with PDFs

1. Upload a PDF.
2. The document is indexed using FAISS.
3. Ask questions based on the uploaded document.

### Calculator

Examples:

```
25 * 48
sqrt(144)
125 / 5
```

### Date & Time

Examples:

```
What is today's date?
Current time
```

---

## 📸 Screenshots

Add screenshots here after deployment.

Example:

```
screenshots/home.png
screenshots/chat.png
screenshots/pdf.png
screenshots/image.png
```

---

## 🔮 Future Improvements

- Voice Assistant
- Speech-to-Text
- Text-to-Speech
- Chat History Database
- Authentication
- Multiple LLM Support
- Conversation Memory
- Document Summarization
- File Management
- Deployment on Streamlit Cloud

---

## 👨‍💻 Author

**Pranjal Umrao**

GitHub

https://github.com/umrao001

---


## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
