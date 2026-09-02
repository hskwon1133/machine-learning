# 기하학 변화
import cv2
import numpy as np


img = cv2.imread('./images/53.png')
# print(img.shape) # (1086, 1448, 3)


# 크기조절 : cv2.resize
img = cv2.resize(img, (800, 500)) #가로*세로
# img = cv2.resize(img, None, fx=0.5, fy=0.5) #둘 중 뭘 지양해?
#inter_linear 쌍선형. 기본값. 값을 추출해서 채워주는 방식 설명좀.

# 뒤집기 (좌우=1, 상하=0, 상하좌우 = -1 반전)
# img = cv2.flip(img, 0)

# 이동 (원래 자리 가도 검정색 화면이 노출)
# x = 100
# y = 100
# matrix = np.float32([[1,0,x],[0,1,y]])
# img = cv2.warpAffine(img, matrix,(800,500))
# img = cv2.warpAffine(img, matrix,(-400,500))

# 회전
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE ) #시계방향 90도
# img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE ) #반시계방향 90도
# img = cv2.rotate(img, cv2.ROTATE_180) #180도

# 회전 자유롭게. 중심점(center) 잡고 회전 가능
w = img.shape[1]
h = img.shape[0]
c = (w//2, h//2)
matrix = cv2.getRotationMatrix2D(c, 30.0, 1.0) #center, angle, scale = float type
img = cv2.warpAffine(img, matrix, (w, h))  #반시계 방향으로 회전이 가능


cv2.imshow('img',img)
cv2.waitKey(0)
