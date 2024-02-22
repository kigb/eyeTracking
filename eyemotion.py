import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:#if the key is esc, then quit
        break

cap.release()
cv2.destroyAllWindows()