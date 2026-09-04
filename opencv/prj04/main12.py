# 특징 검출 및 매칭
# 특징점 : 주변과 구별되는 위치
# 디스크립터 : 특징점 주변 모양 요약 (숫자벡터)

#이진화, 블러, 리사이즈, 오플로드 등의 전처리 후 윤곽따고, 분리하고 알고리즘으로 특징점 찾기. (사실 2줄로 합쳐진다함 main01.py ~ main12.py)
import cv2

img_gray = cv2.imread('images/59.png', cv2.IMREAD_GRAYSCALE)
template = cv2.imread('images/60.png', cv2.IMREAD_GRAYSCALE)


# 코너검출
# result = cv2.cornerHarris(img_gray,2,3,0.04)
# print(img_gray.shape)
# print(result.shape) #image, result shape 같음 / numpy / 숫자가 작으면 코너가 아니다.  k값이 작을 수록 코너를 더 잘 검출해줌


# 특징점, 디스크립터 (무료버전 알고리즘 쓰기)
# sift, orb 각각의 알고리즘을 통해서 처리 가능
# orb가 속도가 빠르고 sift가 정확도가 높음.

# sift = cv2.SIFT_create()
# kp, des = sift.detectAndCompute(img_gray, None)
# print(type(sift)) #<class 'cv2.SIFT'>


# orb = cv2.ORB_create()
# kp, des = orb.detectAndCompute(img_gray, None)
# print(type(kp)) # <class 'tuple'>
# print(type(des)) # numpy
# print(kp) # keypoint
# print(des) #description 어떤 정보를 숫자로 표현
# result = cv2.drawKeypoints(img_gray, kp, None)# flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS

# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img_gray, None)
kp2, des2 = orb.detectAndCompute(template, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = bf.knnMatch(des1, des2, k=2) #k는 가장 닮은 점 2개 골라줘

# print(len(good))
# print(len(matches))
# print(len(des1))
# print(len(des2))

# concept을 이해하기 위함
good = []
for pair in matches:
    if len(pair) != 2: continue
    a,b = pair
    if a.distance < b.distance * 0.75 :
        good.append(a)

result = cv2.drawMatches(img_gray, kp1, template, kp2, good, None, flags = 2) #이미지1, 키포인트1, 이미지2, 키포인트2,굿배열, None, flags =2


cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

