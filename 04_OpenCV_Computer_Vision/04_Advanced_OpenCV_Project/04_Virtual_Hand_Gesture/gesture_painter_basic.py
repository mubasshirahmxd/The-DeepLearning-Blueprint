"""
gesture_painter_basic.py
Virtual painter using index fingertip as brush.
- Clear canvas when all fingers are up.
- Press 'q' or ESC to quit.
"""
import cv2
import numpy as np
import mediapipe as mp
import time
from pathlib import Path

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

def fingers_up_from_landmarks(lm_list):
    fingers = []
    # tips: [8,12,16,20], compare y to y-2
    for tip_id in [8,12,16,20]:
        fingers.append(1 if lm_list[tip_id][1] < lm_list[tip_id-2][1] else 0)
    return fingers

def run_basic_painter(brush_thickness=8):
    cap = cv2.VideoCapture(0)
    hands = mp_hands.Hands(max_num_hands=1)
    canvas = None
    xp, yp = 0,0
    fps_prev = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame,1)
        h,w = frame.shape[:2]
        if canvas is None:
            canvas = np.zeros_like(frame)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                lm_list = []
                for id, lm in enumerate(handLms.landmark):
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    lm_list.append((cx,cy))
                if lm_list:
                    x1,y1 = lm_list[8]  # index tip
                    x2,y2 = lm_list[12] # middle tip
                    fingers = fingers_up_from_landmarks(lm_list)
                    if fingers[0] and not fingers[1]:
                        cv2.circle(frame, (x1,y1), 8, (255,0,255), -1)
                        if xp == 0 and yp == 0:
                            xp, yp = x1, y1
                        cv2.line(canvas, (xp,yp), (x1,y1), (255,0,255), brush_thickness)
                        xp, yp = x1, y1
                    else:
                        xp, yp = 0,0
                    if all(fingers):
                        canvas = np.zeros_like(frame)
                mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
        # merge canvas and frame
        gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray_canvas, 20, 255, cv2.THRESH_BINARY)
        inv_mask = cv2.bitwise_not(mask)
        frame_bg = cv2.bitwise_and(frame, frame, mask=inv_mask)
        frame_fg = cv2.bitwise_and(canvas, canvas, mask=mask)
        final = cv2.add(frame_bg, frame_fg)
        now = time.time()
        fps = 1/(now-fps_prev) if fps_prev else 0
        fps_prev = now
        cv2.putText(final, f"FPS: {int(fps)}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0),2)
        cv2.imshow("Virtual Painter Basic", final)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run_basic_painter()
