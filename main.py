import cv2
from blink import detect_blink

def main():
    cap = cv2.VideoCapture(0)

    print("Camera started. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # 🔍 Detect blink
        blink_detected = detect_blink(frame)

        # 💧 Simulate hardware trigger
        if blink_detected:
            print("💧 TRIGGER")

            cv2.putText(frame, "DROP 💧", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 3)

        # 🖥️ Show camera
        cv2.imshow("Blink Detection", frame)

        # ❌ Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Stopping camera...")
            break

    # 🧹 Cleanup
    cap.release()
    cv2.destroyAllWindows()
    print("Camera closed successfully")

if __name__ == "__main__":
    main()