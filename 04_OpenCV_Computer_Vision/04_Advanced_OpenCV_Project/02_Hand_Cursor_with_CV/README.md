# 🖱️ Hand Cursor with OpenCV

### 💡 Overview

Control your mouse pointer and draw using your hand gestures!
This project combines **OpenCV** and **MediaPipe** to detect hand landmarks and map your index finger to screen movements.

It includes:

- Cursor control
- Air drawing mode
- Face-aware mode for fun sketches

---

## ⚙️ How It Works

- Uses `MediaPipe Hands` to detect index finger coordinates
- Translates finger movement into cursor position
- Optional “draw mode” for sketching in air
- Integrated FPS and HUD display

---

## 📂 Folder Structure

```
02_Hand_Cursor_with_CV/
├─ hand_cursor_basic.py
├─ hand_cursor_face_draw.py
└─ Hand_Cursor_with_CV.ipynb
```

---

## 🧩 Setup Instructions

```bash
pip install opencv-python mediapipe pyautogui numpy
python hand_cursor_basic.py
```

---

## 🎮 Controls

| Mode | Action                         |
| ---- | ------------------------------ |
| Move | Move hand to control cursor    |
| Draw | Enable “draw mode” to sketch |
| Quit | ESC / Q                        |

---

## 📸 Demo Preview

🖐️ Draw, move, and paint with your hands — no mouse needed!

---

**Developer:** [Mubasshir Ahmed](https://github.com/mubasshirahmed-3712)
**License:** MIT
