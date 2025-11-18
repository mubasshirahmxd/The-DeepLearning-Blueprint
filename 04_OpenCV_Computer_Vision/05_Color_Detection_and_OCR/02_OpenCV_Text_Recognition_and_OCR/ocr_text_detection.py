"""
ocr_text_detection.py
----------------------
A clean OCR backend script for extracting text from images using OpenCV + Tesseract.

✅ Works in VSCode / Command Line.
✅ Auto-detects Tesseract installation (Windows/macOS/Linux).
✅ Handles path issues and gives clear install guidance.
✅ Supports multiple preprocessing modes.
"""

import cv2
import numpy as np
import pytesseract
import argparse
import shutil
from pathlib import Path

def find_tesseract():
    """Auto-detect or find tesseract.exe"""
    tess = shutil.which("tesseract")
    if tess:
        return tess
    # Common Windows locations
    possible_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    ]
    for path in possible_paths:
        if Path(path).exists():
            return path
    return None

def preprocess_image(img, mode="thresh"):
    """Apply OpenCV preprocessing for OCR clarity."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if mode == "thresh":
        _, proc = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    elif mode == "adaptive":
        proc = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY,11,2)
    elif mode == "smooth":
        proc = cv2.bilateralFilter(gray, 9, 75, 75)
    else:
        proc = gray
    return proc

def extract_text(image_path, mode="thresh", lang="eng"):
    """Main OCR function: load image, preprocess, and extract text."""
    tess_path = find_tesseract()
    if not tess_path:
        raise EnvironmentError(
            "❌ Tesseract OCR not found!\n"
            "Install from https://github.com/UB-Mannheim/tesseract/wiki (Windows)\n"
            "or run `sudo apt install tesseract-ocr` (Linux)\n"
            "or `brew install tesseract` (macOS)\n\n"
            "If already installed, add it to PATH or manually set in this script."
        )
    pytesseract.pytesseract.tesseract_cmd = tess_path

    img = cv2.imread(str(image_path))
    if img is None:
        raise FileNotFoundError(f"⚠️ Could not load image: {image_path}")

    proc = preprocess_image(img, mode)
    text = pytesseract.image_to_string(proc, lang=lang, config="--psm 6")
    return text.strip(), proc

def main():
    parser = argparse.ArgumentParser(description="OCR Text Extraction using OpenCV + Tesseract")
    parser.add_argument("--image", "-i", required=True, help="Path to input image")
    parser.add_argument("--mode", "-m", choices=["thresh", "adaptive", "smooth"], default="thresh",
                        help="Preprocessing mode")
    parser.add_argument("--lang", "-l", default="eng", help="Language (default: eng)")
    parser.add_argument("--save", "-s", action="store_true", help="Save extracted text as .txt")
    args = parser.parse_args()

    print("🔍 Processing:", args.image)
    try:
        text, proc = extract_text(args.image, args.mode, args.lang)
    except Exception as e:
        print(e)
        return

    print("\n🧾 Extracted Text:\n" + "-"*40)
    print(text or "⚠️ No text detected. Try another preprocessing mode.")
    print("-"*40)

    # Show processed image
    cv2.imshow("Processed Image", proc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if args.save:
        out_path = Path(args.image).with_suffix(".txt")
        out_path.write_text(text, encoding="utf-8")
        print(f"✅ Saved recognized text to: {out_path}")

if __name__ == "__main__":
    main()
