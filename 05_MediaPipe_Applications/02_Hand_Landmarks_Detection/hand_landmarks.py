import cv2
import mediapipe as mp
import warnings
warnings.filterwarnings("ignore")

def run_hand_tracking():
    # ➤ Initialize MediaPipe Hands and Drawing Utilities
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils

    # ➤ Access the webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Failed to capture frame from webcam. Exiting...")
            break

        # Flip for mirror effect
        frame = cv2.flip(frame, 1)

        # Convert frame from BGR (OpenCV) to RGB (MediaPipe expects RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and detect hand landmarks
        result = hands.process(rgb_frame)

        # Draw landmarks if detected
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display the processed frame
        cv2.imshow("MediaPipe Hand Tracking", frame)

        # Exit loop when ESC key is pressed
        if cv2.waitKey(5) & 0xFF == 27:
            break

    # ➤ Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_hand_tracking()
