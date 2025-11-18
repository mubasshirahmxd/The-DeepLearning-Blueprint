<h1 align="center">🚀 BERT Sentiment Analysis Suite</h1>

<h3 align="center">
A complete end-to-end NLP system using <b>BERT + HuggingFace Transformers + FastAPI + Streamlit</b>.
<br>
Train → Serve API → Use Frontend — all in one powerful project.
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python">
  <img src="https://img.shields.io/badge/Transformers-HuggingFace-yellow?logo=huggingface">
  <img src="https://img.shields.io/badge/DeepLearning-BERT-green">
  <img src="https://img.shields.io/badge/API-FastAPI-success?logo=fastapi">
  <img src="https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen">
</p>

---

# 📌 **Project Overview**

This project is a **complete NLP pipeline** built using **BERT (Bidirectional Encoder Representations from Transformers)**.

It includes:

### 🔥 1️⃣ BERT Fine-Tuning

Fine-tune **bert-base-uncased** on the **IMDB movie review dataset** for binary sentiment classification (Positive/Negative).

### ⚡ 2️⃣ FastAPI Backend

After training, the model is served using a scalable REST API:

- `/predict` → Send text → Receive sentiment label.

### 🎨 3️⃣ Streamlit Frontend

A clean UI where users can:

- Type any text
- Send it to FastAPI
- See real-time predictions

### 🧱 4️⃣ Combined Full-Stack Deployment

Both FastAPI + Streamlit run together in one script (multithreaded).

---

# 🧩 **Key Features**

| Feature                         | Description                                    |
| ------------------------------- | ---------------------------------------------- |
| **BERT Fine-Tuning**      | Train with HuggingFace Trainer on IMDB dataset |
| **REST API**              | FastAPI endpoint for real-time prediction      |
| **Streamlit UI**          | Modern, interactive frontend                   |
| **Softmax Probabilities** | Converts logits → class probabilities         |
| **GPU Support**           | Automatically uses CUDA if available           |
| **Production-Ready**      | Save + reload trained model for deployment     |

---

# 📂 **Project Structure**

```

```

BERT_Sentiment_Analysis/
│── app.py # Runs FastAPI + Streamlit
│── bert_train.ipynb / .py # Notebook/script for model training
│── bert_imdb_model/ # Saved model + tokenizer
│── requirements.txt
│── README.md

```

```

---

# ⚙️ **Installation**

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/bert-sentiment-analysis.git
cd bert-sentiment-analysis
```

### 2️⃣ Create & activate environment

```
conda create -n bert_env python=3.10 -y
conda activate bert_env

```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt

```

# 🧠 Training the Model

Run the training script / notebook:

<pre class="overflow-visible!" data-start="3024" data-end="3056"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python bert_train.py
</span></span></code></div></div></pre>

This will:

✔ Load IMDB dataset

✔ Tokenize text

✔ Train BERT

✔ Save model to `bert_imdb_model/`



# 🚀 Running the FastAPI Backend Only

<pre class="overflow-visible!" data-start="3207" data-end="3243"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>uvicorn app:app --reload
</span></span></code></div></div></pre>

### Test API (Postman / browser)

**POST → `/predict/`**

Body:

<pre class="overflow-visible!" data-start="3310" data-end="3361"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"text"</span><span>:</span><span></span><span>"This movie was amazing!"</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

Response:

<pre class="overflow-visible!" data-start="3374" data-end="3407"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"prediction"</span><span>:</span><span></span><span>1</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>


# 🎨 Running the Streamlit UI Only

<pre class="overflow-visible!" data-start="3450" data-end="3482"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>streamlit run app.py
</span></span></code></div></div></pre>

This opens a UI where users can:

<pre class="overflow-visible!" data-start="3518" data-end="3569"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Enter text → click Analyze → see prediction</span></span></code></div></div></pre>


# 🔥 Run BOTH FastAPI + Streamlit Together (Full System)

Simply run:

<pre class="overflow-visible!" data-start="3647" data-end="3672"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python app.py
</span></span></code></div></div></pre>

This launches:

* **FastAPI backend in thread 1**
* **Streamlit frontend in main thread**

> You get a complete full-stack ML system inside one script.




# 📡 API Documentation

### Endpoint:

<pre class="overflow-visible!" data-start="3869" data-end="3891"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>POST /predict/
</span></span></code></div></div></pre>

### Request:

<pre class="overflow-visible!" data-start="3906" data-end="3953"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"text"</span><span>:</span><span></span><span>"I hate this product"</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

### Response:

<pre class="overflow-visible!" data-start="3969" data-end="4002"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span>{</span><span>
  </span><span>"prediction"</span><span>:</span><span></span><span>0</span><span>
</span><span>}</span><span>
</span></span></code></div></div></pre>

Where:

* `1` → Positive sentiment
* `0` → Negative sentiment


# 🧪 Model Prediction Example

Input:

<pre class="overflow-visible!" data-start="4113" data-end="4139"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>I love </span><span>this</span><span> movie!
</span></span></code></div></div></pre>

Output:

<pre class="overflow-visible!" data-start="4149" data-end="4165"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Positive</span><span>
</span></span></code></div></div></pre>

Input:

<pre class="overflow-visible!" data-start="4174" data-end="4212"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>This</span><span> was the worst movie ever.
</span></span></code></div></div></pre>

Output:

<pre class="overflow-visible!" data-start="4222" data-end="4238"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Negative</span></span></code></div></div></pre>



# ✨ Future Enhancements

* Deploy FastAPI → AWS/GCP/Azure
* Deploy Streamlit → Streamlit Cloud
* Add multilingual sentiment
* Add confidence scores
* Add BERT-large or DistilBERT support

---

# 👨‍💻 Developer

**Mubasshir Ahmed**

Deep Learning • NLP • Computer Vision

🔗 GitHub: [https://github.com/mubasshirahmed-3712](https://github.com/mubasshirahmed-3712)

---

# ⭐ Final Note

> *“Transformers are powerful — but pairing them with solid engineering makes them unstoppable.”*
