import numpy as np
import cv2
import pyautogui as m
import sys
import time

k = 1
user_input = input('This application recognizes your face and eye using the trained data model sets'
                   '\n It detects eye blink and handles mouse click event\n Press 1 to start the program. '
                   '\n\n To stop the program bring back the window that records the eye movement,cover your camera and press Q ')

face_cascade = cv2.CascadeClassifier('C:\....\haarcascade_frontalface_default.xml')#Replace this with the path where you reside the file
eye_cascade = cv2.CascadeClassifier('C:\....\haarcascade_eye.xml')#Replace this with the path where you reside the file
cap = cv2.VideoCapture(0)
# Change these parameters to play with sensitivity
c1 = 7
c2 = 5
if user_input == 1:
    while (True):
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            k = 1
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            u1 = x + w
            u2 = y + h
            cir = cv2.circle(img, (x + w / 2, y + h / 2), 1, (0, 255, 255), 2)
            # print x + w / 2, y + h / 2
            #The below code is responsible for moving the mouse cursor in near real-time. Uncomment the below line to test it out.
            # m.moveTo(c1 * x + w / 2, c2 * y + h / 2, 0)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                k = 0
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)

        if k == 1:
            print "Blink"
            # The below snippet is responsible for mouse click events. At the moment this is would work but still needs enhancements
            # uncomment the below to enable mouse left click events.
            # m.click()
        if k == 0:
            print "No Blink"
        cv2.namedWindow("img", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("img", 600, 450)
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print "Oops you pressed the wrong key try restarting the application again"
