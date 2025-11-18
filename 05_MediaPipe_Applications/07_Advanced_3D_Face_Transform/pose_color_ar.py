import cv2
import mediapipe as mp
import numpy as np

def pose_color_ar():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)
    drawing_spec = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)

    lower_color = np.array([0, 0, 0])
    upper_color = np.array([50, 50, 50])
    new_color = np.array([0, 0, 255])

    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, drawing_spec, drawing_spec)
            left_wrist = (int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * image.shape[1]),
                          int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * image.shape[0]))
            right_wrist = (int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * image.shape[1]),
                           int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * image.shape[0]))

            mask = cv2.inRange(image, lower_color, upper_color)
            colored_mask = cv2.bitwise_and(image, image, mask=mask)
            colored_mask[mask > 0] = new_color
            result = cv2.bitwise_or(image, colored_mask)
            cv2.imshow('Pose-driven AR Color Change', result)
        else:
            cv2.imshow('Pose-driven AR Color Change', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    pose_color_ar()
