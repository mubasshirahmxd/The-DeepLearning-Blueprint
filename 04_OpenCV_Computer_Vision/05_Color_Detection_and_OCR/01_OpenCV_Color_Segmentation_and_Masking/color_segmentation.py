"""
color_segmentation.py
Webcam-based OpenCV color segmentation & masking utility.
Controls:
 - r : Red mask
 - g : Green mask
 - b : Blue mask
 - a : All colors except white mask
 - o : Original frame
 - h : show HSV frame
 - s : save current mask as PNG
 - ESC / q : quit
"""
import cv2
import numpy as np
import time
from pathlib import Path

# HSV ranges for colors (tunable)
COLOR_RANGES = {
    "red": [([0,120,70], [10,255,255]), ([170,120,70], [180,255,255])],  # two ranges for red
    "green": [([36, 25, 25], [86, 255,255])],
    "blue": [([94, 80, 2], [126, 255, 255])],
    "non_white": [([0, 0, 0], [180, 255, 200])]  # everything except very bright whites
}

def get_mask(hsv, ranges):
    mask = None
    for (lower, upper) in ranges:
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        m = cv2.inRange(hsv, lower, upper)
        mask = m if mask is None else cv2.bitwise_or(mask, m)
    return mask

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    mode = "original"
    save_count = 0
    fps_prev = time.time()

    print("Controls: r=red, g=green, b=blue, a=all except white, o=original, h=hsv, s=save mask, ESC/q=quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame,1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        display = frame.copy()

        if mode == "red":
            mask = get_mask(hsv, COLOR_RANGES["red"])
            display = cv2.bitwise_and(frame, frame, mask=mask)
        elif mode == "green":
            mask = get_mask(hsv, COLOR_RANGES["green"])
            display = cv2.bitwise_and(frame, frame, mask=mask)
        elif mode == "blue":
            mask = get_mask(hsv, COLOR_RANGES["blue"])
            display = cv2.bitwise_and(frame, frame, mask=mask)
        elif mode == "non_white":
            mask = get_mask(hsv, COLOR_RANGES["non_white"])
            display = cv2.bitwise_and(frame, frame, mask=mask)
        elif mode == "hsv":
            display = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        else:
            display = frame

        # HUD
        fps_now = time.time()
        fps = 1/(fps_now - fps_prev) if fps_prev else 0
        fps_prev = fps_now
        cv2.putText(display, f"Mode: {mode} | FPS: {int(fps)}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0),2)
        cv2.imshow("Color Segmentation", display)

        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):
            break
        elif key == ord('r'):
            mode = "red"
        elif key == ord('g'):
            mode = "green"
        elif key == ord('b'):
            mode = "blue"
        elif key == ord('a'):
            mode = "non_white"
        elif key == ord('o'):
            mode = "original"
        elif key == ord('h'):
            mode = "hsv"
        elif key == ord('s'):
            save_path = Path.cwd() / f"color_mask_{mode}_{int(time.time())}.png"
            if 'mask' in locals():
                cv2.imwrite(str(save_path), mask)
                print(f"Saved mask to {save_path}")
            else:
                cv2.imwrite(str(save_path), display)
                print(f"Saved frame to {save_path}")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
