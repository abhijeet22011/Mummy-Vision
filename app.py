import cv2
from src.face_detector import FaceDetector
from src.eye_detector import EyeDetector


# Create detectors
face_detector = FaceDetector()
eye_detector = EyeDetector()

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        print("Could not access webcam.")
        break

    # Detect face
    frame = face_detector.detect(frame)

    # Detect eyes and calculate eye ratios
    frame, left_ratio, right_ratio, is_sleepy = eye_detector.detect(frame)

    # Display eye ratios
    cv2.putText(
        frame,
        f"Left: {left_ratio:.2f}  Right: {right_ratio:.2f}",
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Display
    cv2.imshow("MummyVision", frame)

    if is_sleepy:
        cv2.putText(
        frame,
        "WAKE UP! MUMMY IS WATCHING!",
        (30, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Release resources
cap.release()
cv2.destroyAllWindows()