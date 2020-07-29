import cv2
import numpy as np


cap=cv2.VideoCapture(0)
back=cv2.imread('image.jpg')
while cap.isOpened():
    ret,frame=cap.read()

    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # cv2.imshow('hsv',hsv)
        red=np.uint8([[[0,0,0]]])   #bGR
        hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
        # print(hsv_red)
        l_red=np.array([100,100,100])
        r_red=np.array([255,255,255])

        mask=cv2.inRange(hsv,l_red,r_red)
        # cv2.imshow('mask',mask)
        part1=cv2.bitwise_and(back,back,mask=mask)
        # cv2.imshow('p', part1)
        mask=cv2.bitwise_not(mask)
        part2=cv2.bitwise_and(frame,frame,mask=mask)

        cv2.imshow('colck',part1+part2)

    if cv2.waitKey(5)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()