import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('lH', 'image', 0, 255, nothing)
cv2.createTrackbar('lS', 'image', 0, 255, nothing)
cv2.createTrackbar('lV', 'image', 0, 255, nothing)
cv2.createTrackbar('hH', 'image', 0, 255, nothing)
cv2.createTrackbar('hS', 'image', 0, 255, nothing)
cv2.createTrackbar('hV', 'image', 0, 255, nothing)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lH = cv2.getTrackbarPos('lH', 'image')
    lS = cv2.getTrackbarPos('lS', 'image')
    lV = cv2.getTrackbarPos('lV', 'image')
    hH = cv2.getTrackbarPos('hH', 'image')
    hS = cv2.getTrackbarPos('hS', 'image')
    hV = cv2.getTrackbarPos('hV', 'image')
    low = np.array([lH,lS,lV])
    high = np.array([hH,hS,hV])
    mask1 = cv2.inRange(hsvFrame, low, high)
    cv2.imshow('frame',mask1)
    if(cv2.waitKey(1)==27):
        break
