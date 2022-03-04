import cv2 as cv
import numpy as np

# 1. 이미지 읽기
img = cv.imread("./img/kitech.jpeg")

# 2-1. 픽셀로 직접 크기 수정 : interpolation=cv.INTER_AREA
#img_resize = cv.resize(img, dsize=(500, 500), interpolation=cv.INTER_AREA)

# 2-2. 비율로 크기 수정 : interpolation=cv.INTER_LINEAR
img_resize = cv.resize(img, dsize=(0,0), fx=10, fy=10, interpolation=cv.INTER_LINEAR)

# 3. BGR 색 추출
bgrLower = np.array([102, 255, 255])    # 하한
bgrUpper = np.array([102, 255, 255])    # 상한

# 4. BGR로부터 마스크 작성
img_mask = cv.inRange(img_resize, bgrLower, bgrUpper)

# 5. 원본 이미지와 마스크 합성
result = cv.bitwise_and(img_resize, img_resize, mask=img_mask)

# 해당 이미지 출력
cv.imshow("image title", result)
print(result)

print("connected")

# 아무 키나 누르면 닫김
cv.waitKey(0)

cv.destroyAllWindows()

print("Bye")