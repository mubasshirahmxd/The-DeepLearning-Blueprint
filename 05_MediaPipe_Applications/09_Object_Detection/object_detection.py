import cv2
import mediapipe as mp
import time

def run_face_detection(min_detection_confidence=0.5):
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    prev_time = 0

    with mp_face_detection.FaceDetection(min_detection_confidence=min_detection_confidence) as face_detection:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                print("Failed to read frame from webcam.")
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = face_detection.process(rgb)

            face_count = 0
            if results.detections:
                face_count = len(results.detections)
                for i, detection in enumerate(results.detections, start=1):
                    # Draw detection using mediapipe util
                    mp_drawing.draw_detection(frame, detection)

                    # Extract bounding box and score for custom label
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, _ = frame.shape
                    x = int(bboxC.xmin * iw)
                    y = int(bboxC.ymin * ih)
                    w = int(bboxC.width * iw)
                    h = int(bboxC.height * ih)
                    score = int(detection.score[0] * 100) if detection.score else 0

                    # Draw label background
                    label = f"Face {i}: {score}%"
                    cv2.rectangle(frame, (x, y-25), (x + len(label)*10, y), (0, 0, 0), -1)
                    cv2.putText(frame, label, (x+2, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

            # FPS
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time) if prev_time else 0
            prev_time = curr_time
            cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            # Face count
            cv2.putText(frame, f"Faces: {face_count}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)

            cv2.imshow("MediaPipe Face Detection - 2D", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    run_face_detection()
