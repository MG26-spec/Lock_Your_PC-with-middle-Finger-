# Lock_Your_PC-with-middle-Finger-
# 🖐️ Lock Your PC with a Gesture

This Python project allows you to **lock your PC using a specific hand gesture** — showing **only your middle finger** to the webcam. It leverages **OpenCV** and **MediaPipe** for real-time hand detection and gesture recognition.

## 🔒 Features

- Detects hand gestures in real-time using your webcam.
- Locks your computer when **only the middle finger** is raised.
- Works across major operating systems:
  - ✅ Windows
  - ✅ Linux (GNOME)
  - ✅ macOS

## 🛠️ Requirements

- Python 3.x
- OpenCV
- MediaPipe

### 📦 Installation

Install the required libraries using pip:

```bash
pip install opencv-python mediapipe
🚀 How to Run
Run the script using Python:

bash
Copy
Edit
python Lock_your_PC.py
Make sure your webcam is enabled.

Raise only your middle finger to trigger the lock.

Press q to exit the application manually.

⚙️ How It Works
Uses MediaPipe to detect hand landmarks.

Checks the position of fingers to see if only the middle finger is up.

If the condition is met, executes a system-specific command to lock the screen.

🧠 Logic Breakdown
Thumb and all other fingers except the middle one must be down.

If the middle finger is the only one raised, the system is locked immediately.

⚠️ Note
The system will lock immediately once the gesture is detected. Make sure to save your work before running this script.

📷 Preview
