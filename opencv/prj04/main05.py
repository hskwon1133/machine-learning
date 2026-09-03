import cv2
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 밝기, 대비
# 히스토그램으로 값이 분포도를 보고 밝기 상태 진단
# 컬러
# img = cv2.imread('./images/53.png')
# img_resized = cv2.resize(img,None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
# img_abs = cv2.convertScaleAbs(img_resized,alpha=1.5,beta=-90) #수동조절 : alpha = 대비, beta = 밝기조절
#
# # 흑백
# img_gray = cv2.imread('./images/53.png', cv2.IMREAD_GRAYSCALE)
# img_gray_resized = cv2.resize(img_gray,None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
#
# img_gray_eq = cv2.equalizeHist(img_gray_resized) #흑백일때만 쓸 수 있음. equlizeHist, 채널이 한개 일때만 가능
# img_gray_abs = cv2.convertScaleAbs(img_gray_resized,alpha=1.5,beta=-90) #수동조절 : alpha = 대비, beta = 밝기조절
# hist = cv2.calcHist([img_gray],[0],None,[256],[0,256]) #mask 해당위치만 처리. histSize = bins, ranges = 값의 범위 0~255
#
#
# # 50 미만, 220이상의 값이 없어 scales 범위를 넓여 히스토그램 분포를 봄
# # beta -50을 주면, 50미만 쪽의 분포가 늘고 190이상의 범위가 없음
# # alpha = 1.5, beta = -90 밝기 조절이 잘된다는 걸 고루분포가 되는지로 확인해서 조절 가능
# #
# # plt.plot(hist)
# # plt.show()
#
#
#
# cv2.imshow('img',img_resized) #img 사이즈 조정 결과 출력
# cv2.imshow('img_abs',img_abs) # img 사이즈 수정 사진에 대비, 밝기 조절 조정 결과 출력
# cv2.imshow('img_gray',img_gray_resized) # 흑백사진 사이즈 조정 결과 출력
# cv2.imshow('img_gray_abs',img_gray_abs) # 흑백사진 사이즈 조정 결과 출력
# cv2.imshow('gray_auto_eq',img_gray_eq) # 흑백 사이즈 조정 사진 자동으로 이퀄라이징해서 출력
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#컬러만 가져오기. 위에 스크립트가 배우는 데 해깔릴 수 있어서 아래에서 따로 배움.

# img = cv2.imread('./images/53.png')
# # img_resized = cv2.resize(img,None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)
# img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb) #HSV도 가능 V=명도 , YCrCb y = 0, cr = 1, cb=2
# img_ycrcb[:,:,0] = cv2.equalizeHist(img_ycrcb[:,:,0])
# result = cv2.cvtColor(img_ycrcb, cv2.COLOR_YCrCb2BGR)
#
# cv2.imshow('result',result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# CLAHE : 지역적응력평활화

gray = np.random.randint(90,160,(300,300), dtype='uint8')
gray[:,0:150]=gray[:,0:150]*0.5

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) #cliblimit가 커질 수록 평탄화가 잘 됨. 한장의 이미지를 쪼개서 볼 수 있음
result = clahe.apply(gray)

result_1 = cv2.equalizeHist(result, gray)

cv2.imshow('gray',gray)
cv2.imshow('result',result)
cv2.imshow('result_1',result_1)
cv2.waitKey(0)
cv2.destroyAllWindows()





























