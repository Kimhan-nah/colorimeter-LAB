import cv2 as cv
from cv2 import moveWindow
import numpy as np
from matplotlib import pyplot as plt

# 관심영역 설정 
isDragging = False      # 마우스 드래그 상태
x0, y0, w, h = -1, -1, -1, -1       # 영역 선택 좌표 저장
blue, red = (255, 0, 0), (0, 0, 255)
 
# 마우스 이벤트 핸들 함수
def onMouse(event, x, y, flags, param):
    global isDragging, x0, y0, img      # 전역변수 참조
    if event == cv.EVENT_LBUTTONDOWN:   # 왼쪽 버튼 다운 -> 드래그 시작
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv.EVENT_MOUSEMOVE:   # 마우스 움직임
        if isDragging:                  # 드래그 진행
            img_draw = img.copy()
            cv.rectangle(img_draw, (x0, y0), (x, y), red, 2)
            cv.imshow('draw img', img_draw)
            cv.moveWindow('draw img', 200, 200)
    elif event == cv.EVENT_LBUTTONUP:   # 왼쪽 마우스 업
        if isDragging:                  # 드래그 중지
            isDragging = False
            w = x - x0
            h = y - y0
            if w > 0 and h > 0:         # 가능한 영역이라면
                # img_draw = img.copy() 
                # cv.rectangle(img_draw, (x0, y0), (x, y), red, 2)    # 선택 영역에 빨간 사각형 표시
                # cv.imshow('img', img_draw)      # 빨간 사각형 그려진 이미지 화면 출력
                roi = img[y0:y0+h, x0:x0+w]     # 원본 이미지에서 선택 영여만 ROI 지정
                cv.imshow('cropped', roi)
                cv.moveWindow('cropped', 200, 200)
                # cv.imwrite('./cropped.png', roi)  # 파일 저장
                print("croped.")
                cv.destroyWindow("img title")   # 첫 생성 윈도우 창 닫기
                cv.destroyWindow("draw img")
            else:
                cv.imshow('img', img)
                print('drag should start from left-top side')
 

# 이미지 읽기
img = cv.imread("./img/kitech.jpeg")

# 이미지 크기 조절 (비율)
# img_resize = cv.resize(img, dsize=(0,0), fx=10, fy=10, interpolation=cv.INTER_LINEAR)


# 해당 이미지 출력
cv.imshow("img title", img)
# 윈도우 창 위치 이동
cv.moveWindow("img title", 200, 200)
print("connected")
# 마우스 이벤트 등록
cv.setMouseCallback("img title", onMouse)

# 아무 키나 누르면 닫김
cv.waitKey()
cv.destroyAllWindows()

print("Bye")