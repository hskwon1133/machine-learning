import cv2

# 이미지 불러와서 작업 후 저장하기
# img = cv2.imread('images/53.png', cv2.IMREAD_COLOR)
#
# print(img) # image가 none일수록 방어가 가능하면 더 좋음. 필요하면 'img가 none이면 예외처리 명령
# print(img.shape)
# cv2.imshow('img', img)
# cv2.waitKey(0) # 0이면 무한대, 3000은 3000초
# cv2.destroyAllWindows()
# cv2.imwrite('images/result.png', img)

# 비디오 불러와서 작업 후 저장하기
cap = cv2.VideoCapture('videos/0.mp4') #webcam도 가능, 노트북 카메라로 가능.
fps = cap.get(cv2.CAP_PROP_FPS) # FPS : Frame per Seconds
# print(cap)
# print(type(cap))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #너비
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #높이

fourcc = cv2.VideoWriter_fourcc(*'mp4v') # 코덱
out = cv2.VideoWriter('videos/result.mp4', fourcc, fps, (w, h)) #param : 경로, 코덱, (너비, 높이)


is_read, frame = cap.read() #프레임 하나씩 불러옴.
# print(is_read)
# print(frame)
# print(type(is_read)) #사진을 잘 읽어옴
# print(type(frame))
# print(frame.shape)

cnt = 0
delay = int(1000 / fps)
while True :
    cnt += 1
    is_read, frame = cap.read()
    if not is_read: break
    cv2.imshow('dd', frame)
    cv2.waitKey(delay)

    #영상으로 저장
    if cnt % 2 == 0 :
        out.write(frame)

out.release() # out 매개도 해제
cap.release() # 다 실행했음 자원을 놓아줘
cv2.destroyAllWindows()

#Frame 너비, 높이 가져와 볼 수 있음