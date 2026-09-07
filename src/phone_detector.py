import cv2
from ultralytics import YOLO


class PhoneDetector:
    def __init__(self):
        self.model = YOLO("yolo11n.pt")

    def detect(self, frame):
        results = self.model(frame, verbose=False)

        phone_detected = False

        for result in results:
            for box in result.boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                if class_id == 67 and confidence > 0.85:

                    phone_detected = True

                    x1, y1, x2, y2 = map(
                        int, box.xyxy[0]
                    )

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 0, 255),
                        2
                    )

                    cv2.putText(
                        frame,
                        f"PHONE {confidence:.2f}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 0, 255),
                        2
                    )

        return frame, phone_detected