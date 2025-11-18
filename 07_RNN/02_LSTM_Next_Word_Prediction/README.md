<h1 align="center">🔮 LSTM-Based Next Word Prediction</h1>

<h3 align="center">
A sequence modeling project using Tokenization, N-gram generation, Embedding layers, and stacked LSTMs.
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python">
  <img src="https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow">
  <img src="https://img.shields.io/badge/Keras-Deep%20Learning-red">
  <img src="https://img.shields.io/badge/Model-LSTM-blueviolet">
  <img src="https://img.shields.io/badge/Dataset-TMDB%205000%20Movies-green">
  <img src="https://img.shields.io/badge/Status-Completed-success">
</p>

---

## 🧠 Project Overview

This project demonstrates **Next Word Prediction using an LSTM-based Language Model**.
It uses the **TMDB 5000 Movies dataset**, specifically the **original_title** column, to learn how words follow each other within movie titles.

Even though movie titles are short, they serve as a light dataset for learning the fundamentals of:

- Tokenization
- Sequence generation
- Sequence padding
- Embedding representations
- LSTM sequence modelling
- Softmax-based next-word prediction

This entire workflow forms the fundamental building block for **chatbots, auto-complete systems, captioning models, NLP assistants**, and more.

---

## 📁 Folder Structure

```bash
02_LSTM_Next_Word_Prediction/
│
├── Next_Word_Prediction.ipynb     # Main notebook
├── tmdb_5000_movies.csv           # Dataset
├── nwp.h5                         # Trained LSTM model
└── README.md                      # Documentation

```

## 🎯 Objective

> **Predict the next word in a sentence using a trained LSTM model.**
>
> Input:   "lord of the"
> Output:  "rings"

## ⚙️ Workflow Summary

### **1. Load Dataset**

Movie titles extracted from TMDB dataset.

### **2. Tokenization**

Convert words → integer IDs using Keras Tokenizer.

### **3. Generate N-gram Sequences**

For `"the dark knight"` →

* X: `"the"`     → y: `"dark"`
* X: `"the dark"` → y: `"knight"`

### **4. Pad Sequences**

Make all sequences equal length.

### **5. One-Hot Encode Targets**

For softmax classification.

### **6. Model Architecture**

Embedding (vocab_size, 14)
LSTM (100 units, return_sequences=True)
LSTM (100 units)
Dense (100, ReLU)
Dense (vocab_size, Softmax)

### **7. Train (250 epochs)**

Loss = categorical_crossentropy

Optimizer = Adam

### **8. Prediction Function**

Predict next word → append to text → predict again.

📊 Model Architecture

Input → Tokenize → Pad → Embedding → LSTM → LSTM → Dense → Softmax → Next Word

### Why LSTM?

* Remembers previous context
* Avoids vanishing gradients using gates
* Handles sequential dependencies

## 🚀 Running the Project

### **1. Install Dependencies**

```
pip install tensorflow numpy pandas

```

### **2. Run the Notebook**

```
jupyter notebook Next_Word_Prediction.ipynb

```

### **3. Interact with the Model**

Open the notebook and run the cells to see the model in action.

---

## 📌 References

- [TMDB 5000 Movies Dataset](https://www.kaggle.com/rounakbanik/tmdb-movie-metadata)
- [Keras Tokenizer](https://keras.io/api/preprocessing/text/#tokenizer-class)
- [Keras Embedding Layer](https://keras.io/api/layers/core_layers/embedding/)

### 3. Load the Trained Model

```
   from tensorflow.keras.models import load_model
   model = load_model('nwp.h5')
```

### 4. Predict

```
   make_prediction("cloudy", 10)
```

### ✨ Example Predictions

> cloudy → cloudy with a chance of the night rises forever again
> mars → mars attacks the planet of earth returns again forever

*(Movie-title dataset creates fun, creative outputs!)*

<pre class="overflow-visible!" data-start="2190" data-end="2327"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"></div></div></pre>

## 📌 Key Learnings

* Sequence Modeling
* N-gram based training
* Word embeddings
* LSTM architecture
* Autoregressive text generation

---

## ⚠️ Limitations

* Dataset consists only of movie titles → limited context
* LSTMs struggle with long dependencies
* Predictions can be quirky

---

## 🚀 Future Improvements

* Use movie **overviews** (long text)
* Add  **GRU** ,  **Bidirectional LSTM** , or **Transformer**
* Use **beam search** instead of greedy search
* Add **Streamlit/Gradio UI**
* Replace one-hot with **SparseCategoricalCrossentropy** for faster training

---

## 👨‍💻 Author

**Mubasshir Ahmed**

FSDS Deep Learning Track

GitHub: [https://github.com/mubasshirahmed-3712](https://github.com/mubasshirahmed-3712)

---

<h3 align="center">✨ “Sequence models don’t just predict words — they predict meaning.” ✨</h3>
