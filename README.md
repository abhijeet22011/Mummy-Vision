# 👀 MummyVision

### Your AI-powered study watchdog


MummyVision is a computer-vision-based personal study assistant that helps you stay focused while studying. It uses your webcam and AI models to detect common distractions and provide real-time alerts.

## 🚀 Features

- 📱 Phone detection
- 😴 Drowsiness detection
- 👤 Face monitoring
- 🔔 Real-time audio alerts
- 📷 Real-time webcam monitoring
- 🤖 YOLO-based object detection
- 👁️ Face landmark-based eye detection

## 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- CVZone
- YOLO (Ultralytics)
- Pygame

## ⚙️ How It Works

```text
📷 Webcam
    │
    ▼
┌─────────────────┐
│  MummyVision 👀 │
└────────┬────────┘
         │
   ┌─────┼─────┐
   ▼     ▼     ▼
  😴     📱     👤
 Sleep  Phone  Face
   │     │     │
   └─────┼─────┘
         ▼
      🚨 Alert
