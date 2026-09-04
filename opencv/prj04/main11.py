#이미지 피라미드, 템플릿매칭
import cv2

img = cv2.imread('images/59.png')
temp_img = cv2.imread('images/60.png')
img = cv2.resize(img, (600, 600))

h = temp_img.shape[0]
w = temp_img.shape[1]

img_up = cv2.pyrUp(img)
img_down = cv2.pyrDown(img)

# 템플릿 매칭
result = cv2.matchTemplate(img, temp_img, cv2.TM_CCOEFF_NORMED) #TM_CCOEFF_NORMED은 매칭이 높을 수록 좋음(max)/ 뭘로봐야 낮은게 좋음?(min), type = numpy
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) #min, max location

top_left = max_loc  #좌측 상단 시작점
bottom_right = (top_left[0] + w, top_left[1] + h)  #위치 못찾음 ^^
cv2.rectangle(img, top_left, min_loc, (50, 50, 50), 3)


cv2.imshow('img', img)
# cv2.imshow('imgup', img_up)
# cv2.imshow('imgdown', img_down)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()