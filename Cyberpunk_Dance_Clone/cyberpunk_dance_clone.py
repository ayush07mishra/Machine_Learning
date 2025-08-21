import cv2
import mediapipe as mp
import numpy as np
import copy

# Initialize Mediapipe Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Set drawing style for cyberpunk glow
def draw_glowing_pose(image, landmarks, color=(0, 255, 255), thickness=2):
    glow_img = np.zeros_like(image)
    
    if landmarks is not None:
        mp_drawing.draw_landmarks(
            glow_img,
            landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=color, thickness=thickness, circle_radius=2),
            connection_drawing_spec=mp_drawing.DrawingSpec(color=color, thickness=thickness)
        )
        
        # Apply glow effect
        blur = cv2.GaussianBlur(glow_img, (0, 0), sigmaX=10, sigmaY=10)
        image = cv2.addWeighted(image, 1.0, blur, 0.8, 0)

    return image

# Mirror coordinates for clone
def mirror_landmarks(landmarks, width):
    for lm in landmarks.landmark:
        lm.x = 1.0 - lm.x  # Flip X
    return landmarks

# Main loop
cap = cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # Flip to mirror
        height, width, _ = frame.shape

        # Convert to RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        # Original pose
        if results.pose_landmarks:
            frame = draw_glowing_pose(frame, results.pose_landmarks)

            # Clone pose
            mirrored_landmarks = mirror_landmarks(copy.deepcopy(results.pose_landmarks), width)

            
            # Offset mirrored pose to the left
            clone_img = np.zeros_like(frame)
            for lm in mirrored_landmarks.landmark:
                lm.x -= 0.3  # shift left
                lm.x = max(0, min(1, lm.x))  # keep in bounds

            frame = draw_glowing_pose(frame, mirrored_landmarks, color=(255, 0, 255), thickness=2)

        # Show frame
        cv2.imshow('Cyberpunk Dance Clone', frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
