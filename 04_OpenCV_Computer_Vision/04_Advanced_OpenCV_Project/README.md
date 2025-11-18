<h1 align="center">🎯 Advanced OpenCV Projects — Gesture & Motion Suite</h1>

<h3 align="center">
A complete collection of OpenCV + MediaPipe interactive applications — from gesture-controlled games to real-time virtual painting.
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv">
  <img src="https://img.shields.io/badge/MediaPipe-Gesture%20AI-orange?logo=google">
  <img src="https://img.shields.io/badge/Platform-VSCode%20%7C%20Colab-lightgrey">
  <img src="https://img.shields.io/badge/Status-Completed-success">
  <img src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## 🧠 Overview

This **Advanced OpenCV Suite** is a curated set of **gesture-based and video-processing projects** developed as part of the **FSDS Deep Learning Practical Series (Kodigit)**.

It blends **MediaPipe hand-tracking**, **OpenCV frame operations**, and **real-time gesture control** to build interactive applications —
from 🎮 games and 🖱️ cursors to 🎨 air painting tools.

All scripts are **VSCode + Colab compatible**, built with clean, readable code and industry-level comments.

---

## 🗂️ Folder Structure

```bash
04_Advanced_OpenCV_Project/
├─ 01_Game_with_Gesture/
│  ├─ handgame.py
│  ├─ Gesture_Game_OpenCV.ipynb
│  └─ README.md
│
├─ 02_Hand_Cursor_with_CV/
│  ├─ hand_cursor_basic.py
│  ├─ hand_cursor_face_draw.py
│  ├─ Hand_Cursor_with_CV.ipynb
│  └─ README.md
│
├─ 03_Video_Frame/
│  ├─ video_frame_reader.py
│  ├─ Video_Frame_Exploration.ipynb
│  └─ README.md
│
└─ 04_Virtual_Hand_Gesture/
   ├─ gesture_distance_draw.py
   ├─ gesture_painter_basic.py
   ├─ air_brush_virtual_painter.py
   ├─ Virtual_Hand_Gesture.ipynb
   └─ README.md
```

---

## 🧩 Project Modules

<details>
<summary>🎮 <b>01 — Game with Gesture</b></summary>

**Concept:**
Control your computer with hand swipes using **MediaPipe Hands** + **PyAutoGUI**.
This project maps real-time hand movement into arrow key actions.

**Highlights:**

- Swipe left/right/up/down = keyboard events
- Real-time tracking using webcam
- Lightweight and CPU-friendly

**Run Command:**

```bash
python 01_Game_with_Gesture/handgame.py
```

📘 [Read More →](./01_Game_with_Gesture/README.md)

</details>

---

<details>
<summary>🖱️ <b>02 — Hand Cursor with CV</b></summary>

**Concept:**
Turn your hand into a **virtual mouse cursor** using **OpenCV + MediaPipe**.
Includes optional *face-aware drawing* mode for interactive fun!

**Highlights:**

- Move cursor using index finger
- Draw in “air” mode
- Works with any webcam

**Run Command:**

```bash
python 02_Hand_Cursor_with_CV/hand_cursor_basic.py
```

📘 [Read More →](./02_Hand_Cursor_with_CV/README.md)

</details>

---

<details>
<summary>🎥 <b>03 — Video Frame Exploration</b></summary>

**Concept:**
Understand video frame reading and FPS handling with **OpenCV VideoCapture**.
Perfect for learning how OpenCV handles continuous frame sequences.

**Highlights:**

- Manual & automatic frame control
- FPS counter and overlay display
- Teaches fundamentals of real-time vision loops

**Run Command:**

```bash
python 03_Video_Frame/video_frame_reader.py
```

📘 [Read More →](./03_Video_Frame/README.md)

</details>

---

<details>
<summary>🖌️ <b>04 — Virtual Hand Gesture (Air Painter)</b></summary>

**Concept:**
Paint and create digital art using only your hand gestures — no mouse needed!
A **MediaPipe-powered virtual air brush** with real-time color selection and eraser.

**Highlights:**

- Pinch-to-draw and clear gestures
- Toolbar with 4 colors + eraser
- Save artwork with one key press
- Perfect for interactive art installations

**Run Command:**

```bash
python 04_Virtual_Hand_Gesture/air_brush_virtual_painter.py
```

📘 [Read More →](./04_Virtual_Hand_Gesture/README.md)

</details>

---

## ⚙️ Installation & Setup

```bash
# Clone this repo
git clone https://github.com/mubasshirahmed-3712/FSDS-DeepLearning-Projects.git
cd 04_OpenCV_Computer_Vision/04_Advanced_OpenCV_Project/

# Create environment
conda create -n cv_env python=3.10 -y
conda activate cv_env

# Install dependencies
pip install opencv-python mediapipe numpy pyautogui
```

---

## 🧾 System Requirements

| Component             | Minimum Requirement                  |
| --------------------- | ------------------------------------ |
| 💻**OS**        | Windows / macOS / Linux              |
| 🐍**Python**    | 3.9+                                 |
| 🎥**Camera**    | Built-in or external webcam          |
| ⚡**RAM**       | 4 GB+                                |
| 🧠**Libraries** | OpenCV, MediaPipe, NumPy, PyAutoGUI  |
| 🧩**IDE**       | VSCode (preferred) / Jupyter / Colab |

---

## 🧠 Key Learnings

- Gesture → Action mapping using MediaPipe landmarks
- FPS optimization & video frame reading
- Interactive computer vision pipeline
- Overlay blending & color space management
- Real-world use of OpenCV for UI/UX systems

---

## 📸 Demo Previews

💥 No screenshots here — go run it yourself and experience the magic!

> (Because real devs don’t watch demos… they *make* them 😎)

---

## 🧑‍💻 Developer & Credits*👨‍💻 Developed by:**[Mubasshir Ahmed](https://github.com/mubasshirahmed-3712)

**🧰 Libraries Used:** OpenCV • MediaPipe • NumPy • PyAutoGUI
**📜 License:** MIT License

---

## 🌟 Closing Note

This repository is a part of the **FSDS Deep Learning Practical Series**, bridging the gap between **deep learning concepts** and **real-world vision applications**.

> _“Great engineers don’t just learn concepts — they build magic from pixels.”_

---

<h3 align="center">✨ Keep experimenting. Keep building. Keep learning. ✨</h3>
