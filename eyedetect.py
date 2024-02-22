import cv2#opencv python
import dlib
from math import hypot
import math
import numpy as np

def distance_between_landmarks(n1, n2, n3, n4, landmarks):
    x1 = landmarks.part(n1).x
    y1 = landmarks.part(n1).y
    x2 = landmarks.part(n2).x
    y2 = landmarks.part(n2).y
    x3 = landmarks.part(n3).x
    y3 = landmarks.part(n3).y
    x4 = landmarks.part(n4).x
    y4 = landmarks.part(n4).y
    
    x_mid, y_mid = (x1 + x2) / 2, (y1 + y2) / 2
    x_mid2, y_mid2 = (x3 + x4) / 2, (y3 + y4) / 2
    
    return math.hypot(x_mid2 - x_mid, y_mid2 - y_mid)


detect = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detect(gray)
    
    #(0,0,0) 0-255 red green blue
    for face in faces:

        landmarks = predictor(gray,face)
        
        #36-39, 42-45
        left_row_length = hypot((landmarks.part(36).x-landmarks.part(39).x),(landmarks.part(36).y-landmarks.part(39).y))
        right_row_length = hypot((landmarks.part(42).x-landmarks.part(45).x),(landmarks.part(42).y-landmarks.part(45).y))
        left_col_length = distance_between_landmarks(37,38,40,41,landmarks)
        right_col_length = distance_between_landmarks(43,44,46,47,landmarks)
        middle_ratio = (left_row_length/left_col_length+right_row_length/right_col_length)/2
        if middle_ratio>5:
            cv2.putText(frame,"blinking",(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))

        left_eye_region = np.array([(landmarks.part(36).x, landmarks.part(36).y),
                            (landmarks.part(37).x, landmarks.part(37).y),
                            (landmarks.part(38).x, landmarks.part(38).y),
                            (landmarks.part(39).x, landmarks.part(39).y),
                            (landmarks.part(40).x, landmarks.part(40).y),
                            (landmarks.part(41).x, landmarks.part(41).y)], np.int32)
        height, width, _ = frame.shape
        mask = np.zeros((height, width), np.uint8)
        cv2.polylines(mask, [left_eye_region], True, 255, 2)
        cv2.fillPoly(mask, [left_eye_region], 255)
        left_eye = cv2.bitwise_and(gray, gray, mask=mask)#& operation
        min_x = np.min(left_eye_region[:, 0])
        max_x = np.max(left_eye_region[:, 0])
        min_y = np.min(left_eye_region[:, 1])
        max_y = np.max(left_eye_region[:, 1])
        gray_eye = left_eye[min_y: max_y, min_x: max_x]
        _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
        threshold_eye = cv2.resize(threshold_eye, None, fx=5, fy=5)
        eye = cv2.resize(gray_eye, None, fx=5, fy=5)
        cv2.imshow("Eye", eye)
        cv2.imshow("Threshold", threshold_eye)
        cv2.imshow("Left eye", left_eye)
    #face vector<vector{float,float}> face[0]
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:#if the key is esc, then quit
        break

cap.release()
cv2.destroyAllWindows()