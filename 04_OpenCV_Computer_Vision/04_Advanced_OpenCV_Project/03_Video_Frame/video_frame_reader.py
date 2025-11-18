"""
video_frame_reader.py
Enhanced demonstration of reading and displaying video frames using OpenCV.

Features:
- Single frame preview
- Manual frame navigation
- Continuous playback with FPS display
- Keyboard controls: SPACE (pause/resume), ESC (quit)
"""
import cv2
import time
import numpy as np
from pathlib import Path

# ➤ Load video using relative path
VIDEO_PATH = Path(__file__).parent / "los_angeles.mp4"

def show_single_frame(video_path=VIDEO_PATH):
    cap = cv2.VideoCapture(str(video_path))
    ret, frame = cap.read()
    if not ret:
        print("❌ Could not read frame.")
        return
    cv2.imshow("Single Frame Preview", frame)
    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()

def manual_frame_navigation(video_path=VIDEO_PATH):
    cap = cv2.VideoCapture(str(video_path))
    print("▶ Manual Frame Navigation: Press any key to move to next frame. ESC to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Manual Frame Navigation", frame)
        key = cv2.waitKey(0) & 0xFF
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def continuous_playback(video_path=VIDEO_PATH):
    cap = cv2.VideoCapture(str(video_path))
    fps_prev = 0
    print("▶ Continuous Playback: Press SPACE to pause, ESC to quit.")

    paused = False
    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                print("⚠️ End of video reached.")
                break

            now = time.time()
            fps = 1 / (now - fps_prev) if fps_prev else 0
            fps_prev = now

            # HUD overlay
            cv2.putText(frame, f"FPS: {int(fps)}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            cv2.putText(frame, "Press SPACE to pause/resume | ESC to quit", (10,60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
            cv2.imshow("Continuous Playback", frame)

        key = cv2.waitKey(20) & 0xFF
        if key == 27:
            break
        elif key == 32:  # SPACE to pause/resume
            paused = not paused

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("1️⃣ Showing single frame...")
    show_single_frame()
    print("2️⃣ Manual navigation demo...")
    manual_frame_navigation()
    print("3️⃣ Continuous playback demo...")
    continuous_playback()
