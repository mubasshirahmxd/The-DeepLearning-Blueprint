"""
app.py — Streamlit OCR Front-End
--------------------------------
Interactive OCR web app using OpenCV + Tesseract.

✅ Upload any image (JPG, PNG)
✅ Choose preprocessing mode (threshold, adaptive, smooth)
✅ Preview processed image
✅ Extract and display text
✅ Download result as .txt
✅ Works locally in VSCode / CMD

Run: streamlit run app/app.py
"""

import streamlit as st
import pytesseract
import cv2
import numpy as np
import shutil
from pathlib import Path
from io import BytesIO

# ---------------------------
# 🌙 Page Configuration
# ---------------------------
st.set_page_config(
    page_title="OpenCV OCR — Text Recognition",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown(
    "<h1 style='text-align:center;'>🧠 OpenCV + Tesseract OCR</h1>", unsafe_allow_html=True)
st.markdown(
    "<h4 style='text-align:center;'>Upload an image → Choose preprocessing → Extract text instantly.</h4>",
    unsafe_allow_html=True,
)
st.markdown("---")

# ---------------------------
# 🧩 Tesseract Path Handling
# ---------------------------
def find_tesseract():
    """Auto-detect tesseract path."""
    tess = shutil.which("tesseract")
    if tess:
        return tess
    common = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    ]
    for path in common:
        if Path(path).exists():
            return path
    return None

tess_path = find_tesseract()
if tess_path:
    pytesseract.pytesseract.tesseract_cmd = tess_path

with st.expander("⚙️ Tesseract Configuration"):
    st.info("If Tesseract OCR is not detected automatically, enter the full path to `tesseract.exe` below.")
    user_path = st.text_input("📂 Tesseract executable path:", value=tess_path or "")
    if user_path.strip():
        pytesseract.pytesseract.tesseract_cmd = user_path.strip()

# ---------------------------
# 📷 Upload Image
# ---------------------------
uploaded_file = st.file_uploader("📤 Upload an image (JPG, PNG)", type=["jpg", "jpeg", "png"])

# ---------------------------
# 🧠 Preprocessing Function
# ---------------------------
def preprocess_image(img, mode="thresh"):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if mode == "thresh":
        _, proc = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    elif mode == "adaptive":
        proc = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    elif mode == "smooth":
        proc = cv2.bilateralFilter(gray, 9, 75, 75)
    else:
        proc = gray
    return proc

# ---------------------------
# ⚙️ OCR Processing
# ---------------------------
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(image, channels="BGR", caption="🖼️ Uploaded Image", use_container_width=True)
    mode = st.selectbox(
        "🎛️ Choose preprocessing method:",
        ["thresh", "adaptive", "smooth"]
    )

    if st.button("🚀 Extract Text"):
        try:
            processed = preprocess_image(image, mode)
            text = pytesseract.image_to_string(processed, config="--psm 6")

            if text.strip():
                st.success("✅ Text successfully extracted!")
                st.text_area("📜 Recognized Text", text.strip(), height=200)
                st.image(processed, caption="🔧 Preprocessed Image", channels="GRAY", use_container_width=True)

                # Download text button
                text_bytes = text.encode('utf-8')
                st.download_button(
                    label="💾 Download Extracted Text",
                    data=text_bytes,
                    file_name="recognized_text.txt",
                    mime="text/plain"
                )
            else:
                st.warning("⚠️ No readable text detected. Try another preprocessing mode or higher quality image.")

        except Exception as e:
            st.error(f"❌ OCR Error: {e}")
else:
    st.info("👆 Upload an image above to begin OCR processing.")

# ---------------------------
# ℹ️ Footer
# ---------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Built with ❤️ using OpenCV, Tesseract, and Streamlit<br>FSDS Deep Learning Series — Mubasshir Ahmed</p>",
    unsafe_allow_html=True
)
