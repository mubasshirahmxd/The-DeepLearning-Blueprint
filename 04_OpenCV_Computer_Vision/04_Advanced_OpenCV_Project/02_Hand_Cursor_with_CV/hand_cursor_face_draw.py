"""
hand_cursor_face_draw.py
Draw on detected face region using index fingertip (landmark 8).
- Uses Haar Cascade for face ROI and MediaPipe for finger tracking
- Drawing limited to face bounding box for AR effects
- HUD, FPS, clear canvas (c), quit ESC/q
"""
import cv2
import mediapipe as mp
import time
from collections import deque
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

class FaceDrawController:
    def __init__(self, max_num_hands=1):
        self.hands = mp_hands.Hands(static_image_mode=False, max_num_hands=max_num_hands,
                                    min_detection_confidence=0.6, min_tracking_confidence=0.5)
        self.trail = deque(maxlen=512)

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        return results

def run_face_draw(hud=True):
    cap = cv2.VideoCapture(0)
    controller = FaceDrawController()
    canvas = None
    fps_prev = 0

    instructions = [
        "Draw on face using index fingertip (point index).",
        "Press 'c' to clear canvas | ESC or 'q' to quit."
    ]

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        h, w = frame.shape[:2]
        if canvas is None:
            canvas = np.zeros((h, w, 3), dtype='uint8')

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80,80))

        results = controller.process(frame)

        # get index fingertip coords (landmark 8)
        if results.multi_hand_landmarks and len(faces) > 0:
            hand = results.multi_hand_landmarks[0]
            lm = hand.landmark[8]
            x, y = int(lm.x * w), int(lm.y * h)

            # check if inside any face bbox and draw
            for (fx, fy, fw, fh) in faces:
                if fx <= x <= fx+fw and fy <= y <= fy+fh:
                    controller.trail.appendleft((x,y))
            # draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            # draw trail on canvas but only inside face bbox mask
            mask = np.zeros((h, w), dtype='uint8')
            for (fx, fy, fw, fh) in faces:
                cv2.rectangle(mask, (fx, fy), (fx+fw, fy+fh), 255, -1)
            for i in range(1, len(controller.trail)):
                if controller.trail[i-1] is None or controller.trail[i] is None:
                    continue
                if mask[controller.trail[i][1], controller.trail[i][0]] == 0:
                    continue
                thickness = int(max(1, 8 * (1 - i / float(len(controller.trail)))))
                cv2.line(canvas, controller.trail[i-1], controller.trail[i], (0,255,0), thickness)

        # overlay canvas on frame
        overlay = frame.copy()
        alpha = 0.8
        cv2.addWeighted(canvas, alpha, overlay, 1-alpha, 0, overlay)

        # HUD
        if hud:
            cv2.rectangle(overlay, (5,5), (530,75), (0,0,0), -1)
            y0 = 25
            for line in instructions:
                cv2.putText(overlay, line, (10,y0), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
                y0 += 20

        # FPS
        now = time.time()
        fps = 1 / (now - fps_prev) if fps_prev else 0
        fps_prev = now
        cv2.putText(overlay, f"FPS: {int(fps)}", (10,95), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        cv2.imshow("Face-aware Hand Drawing", overlay)
        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):
            break
        elif key == ord('c'):
            canvas = np.zeros((h, w, 3), dtype='uint8')

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run_face_draw(hud=True)
