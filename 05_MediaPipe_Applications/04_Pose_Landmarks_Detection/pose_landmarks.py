import cv2
import mediapipe as mp
import time

def run_pose_tracking():
    # ➤ Initialize Pose model
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils

    # ➤ Access webcam
    cap = cv2.VideoCapture(0)
    previous_time = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Failed to read frame from webcam.")
            break

        # Flip for mirror effect
        frame = cv2.flip(frame, 1)

        # Convert BGR to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # ➤ Process frame with MediaPipe Pose
        results = pose.process(rgb)

        # ➤ Draw pose landmarks if detected
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)
            )

        # ➤ Calculate and display FPS
        current_time = time.time()
        fps = 1 / (current_time - previous_time) if previous_time else 0
        previous_time = current_time
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        # ➤ Show frame
        cv2.imshow("MediaPipe Pose Landmarks", frame)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_pose_tracking()
