#허프변환

#cv2.HoughLinesP
#cv2.HoughCircles

import cv2
import numpy as np

img = cv2.imread('images/oriental1.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (500, 500))

edged = cv2.Canny(img, 240, 245)

lines = cv2.HoughLinesP(
    edged, # 경계선 검출
    rho=1,
    theta=3.14159/180, # template
    threshold=100, # 거리
    minLineLength = 50,
    maxLineGap = 20
)

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# 반복문 통해서 lines의 좌표 뽑기
if lines is not None :
    for x1,y1,x2,y2 in lines: #시작점 x1,y1 / 끝점 x2,y2
        cv2.line(img, (x1, y1), (x2, y2), (100, 255, 100), 3)



# 해당 이미지에 선을 그리다.?


cv2.imshow('img', img)
cv2.imshow('edged', edged)
cv2.waitKey(0)
cv2.destroyAllWindows()