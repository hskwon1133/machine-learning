import cv2
import numpy as np

img_bgr = cv2.imread('images/lovely.jpg')
green = cv2.imread('images/green.png')
img_bgr = cv2.resize(img_bgr, (500, 500))
green = cv2.resize(green, (500, 500))
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

lower = np.array([0, 100, 100])
upper = np.array([10, 255, 255])

cv2.inRange(img_hsv, green, green)


cv2.imshow('img', img_bgr)
cv2.imshow('img_hsv', img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()