import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# Eye landmark indexes (MediaPipe)
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

def get_eye_ratio(landmarks, eye_points, w, h):
    points = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in eye_points]

    # vertical distance
    v1 = abs(points[1][1] - points[5][1])
    v2 = abs(points[2][1] - points[4][1])

    # horizontal distance
    h_dist = abs(points[0][0] - points[3][0])

    return (v1 + v2) / (2.0 * h_dist)


def detect_blink(frame):
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:

            left_ratio = get_eye_ratio(face_landmarks.landmark, LEFT_EYE, w, h)
            right_ratio = get_eye_ratio(face_landmarks.landmark, RIGHT_EYE, w, h)

            ratio = (left_ratio + right_ratio) / 2

            # Draw points
            for idx in LEFT_EYE + RIGHT_EYE:
                x = int(face_landmarks.landmark[idx].x * w)
                y = int(face_landmarks.landmark[idx].y * h)
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            # Blink detection
            if ratio < 0.25:
                cv2.putText(frame, "BLINK", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return True