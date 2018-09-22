import cv2
import numpy as np
#How to capture video from Camera
#Converts BGR to RGBA (Blue -> Red, Red->Blue)

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    cv2.imshow('frame',converted)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()