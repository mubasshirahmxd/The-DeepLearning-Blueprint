"""
gesture_distance_draw.py
Pinch-to-draw: uses Euclidean distance between thumb and index finger
to toggle drawing mode. Smooth drawing on a separate canvas overlay.
Controls: 'q' or ESC to quit.
"""
import cv2
import mediapipe as mp
import numpy as np
import math
from pathlib import Path
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

def euclidean_distance(pt1, pt2):
    return math.hypot(pt1[0]-pt2[0], pt1[1]-pt2[1])

def run_pinch_draw(threshold=40):
    cap = cv2.VideoCapture(0)
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.6)
    canvas = np.zeros((480, 640, 3), dtype=np.uint8)
    prev = (0,0)
    fps_prev = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        h, w = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        drawing = False
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                idx = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                th = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                ix, iy = int(idx.x*w), int(idx.y*h)
                tx, ty = int(th.x*w), int(th.y*h)
                dist = euclidean_distance((ix,iy),(tx,ty))
                if dist < threshold:
                    drawing = True
                    if prev == (0,0):
                        prev = (ix,iy)
                    cv2.line(canvas, prev, (ix,iy), (255,0,0), 5)
                    prev = (ix,iy)
                else:
                    prev = (0,0)
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        overlay = cv2.addWeighted(frame, 0.6, canvas, 0.4, 0)
        # HUD and FPS
        now = time.time()
        fps = 1/(now-fps_prev) if fps_prev else 0
        fps_prev = now
        cv2.putText(overlay, "Pinch (thumb+index) to draw. Press 's' to save. ESC/q to quit.", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),1)
        cv2.putText(overlay, f"FPS: {int(fps)}", (10,45), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0),2)
        cv2.imshow("Pinch Draw", overlay)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            Path.cwd().joinpath("gesture_paint_{}.png".format(int(time.time()))).write_bytes(cv2.imencode('.png', canvas)[1].tobytes())
            print("Saved artwork")
        if key == 27 or key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run_pinch_draw()
