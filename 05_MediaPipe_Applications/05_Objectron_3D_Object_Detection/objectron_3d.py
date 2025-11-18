import cv2
import mediapipe as mp
import time

def run_objectron_webcam(model_name='Cup'):
    # ➤ Initialize MediaPipe Objectron and drawing utils
    mp_objectron = mp.solutions.objectron
    mp_drawing = mp.solutions.drawing_utils

    # ➤ Create Objectron instance
    objectron = mp_objectron.Objectron(
        static_image_mode=False,
        max_num_objects=5,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.8,
        model_name=model_name
    )

    # ➤ Access webcam
    cap = cv2.VideoCapture(0)
    prev_time = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Failed to capture frame from webcam.")
            break

        # Flip frame for mirror effect and convert color space
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # ➤ Process frame for 3D object detection
        results = objectron.process(rgb_frame)

        # ➤ Draw detected 3D bounding boxes and axes
        if results.detected_objects:
            for detected_object in results.detected_objects:
                mp_drawing.draw_landmarks(
                    frame,
                    detected_object.landmarks_2d,
                    mp_objectron.BOX_CONNECTIONS
                )
                mp_drawing.draw_axis(
                    frame,
                    detected_object.rotation,
                    detected_object.translation
                )

        # ➤ Calculate and display FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time else 0
        prev_time = curr_time
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # ➤ Display output
        cv2.imshow("MediaPipe Objectron 3D Detection", frame)

        if cv2.waitKey(5) & 0xFF == 27:  # ESC key to exit
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_objectron_webcam()
