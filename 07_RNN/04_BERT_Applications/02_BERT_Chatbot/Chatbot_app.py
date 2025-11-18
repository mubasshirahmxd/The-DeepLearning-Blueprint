import streamlit as st
from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import base64
import time

# -------------------------------------------------------
# 1. BACKGROUND IMAGE
# -------------------------------------------------------
def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("assets/Chatbot_bg.jpg")


# -------------------------------------------------------
# 2. LOAD BERT MODEL + TOKENIZER
# -------------------------------------------------------
@st.cache_resource
def load_bert():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertModel.from_pretrained("bert-base-uncased")
    return tokenizer, model

tokenizer, model = load_bert()


# -------------------------------------------------------
# 3. KNOWLEDGE BASE (Static Q&A)
# -------------------------------------------------------
qa_pairs = {
    "what is your name": "I am a BERT-powered chatbot 🤖!",
    "how are you": "I'm just code… but feeling great! 😄",
    "what is bert": "BERT is a Transformer-based NLP model by Google.",
    "tell me a joke": "Why do programmers hate nature? Too many bugs! 🐛😂",

    "what is data science": (
        "Data Science is the field of extracting insights from data "
        "using statistics, ML, and programming 📊."
    ),

    "what is ai": (
        "Artificial Intelligence enables machines to think, learn, "
        "and solve problems intelligently 🤖💡."
    ),

    "what is microsoft azure": (
        "Azure is Microsoft's cloud computing platform for virtual machines, "
        "AI services, databases, and more ☁️."
    ),
}


# -------------------------------------------------------
# 4. GET BERT EMBEDDING
# -------------------------------------------------------
def bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()


# Precompute embeddings
predefined_embeddings = {q: bert_embedding(q) for q in qa_pairs}


# -------------------------------------------------------
# 5. RESPONSE GENERATION
# -------------------------------------------------------
def get_response(user_input):
    user_embed = bert_embedding(user_input)

    similarities = {
        q: cosine_similarity(user_embed, predefined_embeddings[q])[0][0]
        for q in qa_pairs
    }

    best_match = max(similarities, key=similarities.get)
    score = similarities[best_match]

    if score > 0.55:  # Tuned threshold
        return qa_pairs[best_match]
    else:
        return "I'm not sure I understand that 🤔. Try rephrasing!"


# -------------------------------------------------------
# 6. STREAMLIT UI
# -------------------------------------------------------
st.markdown(
    """
    <style>
        .chat-bubble-user {
            background-color: PINK;
            padding: 10px 15px;
            border-radius: 12px;
            margin: 5px 0;
            width: fit-content;
            max-width: 80%;
        }

        .chat-bubble-bot {
            background-color: YELLOW;
            color: BLACK;
            padding: 10px 15px;
            border-radius: 12px;
            margin: 5px 0;
            width: fit-content;
            max-width: 80%;
        }

        .chat-container {
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 Advanced BERT Chatbot")
st.write("A smart semantic chatbot powered by **BERT embeddings** + **Streamlit UI**.")

# Sidebar
st.sidebar.title("ℹ️ About")
st.sidebar.info(
    """
    **This chatbot understands queries using BERT embeddings**  
    and matches the closest predefined knowledge-base answer.

    **Technology Used:**
    - BERT Base Uncased  
    - Cosine Similarity  
    - Streamlit  
    """
)

st.sidebar.markdown("---")
st.sidebar.subheader("💡 Suggestions")
st.sidebar.write("• What is BERT?")  
st.sidebar.write("• Tell me a joke")  
st.sidebar.write("• What is Data Science?")  
st.sidebar.write("• What is Microsoft Azure?")  

# Session State for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.text_input("Ask something:", "")

# When user sends message
if st.button("Send"):
    if user_input.strip() != "":
        
        # Add user bubble
        st.session_state.chat_history.append(("user", user_input))

        # Bot is thinking...
        with st.spinner("Thinking..."):
            time.sleep(0.4)
            bot_response = get_response(user_input)

        # Add bot bubble
        st.session_state.chat_history.append(("bot", bot_response))


# Display messages
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f'<div class="chat-bubble-user"><b>You:</b> {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble-bot"><b>Bot:</b> {message}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
