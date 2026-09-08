# 이미지의 특징 추출
# 이미지를 1차원으로 만들어 주기 위해서 이미지의 feature를 만들어 줄 것임.
# 질감, 색상, 형태 모두 가능. 색상만 시도해볼 것임

import numpy as np
import cv2

img = np.zeros((100,100,3), dtype=np.uint8)

img[:,:] = (100,255,30) #모든 픽셀은 연두색으로 바꿔줌

hist_b = cv2.calcHist([img],[0],None,[8],[0,256]) #100 = img, 0번채널에 동작하게, mask 없이, histogram size 8개 구간별, range = 0~256
hist_g = cv2.calcHist([img],[1],None,[8],[0,256]) #255 = img, 0번채널에 동작하게, mask 없이, histogram size 8개 구간별, range = 0~256
hist_r = cv2.calcHist([img],[2],None,[8],[0,256]) #30 = img, 0번채널에 동작하게, mask 없이, histogram size 8개 구간별, range = 0~256

# 출력사 10000 표기의 방향이 오른쪽으로 갈수록 색의 강함을 판단할 수 있음. 위의 hist는 그린이 높음을 시사함.

# print(hist_b)
# print(hist_g)
# print(hist_r)

# 3의 배열을 합치기 (concat)
result = np.concatenate((hist_b,hist_g,hist_r)) # 일차원 배열로 특징 학습 가능
print(result.shape)
print(result)
