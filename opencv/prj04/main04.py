# 그리기, 주석 (네모, 동그라미 외 선, 다각형 그리기)
import cv2
import numpy as np
from fontTools.cffLib import width

rgb_img = cv2.imread('images/rgb.png')

h,w  = rgb_img.shape[:2]
# start = rgb_img[0][0]
# end = rgb_img[-1][-1]
# print(rgb_img.shape)
center = (w//2, h//2)
#선
cv2.line(rgb_img,(0,0), (1152,648), [0,0,0], 5) #이미지, 시작, 끝, 색, 두께 => shape을 이용하면 좌표 찍기 쉬움
#원
cv2.circle(rgb_img,center,100,[255,255,255], 2)
#사각형
# cv2.rectangle(rgb_img,(100,100),(500,500),[0,0,0], 2)
cv2.rectangle(rgb_img,(200,200,500,500),[0,0,0], 2) #가로, 세로 사이즈를 한번에 잡아도 됨

#다각형  : cv2.polylines(이미지, 점들, 닫힘여부, 색상, 두께)
pts = np.array([
    [10,10]
    , [200,100]
    , [300,200]
    , [400,300]
    , [500,400]
])
pts = np.reshape(pts, (-1,1,2)) # -1 니가 갯수 알아서 처리해라
# cv2.polylines(rgb_img,[pts], isClosed = True, color=  (0,0,0), thickness= 10) #shape을 맞춰줘야함.
# cv2.fillPoly(rgb_img,[pts],(0,0,0)) #다각형 안을 채워줌

#텍스트 이미지, 텍스트, 위치, 폰트, 크기, 색, 굵기
# cv2.putText(rgb_img, 'Hello', (600,600), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0), 10) #cv2.FONT% 패턴으로 폰트 디자인 바꿀 수 있음, 한글의 두께는 바뀌지 않음


cv2.imshow('img', rgb_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()