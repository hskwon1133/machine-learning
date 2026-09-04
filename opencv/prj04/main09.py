#모폴로지 연산
#이진화 처리해서 특정 인덱값으로 넘어가거나 낮으면 어찌 처릴 하겠다.
#침식(노이즈를 깍는 거)/ 팽창(끊어진부분을 잇는거)
import cv2
import numpy as np

# 이미지 준비
img = np.zeros((300,300), np.uint8)
x,y = img.shape
center = (x//2, y//2)
squ_str = ((center[0]//2), (center[1]//2))
squ_end = (squ_str[0]+center[0], squ_str[1]+center[1])
circle_st = (squ_str[0]//2, squ_str[1]//2)

cv2.rectangle(img, squ_str, squ_end, (255,255,255), -1)
cv2.circle(img, center, 5, (0,0,0), -1)
cv2.circle(img, circle_st, 5, (255,255,255), -1)

#모폴로지
kn = np.ones((5,5), np.uint8)
# result_e = cv2.erode(img, kn, iterations=5) #흰색이 침식됨.
# result_d = cv2.dilate(img, kn, iterations=5) #흰색 팽창됨.

#침식 -> 팽창 : Open 침식을 당하면서 작아졌다가 작아진 크기가 팽창하면서 다듬어진 모양의 결과물이 나옴
#팽창 -> 침식 : Close
img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kn)
img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kn)
img_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kn) # 윤곽선 나옴

cv2.imshow('img', img)
cv2.imshow('img_open', img_open)
cv2.imshow('img_close', img_close)
cv2.imshow('img_gradient', img_gradient)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
