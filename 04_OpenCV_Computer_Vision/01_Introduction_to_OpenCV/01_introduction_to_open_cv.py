# ============================================
# 📘 01_Introduction_to_OpenCV.ipynb
# ============================================

# This notebook introduces OpenCV — its purpose, history, features, and key syntax.
# It contains theory and function references, not practical executions.

"""
<h2 style="text-align:center;">📘 Introduction to OpenCV</h2>

---

<h3>🧠 What is Computer Vision (CV)?</h3>

Computer Vision (CV) is a field of Artificial Intelligence that allows machines to interpret and understand visual information from the world — such as images, videos, and live camera feeds.  

In simple terms, **Computer Vision enables computers to 'see' like humans**.

Real-world applications:
- Face and object recognition (e.g., Face ID, surveillance)
- Medical imaging (X-ray, MRI analysis)
- Self-driving cars (lane, object, and pedestrian detection)
- Quality inspection in manufacturing
- Augmented reality and gesture tracking

---

<h3>📷 What is OpenCV?</h3>

**OpenCV (Open Source Computer Vision Library)** is an open-source library developed to provide a unified infrastructure for computer vision and machine learning tasks.

✅ Created by **Intel** in 2000.  
✅ Written in **C++**, but has **Python bindings** (cv2 module).  
✅ Highly optimized for **real-time image and video processing**.

---

<h3>⚙️ Why use OpenCV?</h3>

OpenCV simplifies complex computer vision tasks:
- Image and video reading/writing
- Image transformations and filtering
- Edge and contour detection
- Object detection using pre-trained models
- Integration with Deep Learning (TensorFlow, PyTorch, etc.)

---

<h3>🧮 How OpenCV Represents Images</h3>

When you read an image using OpenCV:
```python
img = cv2.imread('image.jpg')
```
- It is stored as a **NumPy array**.
- Each image is composed of **pixels**.
- Each pixel has **3 color channels** (B, G, R) for color images or **1 channel** for grayscale.

📘 Example representation:
```
img.shape → (height, width, channels)
```
If `img.shape = (720, 1080, 3)`, it means:
- 720 pixels height
- 1080 pixels width
- 3 color channels (B, G, R)

---

<h3>💾 Installing OpenCV</h3>

To install OpenCV in your environment:
```bash
pip install opencv-python
```
(Optional GUI features require `opencv-python-headless` in servers or Colab.)

---

<h3>📦 Importing and Checking Version</h3>

```python
import cv2
print(cv2.__version__)
```

Example output:
```
# ➤ 4.10.0
```

---

<h3>📚 Common OpenCV Functions (Syntax Only)</h3>

| Function | Description |
|-----------|--------------|
| `cv2.imread(path)` | Reads an image from a file path |
| `cv2.imshow(window_name, image)` | Displays an image in a popup window |
| `cv2.waitKey(delay)` | Waits for key press (0 = infinite) |
| `cv2.destroyAllWindows()` | Closes all OpenCV windows |
| `cv2.imwrite(filename, image)` | Writes image to disk |
| `cv2.cvtColor(image, code)` | Converts image color space (e.g., BGR↔RGB↔GRAY) |
| `cv2.resize(image, size)` | Resizes an image |
| `cv2.flip(image, flipCode)` | Flips an image horizontally/vertically |

---

<h3>🎨 Understanding BGR vs RGB</h3>

OpenCV uses **BGR** (Blue, Green, Red) instead of the standard **RGB** (Red, Green, Blue) format.

This means that when displaying images using Matplotlib, colors may appear distorted unless converted:

```python
# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

---

<h3>🧠 Where OpenCV Fits in the AI Workflow</h3>

OpenCV acts as the **preprocessing and real-time engine** for computer vision workflows:

1. **Capture/Load**: Read images or videos
2. **Process**: Resize, filter, detect objects/faces
3. **Feed**: Send data to ML/DL models (like CNNs)
4. **Visualize**: Display or draw detection results

---

<h3>📝 Summary</h3>

✅ OpenCV is an open-source CV library for image and video analysis.  
✅ It reads images as NumPy arrays in **BGR format**.  
✅ Core I/O functions: `imread`, `imshow`, `waitKey`, `destroyAllWindows`, `imwrite`.  
✅ BGR↔RGB conversion is crucial for correct color visualization.  
✅ Acts as the bridge between raw visual data and deep learning models.

---

<h4 style="text-align:center;">Next → 02_Image_Read_Write_Display.ipynb : Practical Image I/O with OpenCV</h4>
"""