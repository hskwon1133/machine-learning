#경계(밝기에 대한 변화량), 엣지
#중간에 노이즈가 있음, 잡티 제거 해주고
#엣지 잡아줌
#피처맨만드는 거, 특징 만든느 거 중요함
import cv2

# img = cv2.imread('./images/ryu.jpg', cv2.IMREAD_GRAYSCALE)
# img_resized = cv2.resize(img, (600, 400))

#Sobel
# SobelX = cv2.Sobel(img_resized, cv2.CV_64F, 1, 0, ksize=3) #64byte, ksize를 쓰는 이유? (커널사이즈)
# SobelY = cv2.Sobel(img_resized, cv2.CV_64F, 0, 1, ksize=3) #64byte, ksize를 쓰는 이유? (커널사이즈)
#
# SobelX = cv2.convertScaleAbs(SobelX)
# SobelY = cv2.convertScaleAbs(SobelY)
# sobelxy = cv2.addWeighted(SobelX, 1, SobelY, 1, 1, 0)
# sobelxy = cv2.GaussianBlur(sobelxy, (5, 5), 5)
#
# cv2.imshow('img', img)
# cv2.imshow('SobelX', SobelX)
# cv2.imshow('SobelY', SobelY)
# cv2.imshow('sobelxy', sobelxy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#Laplacian
# img = cv2.imread('./images/ryu.jpg', cv2.IMREAD_GRAYSCALE)
# img_resized = cv2.resize(img, (600, 400))
# img_resized = cv2.GaussianBlur(img_resized, (1, 1), 0)
#
# img_lap = cv2.Laplacian(img_resized, cv2.CV_64F, 0)
# img_lap = cv2.convertScaleAbs(img_lap)
#
# cv2.imshow('img_resized', img_resized)
# cv2.imshow('img_lap', img_lap)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#Canny
img = cv2.imread('./images/ryu2.png', cv2.IMREAD_GRAYSCALE)
img_resized = cv2.resize(img, (800, 600))
img_resized = cv2.GaussianBlur(img_resized, (5, 5), 0)

img_can = cv2.Canny(img_resized, 100, 1) #edge 조절시에 옵션 조절 필요

cv2.imshow('img_resized', img_resized)
cv2.imshow('img_can', img_can)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
