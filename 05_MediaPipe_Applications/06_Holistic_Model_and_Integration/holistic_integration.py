import cv2
import time
import mediapipe as mp

def run_holistic_tracking():
    # ➤ Initialize Holistic model and drawing utilities
    mp_holistic = mp.solutions.holistic
    holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils

    # ➤ Drawing styles (color-coded)
    face_spec = mp_drawing.DrawingSpec(color=(255,0,255), thickness=1, circle_radius=1)
    face_conn_spec = mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius=1)
    hand_spec = mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2)
    pose_spec = mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)

    cap = cv2.VideoCapture(0)
    prev_time = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Failed to read frame from webcam.")
            break

        # Resize for stability (optional) and mirror
        frame = cv2.resize(frame, (960, 720))
        frame = cv2.flip(frame, 1)

        # Convert color and process
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb.flags.writeable = False
        results = holistic.process(rgb)
        rgb.flags.writeable = True

        # Convert back to BGR for OpenCV drawing
        image = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

        # Draw face landmarks (mesh & contours) if present
        if results.face_landmarks:
            mp_drawing.draw_landmarks(
                image,
                results.face_landmarks,
                mp_holistic.FACEMESH_TESSELATION,
                landmark_drawing_spec=face_spec,
                connection_drawing_spec=face_conn_spec
            )
            mp_drawing.draw_landmarks(
                image,
                results.face_landmarks,
                mp_holistic.FACEMESH_CONTOURS,
                landmark_drawing_spec=face_spec,
                connection_drawing_spec=face_conn_spec
            )

        # Draw right hand landmarks
        if results.right_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                results.right_hand_landmarks,
                mp_holistic.HAND_CONNECTIONS,
                landmark_drawing_spec=hand_spec,
                connection_drawing_spec=hand_spec
            )

        # Draw left hand landmarks
        if results.left_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                results.left_hand_landmarks,
                mp_holistic.HAND_CONNECTIONS,
                landmark_drawing_spec=hand_spec,
                connection_drawing_spec=hand_spec
            )

        # Draw pose landmarks (full body skeleton)
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec=pose_spec,
                connection_drawing_spec=pose_spec
            )

        # FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time else 0
        prev_time = curr_time
        cv2.putText(image, f"FPS: {int(fps)}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.imshow("MediaPipe Holistic Integration", image)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run_holistic_tracking()
