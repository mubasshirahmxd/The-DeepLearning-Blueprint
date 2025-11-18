# 🚀 **Speech Recognition Assistant (Intermediate Level)**

### *Voice-activated assistant using Python, SpeechRecognition, pyttsx3, Wikipedia & YouTube Automation*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
  <img src="https://img.shields.io/badge/SpeechRecognition-Voice%20AI-yellow">
  <img src="https://img.shields.io/badge/TextToSpeech-pyttsx3-orange">
  <img src="https://img.shields.io/badge/Wikipedia-API-green?logo=wikipedia">
  <img src="https://img.shields.io/badge/Status-Completed-success">
</p>
---

## 🧠 **Overview**

This project is a fully functional **voice assistant** that listens for a *hotword* (“Alexa”), recognizes your speech, and performs actions such as:

* 🎵 Playing songs on YouTube
* 🔍 Searching Google
* 📖 Fetching Wikipedia summaries
* ⏰ Telling the current time
* 🌐 Opening websites (YouTube, Google, GitHub)
* 🗣 Speaking responses using TTS

The assistant uses Google’s Speech-to-Text engine and works in real-time via microphone.

---

## 📂 **Project Structure**

<pre class="overflow-visible!" data-start="3060" data-end="3456"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>03</span><span>_Speech_Recognition_Assistant/
│
├── app/
│   ├── speech_assistant.py      # Main assistant </span><span>loop</span><span>
│   ├── config.py                # Hotword + microphone settings
│   └── utils/
│       ├── listener.py          # Speech-</span><span>to</span><span>-</span><span>text</span><span> module
│       ├── speaker.py           # </span><span>Text</span><span>-</span><span>to</span><span>-speech module
│       └── commands.py          # </span><span>All</span><span> commands (play, </span><span>search</span><span>, </span><span>time</span><span>, wikipedia)
│
└── README.md
</span></span></code></div></div></pre>

---

## ⭐ **Features**

### 🔥 Hotword Activation

Assistant activates only when you say:

> **“Alexa ...”**

### 🔊 Text-to-Speech

Replies using **pyttsx3** (offline TTS).

### 🗣 Speech-to-Text

Real-time recognition using  **Google Speech API** .

### 🎵 YouTube Automation

Play any song directly:

> “Alexa play despacito”

### 📚 Wikipedia Summaries

Ask for any topic:

> “Alexa wikipedia machine learning”

### 🔍 Google Search

Opens search in browser:

> “Alexa search best pizza recipe”

### 🌐 Open Websites

> “Alexa open github”

---

## ⚙️ **Setup Instructions**

### 1️⃣ Create environment

<pre class="overflow-visible!" data-start="4062" data-end="4141"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>conda create -n speech_env python=3.10 -y
conda activate speech_env
</span></span></code></div></div></pre>

### 2️⃣ Install dependencies

<pre class="overflow-visible!" data-start="4172" data-end="4241"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install SpeechRecognition pyttsx3 pywhatkit wikipedia
</span></span></code></div></div></pre>

Optional (recommended):

<pre class="overflow-visible!" data-start="4267" data-end="4298"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install pyaudio
</span></span></code></div></div></pre>

### 3️⃣ Fix microphone permissions

Windows → *Microphone Privacy Settings* → Turn ON.

---

## ▶️ **Run the Assistant**

<pre class="overflow-visible!" data-start="4422" data-end="4464"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python app/speech_assistant.py
</span></span></code></div></div></pre>

---

## 🎤 **Usage Examples**

| Command                                       | What it does          |
| --------------------------------------------- | --------------------- |
| **Alexa play kesariya**                  | Plays song on YouTube |
| **Alexa search best laptop under 50000** | Google search         |
| **Alexa wikipedia virat kohli**          | Reads 2-line summary  |
| **Alexa what is the time**               | Tells current time    |
| **Alexa open youtube**                   | Opens YouTube         |

---

## 🛠 Configuration

Edit the hotword or mic index in:

`app/utils/config.py`

<pre class="overflow-visible!" data-start="4897" data-end="4944"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>HOTWORD = </span><span>"Alexa"</span><span>
MIC_INDEX = </span><span>None</span><span>
</span></span></code></div></div></pre>

To list all microphones:

<pre class="overflow-visible!" data-start="4972" data-end="5014"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>python -m speech_recognition
</span></span></code></div></div></pre>

---

## ⚠️ Notes & Limitations

* Requires internet for speech recognition & Wikipedia
* pywhatkit opens YouTube in browser → playback depends on system
* PyAudio may need manual installation on Windows
* Not a fully offline assistant (STT uses Google API)

---

## 🚀 Future Extensions

* Add offline wake word detection (Porcupine)
* Add offline STT (Vosk)
* Add GUI dashboard
* Add ChatGPT integration for conversational mode
* Add system-level commands (volume, brightness, open apps)

---

## 👨‍💻 Author

**Mubasshir Ahmed**

FSDS | Deep Learning & Applied AI

GitHub: *github.com/mubasshirahmed-3712*

---

<p align="center">
✨ “Your voice is now your command.” ✨  
</p>
