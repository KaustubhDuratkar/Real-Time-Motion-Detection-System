import cv2
import numpy as np
from datetime import datetime

# Start camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Video writer (for recording)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('motion_record.avi', fourcc, 20.0, (640,480))

# Read initial frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# Resize for performance
frame1 = cv2.resize(frame1, (640,480))
frame2 = cv2.resize(frame2, (640,480))

# Create window
cv2.namedWindow("Motion Detector")

# Trackbar for sensitivity
def nothing(x):
    pass

cv2.createTrackbar("Sensitivity", "Motion Detector", 20, 100, nothing)

# FPS calculation
prev_time = datetime.now()

while cap.isOpened():
    
    # Resize frames
    frame1 = cv2.resize(frame1, (640,480))
    frame2 = cv2.resize(frame2, (640,480))
    
    # Frame difference
    diff = cv2.absdiff(frame1, frame2)
    
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)

    # Get sensitivity from trackbar
    sensitivity = cv2.getTrackbarPos("Sensitivity", "Motion Detector")

    _, thresh = cv2.threshold(blur, sensitivity, 255, cv2.THRESH_BINARY)
    
    # Morphological operations for smoothness
    kernel = np.ones((5,5), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=2)
    eroded = cv2.erode(dilated, kernel, iterations=1)

    contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False

    for contour in contours:
        if cv2.contourArea(contour) < 1500:
            continue

        motion_detected = True

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)

    # Status text
    status = "MOTION DETECTED" if motion_detected else "No Motion"
    color = (0,0,255) if motion_detected else (0,255,0)

    cv2.putText(frame1, status, (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Timestamp
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame1, time_now, (10,460),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)

    # FPS calculation
    current_time = datetime.now()
    fps = 1 / (current_time - prev_time).total_seconds()
    prev_time = current_time

    cv2.putText(frame1, f"FPS: {int(fps)}", (500,30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2)

    # Record when motion detected
    if motion_detected:
        out.write(frame1)

    # Show windows
    cv2.imshow("Motion Detector", frame1)
    cv2.imshow("Threshold", thresh)

    # Update frames
    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret:
        break

    # Controls
    key = cv2.waitKey(30)

    if key == 27:   # ESC to exit
        break
    elif key == ord('c'):   # Clear screen effect
        print("Screen cleared")

cap.release()
out.release()
cv2.destroyAllWindows()