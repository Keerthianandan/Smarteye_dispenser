import cv2
from alignment import is_aligned

# Load Haarcascade files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


def detect_eye(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces first (for accuracy)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Get frame size
    h, w = frame.shape[:2]

    for (x, y, fw, fh) in faces:
        # Draw face box (optional but helpful)
        cv2.rectangle(frame, (x, y), (x + fw, y + fh), (255, 0, 0), 2)

        # Region of interest (face area)
        roi_gray = gray[y:y + fh, x:x + fw]
        roi_color = frame[y:y + fh, x:x + fw]

        # Detect eyes inside face
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

        for (ex, ey, ew, eh) in eyes:
            # Calculate eye center
            eye_center_x = x + ex + ew // 2
            eye_center_y = y + ey + eh // 2

            # Check alignment
            aligned = is_aligned(eye_center_x, eye_center_y, w, h)

            if aligned:
                color = (0, 255, 0)  # Green
                cv2.putText(frame, "ALIGNED", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            else:
                color = (0, 0, 255)  # Red

            # Draw eye rectangle
            cv2.rectangle(frame,
                          (x + ex, y + ey),
                          (x + ex + ew, y + ey + eh),
                          color, 2)

            # Draw center point
            cv2.circle(frame,
                       (eye_center_x, eye_center_y),
                       3, (255, 255, 0), -1)