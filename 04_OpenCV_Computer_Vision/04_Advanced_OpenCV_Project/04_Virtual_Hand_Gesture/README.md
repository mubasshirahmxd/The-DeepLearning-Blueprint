# 🖌️ Virtual Hand Gesture — Air Brush Painter

### 🎨 Overview

A full-featured **gesture-based air painting app** built with **MediaPipe** and **OpenCV**.
Control your brush, change colors, erase, and save your artwork — all with hand movements.

---

## ⚙️ How It Works

- Tracks hand landmarks using `MediaPipe Hands`
- Detects finger positions and gestures
- Draws lines or clears the canvas using real-time logic
- Toolbar allows selecting colors or erasing

---

## 📂 Folder Structure

```
04_Virtual_Hand_Gesture/
├─ gesture_distance_draw.py
├─ gesture_painter_basic.py
├─ air_brush_virtual_painter.py
└─ Virtual_Hand_Gesture.ipynb
```

---

## 🧩 Setup Instructions

```bash
pip install opencv-python mediapipe numpy
python air_brush_virtual_painter.py
```

---

## 🎮 Controls & Gestures

| Gesture / Key    | Action                 |
| ---------------- | ---------------------- |
| ✌️ Two Fingers | Select color (toolbar) |
| ☝️ One Finger  | Draw                   |
| ✋ All Fingers   | Clear canvas           |
| 🎨 Black Color   | Eraser mode            |
| 💾 S Key         | Save artwork           |
| 🚪 ESC / Q       | Quit                   |

---

## 📸 Demo Preview

💥 No screenshots here — try it yourself and paint in the air like Tony Stark 😎

---

**Developer:** [Mubasshir Ahmed](https://github.com/mubasshirahmed-3712)
**License:** MIT
