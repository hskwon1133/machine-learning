# 산술, 논리, 마스킹

# 산술
# 200 + 250 = 550 이미지끼리 더할 때 255를 넘어가면 overflow가 되어 0으로 돌아감 (연산에 모두 적용)
# 보통 이미지를 합치면 합성을 요구할 것임.

# 논리 (이산수학이 뭐임... 알아야함?)
# XOR ab가 숫자가 다를 때 true, xnor은 반대로 ab 숫자가 같을 때 true

# 마스킹
# 산술과 논리를 이용해서 마스킹 해라.


# 이미지 준비
import cv2
import numpy as np


# 산술
# a  = np.uint8([[250]]) # 2차원 하나만 입력시 1pixel짜리 이미지 하나 만들어짐.
# b =  np.uint8([[10]])
# # result = a+b
# # print(result) #260으로 overflow가 되어서 4로 출력. 256 = 0, 257=1, 258=2, 259=3, 260=4
# result = cv2.add(a,b)
# print(result) #최대값(225 도달시) : 포화 상태가 되어 멈춤.
#
# print(a)
# print(b)
#
# cv2.imshow('a',a)
# cv2.imshow('b',b)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#블렌딩

a = cv2.imread('./images/53.png')
# b = cv2.imread('./images/cosmos.jpg')
a = cv2.resize(a, (800,500), interpolation=cv2.INTER_AREA)
# b = cv2.resize(b, (800,500), interpolation=cv2.INTER_AREA)
#
# result = cv2.addWeighted(a,0.8, b,0.2,0.5) #사진1, 사진1가중치, 사진2, 사진2가중치, 전체밝기보정값(명도)
# # 알파, 베타 조절 하면 +는 밝아지고, -는 어두어짐(명도인가?, 근데 뭔가 필름처럼 어두어짐.. 이거 알려줘)
#
# cv2.imshow('result',result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#비트연산
# a = cv2.imread('./images/53.png', cv2.IMREAD_GRAYSCALE)
# b = cv2.imread('./images/cosmos.jpg', cv2.IMREAD_GRAYSCALE)
# a = cv2.resize(a, (800,500), interpolation=cv2.INTER_AREA)
# b = cv2.resize(b, (800,500), interpolation=cv2.INTER_AREA)
# # 논리연산을 썼을때 255를 넘는 경우 과하게 흑백 결과가 도출됨. (사유 설명 부탁)
# # 흰색, 검정색으로 나눠서 자르기 위함.
# # result_and = cv2.bitwise_and(a,b)
# result_and = cv2.bitwise_not(a)
# cv2.imshow('result',result_and)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#마스킹
#마스크 : 값이 0 또는 255인 흑백이미지(opencv에서만)
mask = np.zeros([500,800], np.uint8)

w = mask.shape[0]
h = mask.shape[1]
center = (h//2, w//2)
#start_point랑 end_point를 구하는 연산 방법 알려줘
start_point = (100,100)
end_point = (700,400)

cv2.circle(mask,center,250,255,-1)  #이미지, 중심점, 반지름, 색, 선두께 # mask 이미지를, 정중앙에 센터를 잡고, 반지를 100으로 흰색 원을 채워줘.
cv2.rectangle(mask, start_point, end_point, 255, -1)

result = cv2.bitwise_and(a,mask)

cv2.imshow('a',a)
cv2.imshow('mask',mask)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()



