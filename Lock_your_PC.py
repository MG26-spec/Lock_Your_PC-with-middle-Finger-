import cv2
import mediapipe as mp
import os
import platform

# Initialize MediaPipe Hand Detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Finger tip landmark indexes
finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

# Start webcam
cap = cv2.VideoCapture(0)

def is_middle_finger_only_up(landmarks):
    fingers = []

    # Thumb: check x coordinate for left/right hand
    if landmarks[4].x < landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers: tip.y < pip.y means finger is up
    for tip_id in [8, 12, 16, 20]:
        if landmarks[tip_id].y < landmarks[tip_id - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Return True if only middle finger is up
    return fingers == [0, 0, 1, 0, 0]

def lock_screen():
    system = platform.system()
    if system == "Windows":
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif system == "Linux":
        os.system("gnome-screensaver-command -l")
    elif system == "Darwin":  
        os.system("/System/Library/CoreServices/Menu\\ Extras/User.menu/Contents/Resources/CGSession -suspend")

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_middle_finger_only_up(hand_landmarks.landmark):
                print("Middle finger detected. Locking screen...")
                lock_screen()
                cap.release()
                cv2.destroyAllWindows()
                exit()

    cv2.imshow("Gesture Lock", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

