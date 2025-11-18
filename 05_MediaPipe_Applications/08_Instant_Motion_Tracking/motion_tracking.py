import cv2
import mediapipe as mp
import time
from collections import deque

def run_motion_tracking(trail_length=64, draw_trail=True):
    # Real-time hand motion tracking using MediaPipe Hands.
    # - trail_length: number of points to remember for trail
    # - draw_trail: whether to draw motion trajectory for index fingertip
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # Drawing specs
    landmark_spec = mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2)
    connection_spec = mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)

    # Deque to store fingertip positions for trail (index finger tip = landmark 8)
    pts = deque(maxlen=trail_length)

    cap = cv2.VideoCapture(0)
    previous_time = 0

    with mp_hands.Hands(static_image_mode=False, max_num_hands=2,
                        min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                print("Failed to grab frame. Exiting...")
                break

            frame = cv2.flip(frame, 1)  # mirror view
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            # Draw landmarks
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                              landmark_spec, connection_spec)

                    # get index fingertip coords (landmark 8) in pixel space
                    lm = hand_landmarks.landmark[8]
                    x = int(lm.x * frame.shape[1])
                    y = int(lm.y * frame.shape[0])
                    pts.appendleft((x, y))

            # Draw trajectory trail
            if draw_trail and len(pts) > 1:
                for i in range(1, len(pts)):
                    if pts[i - 1] is None or pts[i] is None:
                        continue
                    thickness = int(max(1, 10 * (1 - i / float(len(pts)))))
                    cv2.line(frame, pts[i - 1], pts[i], (0, 255, 255), thickness)

            # FPS calculation
            current_time = time.time()
            fps = 1 / (current_time - previous_time) if previous_time else 0
            previous_time = current_time
            cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            cv2.imshow("Instant Motion Tracking - MediaPipe Hands", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord('q'):  # ESC or q to quit
                break
            elif key == ord('c'):  # clear trail
                pts.clear()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run_motion_tracking()
