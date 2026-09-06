import cv2
from src.face_detector import FaceDetector


# Create face detector
face_detector = FaceDetector()

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        print("Could not access webcam.")
        break

    # Detect faces
    frame = face_detector.detect(frame)

    # Display
    cv2.imshow("MummyVision", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()