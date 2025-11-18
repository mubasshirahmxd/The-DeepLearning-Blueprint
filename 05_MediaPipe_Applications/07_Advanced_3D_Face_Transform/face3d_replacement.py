import cv2
import mediapipe as mp
import numpy as np

def face3d_replacement():
    mp_drawing = mp.solutions.drawing_utils
    mp_face_mesh = mp.solutions.face_mesh

    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, color=(0, 255, 0))

    cap = cv2.VideoCapture(0)

    # Capture a replacement face once (press 'c' to capture replacement face)
    replacement_face = None
    print("Press 'c' to capture a replacement face image for overlay. Press 'q' to quit.")

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break
        image = cv2.flip(image, 1)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('c'):
            replacement_face = image.copy()
            print("Replacement face captured.")
        if k == ord('q'):
            break

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)
        transformed_image = image.copy()

        if results.multi_face_landmarks and replacement_face is not None:
            for face_landmarks in results.multi_face_landmarks:
                # Convert landmarks to pixel coordinates
                landmarks = [(lm.x, lm.y, lm.z) for lm in face_landmarks.landmark]
                x_coords = [int(l[0] * image.shape[1]) for l in landmarks]
                y_coords = [int(l[1] * image.shape[0]) for l in landmarks]
                xmin, xmax = min(x_coords), max(x_coords)
                ymin, ymax = min(y_coords), max(y_coords)

                # Resize replacement face to ROI and blend
                roi_width = xmax - xmin
                roi_height = ymax - ymin
                if roi_width > 0 and roi_height > 0:
                    resized = cv2.resize(replacement_face, (roi_width, roi_height))
                    mask = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
                    _, mask = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)
                    mask_inv = cv2.bitwise_not(mask)
                    roi = transformed_image[ymin:ymax, xmin:xmax]
                    bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
                    fg = cv2.bitwise_and(resized, resized, mask=mask)
                    dst = cv2.add(bg, fg)
                    transformed_image[ymin:ymax, xmin:xmax] = dst

                mp_drawing.draw_landmarks(transformed_image, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION, landmark_drawing_spec=drawing_spec, connection_drawing_spec=drawing_spec)

        cv2.imshow('Face Replacement / Morphing (Press c to capture replacement)', transformed_image)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    face3d_replacement()
