<h1 align="center">🤖 BERT-Powered Intelligent Chatbot</h1>

<h3 align="center">Context-Aware NLP Chatbot using BERT + Streamlit</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Transformers-BERT-yellow?logo=huggingface" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-ff4b4b?logo=streamlit" />
  <img src="https://img.shields.io/badge/Model-Contextual%20Embeddings-brightgreen" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

---

## 📌 Overview

This project is a **BERT-powered chatbot** capable of understanding user queries and responding based on **semantic similarity**, not just keywords.

Unlike a rule-based chatbot, this model:

- Uses **BERT embeddings** (Bidirectional Transformers)
- Compares user input with **pre-defined questions** via cosine similarity
- Automatically selects the most contextually relevant response
- Runs on a clean, modern **Streamlit UI**
- Includes a **custom UI background** for a premium look

This chatbot is simple but demonstrates the **core power of BERT for real NLP applications**.

---

## 🧠 How It Works

### 1. **BERT Embeddings**

Each question and user message is converted into a BERT vector using:

```python
outputs.last_hidden_state.mean(dim=1)
```

This gives a **semantic embedding** for the sentence.

---

### 2. **Cosine Similarity Matching**

We compare:

```
user_embedding  ↔  predefined_question_embedding
```

Whichever question has the **highest similarity score** determines the chatbot’s response.

---

### 3. **Streamlit Frontend**

A lightweight UI that:

✔ Loads the background image
✔ Accepts user input
✔ Shows intelligent, BERT-powered responses

---

## 📂 Project Structure

```
02_BERT_Chatbot/
├── assets/
│   └── Chatbot_bg.jpg         # Background image
├── Chatbot_app.py             # Main Streamlit chatbot script
└── UI_Overview.png            # Screenshot preview
```

---

## 🚀 Run the Chatbot

### 1️⃣ Install Dependencies

```bash
pip install streamlit transformers torch scikit-learn
```

### 2️⃣ Start the Streamlit App

```bash
streamlit run Chatbot_app.py
```

Then open:

```
http://localhost:8501/
```

---

## 🎨 UI Preview

<p align="center">
  <img src="UI_Overview.png" alt="Chatbot UI Overview" width="750">
</p>


---

## 💬 Supported Questions

The chatbot understands queries similar to:

- What is your name?
- What is BERT?
- Tell me a joke
- What is AI?
- What is Data Science?
- What is Microsoft Azure?

These responses come from predefined Q/A pairs matched using BERT embeddings.

---

## 🔧 Technologies Used

| Component                   | Description                |
| --------------------------- | -------------------------- |
| **BERT Base Uncased** | Text embeddings            |
| **Transformers**      | Tokenizer + Model          |
| **PyTorch**           | Backend tensor computation |
| **Streamlit**         | Interactive UI             |
| **Cosine Similarity** | Semantic matching          |

---

## 🧠 Why This Project Is Useful

- Clear demonstration of **BERT’s contextual embeddings**
- Real example of **semantic search**
- Fast and lightweight—no fine-tuning required
- Great portfolio project for **NLP engineers & students**
- Easy to extend into full LLM/RAG chatbot

---

## 🔮 Future Enhancements

- Add GPT-based fallback when similarity is low
- Add conversational memory
- Add voice input using SpeechRecognition
- Deploy on Streamlit Cloud
- Add large dataset support (FAQ chatbot)

---

## 👨‍💻 Developer

**Mubasshir Ahmed**
FSDS Deep Learning & NLP Applications

---

<h3 align="center">✨ Built with ❤️ using BERT & Streamlit ✨</h3>
