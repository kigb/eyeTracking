import cv2
import dlib
from math import hypot
cam = cv2.VideoCapture(0)
detect = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
while True:
    _, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detect(gray)

    for face in faces:
        # print(face)
        # cv2.rectangle(frame,(face.left(),face.top()),(face.right(),face.bottom()),(0,255,255),3)

        landmarks = predictor(gray,face)
        #use landmarks.part(x) to get the coordinate
        for p in range(36,42):#draw points from 36 - 41
            x = landmarks.part(p).x
            y = landmarks.part(p).y
            cv2.circle(frame,(x,y),3,(0,0,255),2)
        for p in range(42,48):
            x = landmarks.part(p).x
            y = landmarks.part(p).y
            cv2.circle(frame,(x,y),3,(0,0,255),2)
        cv2.line(frame,(landmarks.part(36).x,landmarks.part(36).y),(landmarks.part(39).x,landmarks.part(39).y),(0,0,255),2)


    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:#if the key is esc, then quitS
        break

cam.release()
cv2.destroyAllWindows()