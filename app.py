import cv2
import pygame

from src.phone_detector import PhoneDetector
from src.face_detector import FaceDetector
from src.eye_detector import EyeDetector


# Create detectors
face_detector = FaceDetector()
eye_detector = EyeDetector()
phone_detector = PhoneDetector()

# Initialize audio
pygame.mixer.init()

sleep_alarm = pygame.mixer.Sound("audio/sleep_alarm.mp3")
phone_alarm = pygame.mixer.Sound("audio/phone_alarm.mp3")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        print("Could not access webcam.")
        break

    # Face Detection
    frame = face_detector.detect(frame)

    # Detect eyes and calculate eye ratios
    frame, left_ratio, right_ratio, is_sleepy = eye_detector.detect(frame)

    # Phone Detection
    frame, phone_detected = phone_detector.detect(frame)
    
    if phone_detected:
      cv2.putText(
        frame,
        "PHONE DETECTED!",
        (30, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 0, 255),
        2
      )
      if not pygame.mixer.get_busy():
          phone_alarm.play()
    
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
        if not  pygame.mixer.get_busy():
                  sleep_alarm.play()

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Release resources
cap.release()
cv2.destroyAllWindows()