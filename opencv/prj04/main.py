import cv2

img = cv2.imread('images/53.png', cv2.IMREAD_GRAYSCALE) # Original 일 경우 shape(1086, 1448, 3) IMREAD_GRAYSCALE입력하면 채널은 없음 (1086, 1448)
# print(img.shape)

#잘라서 색을 바꿔봄
# roi  = img[0:100,0:100,:]
# roi[0:100, 0:100] = [0,255,0]
#
# print(roi.shape)

roi = img[550:900, 470:830] #컵만 자르기
img[0:350, 0:360] = roi # img에 roi넣기

cv2.imshow('roi',roi)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

