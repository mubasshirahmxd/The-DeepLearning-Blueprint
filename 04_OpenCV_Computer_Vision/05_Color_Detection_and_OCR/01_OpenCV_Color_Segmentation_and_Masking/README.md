<h1 align="center">
 🎨 OpenCV Color Segmentation & Masking 
 </h1>

<h3 align="center">
A real-time computer vision project showcasing color-based segmentation, masking, and detection using OpenCV’s HSV color space.
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python">
  <img src="https://img.shields.io/badge/OpenCV-Color%20Segmentation-red?logo=opencv">
  <img src="https://img.shields.io/badge/NumPy-Array%20Processing-yellow?logo=numpy">
  <img src="https://img.shields.io/badge/Platform-VSCode%20%7C%20Colab-lightgrey">
  <img src="https://img.shields.io/badge/Status-Completed-success">
  <img src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## 🧠 Overview

The **OpenCV Color Segmentation & Masking** project demonstrates how to use the **HSV color model** to extract and isolate specific colors from a live webcam feed in real time.

This project is part of the **FSDS Deep Learning Practical Series**, designed to bridge computer vision fundamentals with real-world implementation.

You can toggle between **Red**, **Green**, **Blue**, and **All Except White** color masks — exploring how HSV color ranges enable precise color detection and filtering.

---

## 📂 Folder Structure

```bash
04_OpenCV_Computer_Vision/
└─ 05_Color_Detection_and_OCR/
   └─ 01_OpenCV_Color_Segmentation_and_Masking/
      ├─ raw_scripts/
      │  ├─ CV1_capture_videos.py
      │  ├─ CV2_red_color_mask.py
      │  ├─ CV3_blue_color_mask.py
      │  ├─ CV4_green_color_mask.py
      │  ├─ CV5_except_white_mask.py
      │  └─ test_HSV_color.py
      │
      ├─ color_segmentation.py
      ├─ opencv_color_segmentation_and_masking.ipynb
      └─ README.md
```

---

## 🧩 Key Features

| Feature                              | Description                                                           |
| ------------------------------------ | --------------------------------------------------------------------- |
| 🎥**Real-Time Webcam Feed**    | Detect and mask colors directly from your camera                      |
| 🌈**HSV Color Space**          | Robust color segmentation that separates hue, saturation & brightness |
| 🔴🟢🔵**Multiple Color Modes** | Red, Green, Blue, and “All Except White” masking                    |
| 💾**Save Masks**               | Press `S` to save the current frame or mask                         |
| ⚙️**Interactive Controls**   | Toggle between views using keyboard shortcuts                         |
| 🧠**Practical Learning**       | Perfect for understanding computer vision pipelines                   |

---

## ⚙️ Installation & Setup

### 1️⃣ Create Environment

```bash
conda create -n cv_env python=3.10 -y
conda activate cv_env
```

### 2️⃣ Install Dependencies

```bash
pip install opencv-python numpy
```

---

## 🚀 Run the Project

```bash
python color_segmentation.py
```

**🎮 Controls:**

| Key             | Action                  |
| --------------- | ----------------------- |
| `r`           | Red mask                |
| `g`           | Green mask              |
| `b`           | Blue mask               |
| `a`           | All colors except white |
| `o`           | Original view           |
| `h`           | HSV view                |
| `s`           | Save current mask/frame |
| `ESC` / `q` | Quit                    |

---

## 🧠 Concept — Why HSV?

Unlike RGB, the **HSV color model** separates color information (Hue) from intensity (Value).
This makes it ideal for **robust color-based segmentation** under varying lighting conditions.

| Channel                  | Range  | Purpose            |
| ------------------------ | ------ | ------------------ |
| **Hue (H)**        | 0–180 | Defines color type |
| **Saturation (S)** | 0–255 | Color intensity    |
| **Value (V)**      | 0–255 | Brightness level   |

---

## 🧾 System Requirements

| Component             | Minimum Requirement                  |
| --------------------- | ------------------------------------ |
| 💻**OS**        | Windows / macOS / Linux              |
| 🐍**Python**    | 3.9+                                 |
| 🎥**Camera**    | Built-in or external webcam          |
| ⚡**RAM**       | 4 GB+                                |
| 🧩**Libraries** | OpenCV, NumPy                        |
| 🧠**IDE**       | VSCode (preferred) / Jupyter / Colab |

---

## 📸 Demo Previews

💥 No screenshots here. Go run it yourself and see the magic happen! 😏
(Yeah, that’s right — real developers test their own code 😎)

---

## 🧩 Learnings & Takeaways

- How to work with **HSV color space** in OpenCV
- How to create **binary masks** for color segmentation
- How to integrate **real-time webcam processing**
- How to use **keyboard controls** for interaction
- How to preprocess for advanced models like OCR or object detection

---

## 🧑‍💻 Developer & Credits

**Developed by:** [Mubasshir Ahmed](https://github.com/mubasshirahmed-3712)
**Libraries Used:** OpenCV • NumPy
**License:** MIT License

---

## 🌟 Closing Note

This project is part of the **FSDS Computer Vision Track**, combining **theory, implementation, and interactivity** into a single, recruiter-ready package.

> _“Colors are not just visuals — they’re signals. Learn to decode them.”_ 🎨

---

<h3 align="center">✨ Keep coding, keep creating, and keep seeing the world in pixels. ✨</h3>
