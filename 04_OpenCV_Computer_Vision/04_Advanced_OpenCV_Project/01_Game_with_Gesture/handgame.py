import cv2
import mediapipe as mp
import pyautogui
import time
from collections import deque

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

class IndexFingerSwipeTracker:
    def __init__(self, min_detection_confidence=0.7, max_num_hands=1):
        self.hands = mp_hands.Hands(min_detection_confidence=min_detection_confidence,
                                    max_num_hands=max_num_hands)
        self.last_pos = None
        self.raw_last = None
        self.alpha = 0.6
        self.swipe_threshold_x = 0.05
        self.swipe_threshold_y = 0.05
        self.cooldown = 0.5
        self.last_trigger = 0

    def detect_gesture(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        gesture = None
        hand_landmarks = None

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            index_tip = hand_landmarks.landmark[8]
            raw_pos = (index_tip.x, index_tip.y)

            if self.raw_last is None:
                self.raw_last = raw_pos

            dx = raw_pos[0] - self.raw_last[0]
            dy = raw_pos[1] - self.raw_last[1]

            if self.last_pos is None:
                self.last_pos = raw_pos
            else:
                self.last_pos = (self.alpha * raw_pos[0] + (1 - self.alpha) * self.last_pos[0],
                                 self.alpha * raw_pos[1] + (1 - self.alpha) * self.last_pos[1])

            self.raw_last = raw_pos

            if abs(dx) > self.swipe_threshold_x and abs(dx) > abs(dy):
                gesture = "left" if dx > 0 else "right"
            elif abs(dy) > self.swipe_threshold_y and abs(dy) > abs(dx):
                gesture = "down" if dy > 0 else "up"
        else:
            self.last_pos = None
            self.raw_last = None

        return gesture, hand_landmarks

def trigger_key(gesture, tracker):
    now = time.time()
    if gesture and (now - tracker.last_trigger > tracker.cooldown):
        pyautogui.press(gesture)
        tracker.last_trigger = now

def run_hand_game(hud=True, trail=True):
    cap = cv2.VideoCapture(0)
    tracker = IndexFingerSwipeTracker()
    fps_prev = 0
    pts = deque(maxlen=64) if trail else None

    instructions = [
        "Gesture Controls: Swipe L/R/U/D to press arrow keys",
        "Press 'c' to clear trail (if enabled) | ESC or 'q' to quit"
    ]

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        gesture, landmarks = tracker.detect_gesture(frame)

        if landmarks:
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=4),
                                      mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2))
            if trail:
                lm = landmarks.landmark[8]
                x, y = int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])
                pts.appendleft((x, y))
                for i in range(1, len(pts)):
                    if pts[i - 1] is None or pts[i] is None:
                        continue
                    thickness = int(max(1, 8 * (1 - i / float(len(pts)))))
                    cv2.line(frame, pts[i - 1], pts[i], (0, 255, 255), thickness)

        if hud:
            cv2.rectangle(frame, (5, 5), (430, 70), (0, 0, 0), -1)
            y0 = 20
            for line in instructions:
                cv2.putText(frame, line, (10, y0), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                y0 += 20

        if gesture:
            cv2.putText(frame, f"Gesture: {gesture.upper()}", (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 128, 255), 2)
            trigger_key(gesture, tracker)

        fps_now = time.time()
        fps = 1 / (fps_now - fps_prev) if fps_prev else 0
        fps_prev = fps_now
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Gesture Game Controller", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):
            break
        elif key == ord('c') and trail:
            pts.clear()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run_hand_game(hud=True, trail=True)
