"""
hand_cursor_basic.py
Air-draw using wrist position tracked by MediaPipe Hands.
- Left-click style drawing (continuous lines)
- HUD overlay, FPS counter, clear canvas (c), exit ESC/q
- Run locally in VSCode/terminal (webcam + GUI required)
"""
import cv2
import mediapipe as mp
import time
from collections import deque

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

class HandCursorController:
    def __init__(self, max_num_hands=1, min_detection_confidence=0.6):
        self.hands = mp_hands.Hands(static_image_mode=False,
                                    max_num_hands=max_num_hands,
                                    min_detection_confidence=min_detection_confidence,
                                    min_tracking_confidence=0.5)
        self.trail = deque(maxlen=512)  # store points for drawing

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        return results

def run_hand_cursor(hud=True, canvas_size=(640,480)):
    cap = cv2.VideoCapture(0)
    controller = HandCursorController()
    canvas = None
    fps_prev = 0

    instructions = [
        "Air-draw: Move your wrist to draw.",
        "Press 'c' to clear canvas | ESC or 'q' to quit."
    ]

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        h, w = frame.shape[:2]
        if canvas is None:
            canvas = 255 * np.ones((h, w, 3), dtype='uint8')

        results = controller.process(frame)

        # get wrist coords (hand landmark 0)
        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]
            lm = hand.landmark[0]  # wrist
            x, y = int(lm.x * w), int(lm.y * h)
            controller.trail.appendleft((x,y))

            # draw trail onto canvas
            for i in range(1, len(controller.trail)):
                if controller.trail[i-1] is None or controller.trail[i] is None:
                    continue
                thickness = int(max(1, 8 * (1 - i / float(len(controller.trail)))))
                cv2.line(canvas, controller.trail[i-1], controller.trail[i], (0,0,255), thickness)

            # draw landmarks on frame
            mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        # overlay canvas on a copy of frame (semi-transparent)
        overlay = frame.copy()
        if canvas is not None:
            alpha = 0.7
            cv2.addWeighted(canvas, alpha, overlay, 1-alpha, 0, overlay)

        # HUD
        if hud:
            cv2.rectangle(overlay, (5,5), (460,75), (0,0,0), -1)
            y0 = 25
            for line in instructions:
                cv2.putText(overlay, line, (10,y0), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
                y0 += 20

        # FPS
        now = time.time()
        fps = 1 / (now - fps_prev) if fps_prev else 0
        fps_prev = now
        cv2.putText(overlay, f"FPS: {int(fps)}", (10,95), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        cv2.imshow("Hand Cursor - Air Draw", overlay)
        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):
            break
        elif key == ord('c'):
            canvas = 255 * np.ones((h, w, 3), dtype='uint8')

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    import numpy as np
    run_hand_cursor(hud=True)
