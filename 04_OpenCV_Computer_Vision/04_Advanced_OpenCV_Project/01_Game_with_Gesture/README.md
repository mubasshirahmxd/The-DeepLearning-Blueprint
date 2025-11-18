# 🎮 Game with Gesture

### 🧠 Overview

This project demonstrates how to control simple actions using **hand gestures** captured via webcam. Using **MediaPipe Hands** and **OpenCV**, you can simulate directional key presses (Left, Right, Up, Down) based on your index finger’s movement.

Perfect for building gesture-based games or interactive media controls.

---

## ⚙️ How It Works

- Detects hand landmarks using `mp.solutions.hands`
- Tracks the **index finger tip** position
- Calculates movement direction (swipe up/down/left/right)
- Sends simulated keyboard key events using `pyautogui`

---

## 📂 Folder Structure

```
01_Game_with_Gesture/
├─ handgame.py
└─ Gesture_Game_OpenCV.ipynb
```

---

## 🧩 Setup Instructions

```bash
pip install opencv-python mediapipe pyautogui numpy
python handgame.py
```

---

## 🎮 Controls

| Gesture     | Action              |
| ----------- | ------------------- |
| Swipe Left  | Presses Left Arrow  |
| Swipe Right | Presses Right Arrow |
| Swipe Up    | Presses Up Arrow    |
| Swipe Down  | Presses Down Arrow  |
| ESC         | Quit                |

---

## 📸 Demo Preview

💥 No screenshots here — go run it and feel like Iron Man 😎

---

**Developed by:** [Mubasshir Ahmed](https://github.com/mubasshirahmed-3712)
**Libraries Used:** OpenCV • MediaPipe • PyAutoGUI
**License:** MIT
