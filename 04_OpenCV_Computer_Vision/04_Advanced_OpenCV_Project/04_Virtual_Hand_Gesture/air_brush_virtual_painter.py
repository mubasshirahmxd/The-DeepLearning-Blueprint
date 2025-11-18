"""
air_brush_virtual_painter_fixed.py
Enhanced version of Air Brush Virtual Painter
✅ Works in mirrored webcam
✅ Stable drawing & toolbar
✅ FPS + Save + Eraser + Clear gesture
"""

import cv2
import numpy as np
import mediapipe as mp
import time
from pathlib import Path

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

def run_air_brush():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    draw_color = (255, 0, 255)
    brush_thickness = 7
    eraser_thickness = 50
    xp, yp = 0, 0
    img_canvas = np.zeros((720, 1280, 3), np.uint8)
    fps_prev = time.time()

    tip_ids = [4, 8, 12, 16, 20]

    def fingers_up(hand_landmarks):
        fingers = []
        # Thumb — adjust logic for mirrored cam
        if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[tip_ids[0] - 1].x:
            fingers.append(1)
        else:
            fingers.append(0)
        # Other fingers
        for id in range(1, 5):
            if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

    while True:
        ret, img = cap.read()
        if not ret:
            break

        img = cv2.flip(img, 1)
        h, w = img.shape[:2]
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                lm_list = [(int(lm.x * w), int(lm.y * h)) for lm in handLms.landmark]
                if lm_list:
                    x1, y1 = lm_list[8]  # index
                    x2, y2 = lm_list[12]  # middle
                    fingers = fingers_up(handLms)

                    # Selection Mode (two fingers up)
                    if fingers[1] and fingers[2]:
                        xp, yp = 0, 0
                        cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), draw_color, cv2.FILLED)
                        if y1 < 120:
                            if 250 < x1 < 450:
                                draw_color = (255, 0, 255)
                            elif 550 < x1 < 750:
                                draw_color = (0, 255, 0)
                            elif 800 < x1 < 950:
                                draw_color = (0, 0, 255)
                            elif 1000 < x1 < 1200:
                                draw_color = (0, 0, 0)

                    # Drawing Mode (index up)
                    elif fingers[1] and not fingers[2]:
                        cv2.circle(img, (x1, y1), 15, draw_color, cv2.FILLED)
                        if xp == 0 and yp == 0:
                            xp, yp = x1, y1
                        if draw_color == (0, 0, 0):
                            cv2.line(img_canvas, (xp, yp), (x1, y1), draw_color, eraser_thickness)
                        else:
                            cv2.line(img_canvas, (xp, yp), (x1, y1), draw_color, brush_thickness)
                        xp, yp = x1, y1

                    # Clear gesture (all fingers up)
                    if all(fingers):
                        img_canvas = np.zeros((720, 1280, 3), np.uint8)

                mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

        # Combine image and canvas
        img_gray = cv2.cvtColor(img_canvas, cv2.COLOR_BGR2GRAY)
        _, img_inv = cv2.threshold(img_gray, 20, 255, cv2.THRESH_BINARY_INV)
        img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(img, img_inv)
        img = cv2.bitwise_or(img, img_canvas)

        # Toolbar
        cv2.rectangle(img, (250, 0), (450, 100), (255, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (550, 0), (750, 100), (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (800, 0), (950, 100), (0, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (1000, 0), (1200, 100), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, "Press 'S' to Save | ESC to Quit", (10, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # FPS
        fps_now = time.time()
        fps = 1 / (fps_now - fps_prev)
        fps_prev = fps_now
        cv2.putText(img, f"FPS: {int(fps)}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Air Brush Painter", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("s"):
            filename = f"air_art_{int(time.time())}.png"
            cv2.imwrite(filename, img_canvas)
            print(f"✅ Artwork saved as {filename}")
        elif key == 27 or key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_air_brush()
