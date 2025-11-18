import cv2
import mediapipe as mp
import numpy as np

def face3d_transform_matrix(scale=1.5):
    mp_drawing = mp.solutions.drawing_utils
    mp_face_mesh = mp.solutions.face_mesh

    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, color=(0, 255, 0))

    # 3x3 transformation matrix (apply to x,y,z normalized coords)
    transformation_matrix = np.array([[scale, 0, 0],
                                      [0, scale, 0],
                                      [0, 0, 1]])

    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)

        transformed_image = image.copy()
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                landmarks = np.zeros((468, 3), dtype=np.float32)
                for i, lm in enumerate(face_landmarks.landmark):
                    landmarks[i] = [lm.x, lm.y, lm.z]

                # Apply transformation
                transformed = landmarks @ transformation_matrix.T

                # Draw transformed landmarks
                for (x_norm, y_norm, z) in transformed:
                    x = int(x_norm * image.shape[1])
                    y = int(y_norm * image.shape[0])
                    cv2.circle(transformed_image, (x, y), 1, (255, 0, 0), -1)

                # Also draw original mesh for comparison
                mp_drawing.draw_landmarks(transformed_image, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION, landmark_drawing_spec=drawing_spec, connection_drawing_spec=drawing_spec)

        cv2.imshow('Face 3D Transform (Matrix Scaling)', transformed_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    face3d_transform_matrix()
