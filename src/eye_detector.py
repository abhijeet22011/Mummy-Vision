import cv2
import mediapipe as mp
import math


class EyeDetector:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        # MediaPipe eye landmark indices
        self.LEFT_EYE = [33, 160, 158, 133, 153, 144]
        self.RIGHT_EYE = [362, 385, 387, 263, 373, 380]

        self.EYE_CLOSED_THRESHOLD = 0.20
        self.SLEEP_THRESHOLD_FRAMES = 1
        self.closed_frames = 0

    def calculate_eye_ratio(self, landmarks, eye_indices, width, height):
        points = []

        for index in eye_indices:
            landmark = landmarks[index]

            x = int(landmark.x * width)
            y = int(landmark.y * height)

            points.append((x, y))

        # Vertical distances
        vertical_1 = math.dist(points[1], points[5])
        vertical_2 = math.dist(points[2], points[4])

        # Horizontal distance
        horizontal = math.dist(points[0], points[3])

        # Eye Aspect Ratio
        ratio = (vertical_1 + vertical_2) / (2.0 * horizontal)

        return ratio

    def detect(self, frame):
        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = self.face_mesh.process(rgb_frame)

        left_ratio = 0.0
        right_ratio = 0.0

        if results.multi_face_landmarks:
            face_landmarks = results.multi_face_landmarks[0]
            landmarks = face_landmarks.landmark

            height, width, _ = frame.shape

            left_ratio = self.calculate_eye_ratio(
                landmarks,
                self.LEFT_EYE,
                width,
                height
            )

            right_ratio = self.calculate_eye_ratio(
                landmarks,
                self.RIGHT_EYE,
                width,
                height
            )

            average_ratio = (left_ratio + right_ratio) / 2

            if average_ratio < self.EYE_CLOSED_THRESHOLD:
                self.closed_frames += 1
            else:
                self.closed_frames = 0

            is_sleepy = self.closed_frames >= self.SLEEP_THRESHOLD_FRAMES

        return frame, left_ratio, right_ratio, is_sleepy