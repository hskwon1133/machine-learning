#이진화, 임계처리

import cv2

img_gray = cv2.imread('./images/kitty.png',cv2.IMREAD_GRAYSCALE)
img_gray_rs = cv2.resize(img_gray,(500,500), interpolation = cv2.INTER_AREA)

# === 전역 임계처리 ===
# a, b = cv2.threshold(img_gray_rs,200,250,cv2.THRESH_BINARY) #어떤 타입으로 나눌지 (여러 타입 있음), 흑백으로 나눠줌. 기준값(127)보다 크면 255로 하겠다.
# a, b = cv2.threshold(img_gray_rs,200,250,cv2.THRESH_BINARY_INV) #어떤 타입으로 나눌지 - 반대
# a, b = cv2.threshold(img_gray_rs,200,250,cv2.THRESH_TRUNC) #어떤 타입으로 나눌지 - 200보다 크면 다 200
# a, b = cv2.threshold(img_gray_rs,200,250,cv2.THRESH_TOZERO) #어떤 타입으로 나눌지 - 200보다 크면 ZERO

# a, b = cv2.threshold(img_gray_rs,200,250,cv2.THRESH_BINARY+cv2.THRESH_OTSU) #어떤 타입으로 나눌지 (여러 타입 있음), 흑백으로 나눠줌. 기준값(127)보다 크면 255로 하겠다.

# print(a)
# cv2.imshow('img_gray_rs',img_gray_rs)
# cv2.imshow('b',b)

# === 적응력 임계처리 ===

result = cv2.adaptiveThreshold(
    img_gray_rs
    , 255
    , cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    , cv2.THRESH_BINARY
    , 11
    , 0
                      )
#이미지, 계산방식, 처리방식, 주변영역크기, 상수
#기준값보다 크면 255로 보내, 단 주변...뭐라고..? 비해 가우시안방식으로 해줘.
#
# cv2.imshow('result',result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
