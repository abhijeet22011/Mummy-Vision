import cv2
from src.eye_detector import EyeDetector


# Create eye detector
eye_detector = EyeDetector()

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        print("Could not access webcam.")
        break

    # Detect facial landmarks
    frame, left_ratio, right_ratio = eye_detector.detect(frame)

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
    cv2.imshow("MummyVision - Eye Test", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()