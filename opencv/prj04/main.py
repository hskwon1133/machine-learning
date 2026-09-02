import cv2

img = cv2.imread('images/53.png')
print(img.shape)

#잘라서 색을 바꿔봄
roi  = img[0:100,0:100,:]
roi[0:100, 0:100] = [0,255,0]

print(roi.shape)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
