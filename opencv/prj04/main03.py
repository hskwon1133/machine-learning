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

# a = cv2.imread('./images/53.png')
# # b = cv2.imread('./images/cosmos.jpg')
# a = cv2.resize(a, (800,500), interpolation=cv2.INTER_AREA)
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

#마스킹 : 이거 포토샵에서 누끼 따는 거 아님? ㅋㅋ
#흑백 마스크 : 값이 0 또는 255인 흑백이미지(opencv에서만)
# mask = np.zeros([500,800], np.uint8)
#
# w = mask.shape[0]
# h = mask.shape[1]
# center = (h//2, w//2)
# #start_point랑 end_point를 구하는 연산 방법 알려줘
# start_point = (100,100)
# end_point = (700,400)
#
# cv2.circle(mask,center,250,255,-1)  #이미지, 중심점, 반지름, 색, 선두께 # mask 이미지를, 정중앙에 센터를 잡고, 반지를 100으로 흰색 원을 채워줘.
# cv2.rectangle(mask, start_point, end_point, 255, -1)
#
# result = cv2.bitwise_and(a,mask) # a와 mask의 shape이 동일해야 함.
# result1 = cv2.bitwise_and(a,a,mask=mask) #mask를 쓰면 a라는 이미지는 컬러도 가능. mask를 통과하는 것만 사진 노출. parmeter mask를 써서 적용 요청. 해당 명령 내용을 설명해줘.
#
# cv2.imshow('a',a)
# cv2.imshow('mask',mask)
# cv2.imshow('result',result)
# cv2.imshow('result1',result1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 색(HSV = 색상, 채도, 명도) 마스크
# rgb = cv2.imread('images/rgb.jpg')
# rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)


# rgb = cv2.imread('images/31.jpg')
# rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
# lower = np.array([0, 0, 0])
# upper = np.array([0, 255, 0])
# mask = cv2.inRange(rgb, lower, upper) #target, lower하한값, upper상한값
# result = cv2.bitwise_and(rgb, rgb, mask=mask)
# 이 결과값은 초록색을 살리려고 하였지만, HSV 기준에서는 그린이 아님.

img_bgr = cv2.imread('images/31.jpg')
img_bgr = cv2.resize(img_bgr, (500, 500), interpolation=cv2.INTER_AREA) #가로, 세로
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

lower = np.array([36, 22, 23])
upper = np.array([110, 255, 255])
mask = cv2.inRange(img_hsv, lower, upper) #target, lower하한값, upper상한값
mask_2 = cv2.bitwise_not(mask)
result = cv2.bitwise_and(img_bgr, img_bgr, mask=mask)
result1 = cv2.bitwise_and(img_bgr, img_bgr, mask=mask_2)
# RGB의 경우 예를 들어 주황색을 찾기가 어려움, 근데 HSV는 찾기 쉬움.
# 사이트(http://pseudopencv.site/utilities/hsvcolormask/) 내에 파일을 넣어서 HSV 조절하면 range 코드 생성됨.
# HSV를 활용해서 mask 만들기

cv2.imshow('img_bgr and img_bgr', result)
cv2.imshow('not', result1)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 흑백은 채널1, 컬러는 채널3
# 이미지는 8비트이기 떄문에 RGB, BGR은 0~255까지. uint8 형식이어야함
# 색상정보는 후에 HSV로 볼거임
# BGR, RGB, HSV .. 컬러에 대한 종류는 이게 다임?
# 기하학 변경은 데이터 증감을 위해서
