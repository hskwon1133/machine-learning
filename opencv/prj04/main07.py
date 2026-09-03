# 필터링, 블러링
# 커널을 이용해서.. 합성곱..?
# 블러닝은 샤프에 따라서 뭐가 가능하고?


import cv2
import numpy as np

# img = cv2.imread('./images/street_midnight.jpg')
# img_re  = cv2.resize(img,(600,800), interpolation = cv2.INTER_AREA)

# img_blur = cv2.blur(img_re,(5,5))  # 커널 사이즈가 클수록 블러가 더 크게 일어남
# img_blur_g = cv2.GaussianBlur(img_blur,(5,5),0) #시그마를 키워주면 블러가 더 크게 일어남. 제일 많이 씀
# img_blur_m = cv2.medianBlur(img_blur,5) # 중앙값을 가져오려면 kernal 사이즈 홀수
# img_blur_b = cv2.bilateralFilter(img_blur,5,100,100) # 지름 5, 주변 색상이 얼마나 비슷함?,
# k = np.array([[0,-1,0]
#                 ,[-1,5,-1]
#                  ,[0,-1,0]])
# img_k = cv2.filter2D(img_re,-1,k) #필터링
#
# cv2.imshow('img', img_re)
# cv2.imshow('img_blur', img_blur)
# cv2.imshow('img_blur_g', img_blur_g) # 주변 픽셀을 가져와서 가중치를 가져와서 평균구해서 채워주기
# cv2.imshow('img_blur_m', img_blur_m) # 주변 픽셀 가져와서 중앙값 가져와서 채워주기
# cv2.imshow('img_blur_b', img_blur_b) # 설명 필요
# cv2.imshow('img_k', img_k) # 설명 필요
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#====노이즈제거하기 ====
#소금, 후추 제거하기
rng = np.random.default_rng(seed=42)
img = np.full((500,500), 128, dtype=np.uint8)
xs = rng.integers(0,500,3000) #0~499사이 숫자를 3000개 정수로
ys = rng.integers(0,500,3000) #0~499사이 숫자를 3000개 정수로
noise = rng.integers(0,2,3000) #0~1사이 숫자를 3000개 정수로
# img[ys,xs] = 0 # 행렬에 넣기
#방법 1
# bool_arr = noise == 0
# img[ys,xs] = np.where(bool_arr, 0,250)

#방법 2
img[ys,xs] = np.where(noise, 0,250)
img_blur = cv2.blur(img,(5,5))
img_blur_m = cv2.medianBlur(img,3)
img_blur_g = cv2.GaussianBlur(img,(3,3),0)

cv2.imshow('img', img) # 설명 필요
cv2.imshow('img_blur', img_blur) # 설명 필요
cv2.imshow('img_blur_m', img_blur_m) # 설명 필요
cv2.imshow('img_blur_g', img_blur_g) # 설명 필요
cv2.waitKey(0)
cv2.destroyAllWindows()
