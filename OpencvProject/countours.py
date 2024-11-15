# namecard\\countours.py
# 3단계 : 명함 이미지 외곽선 추출

import numpy as np
import sys
import cv2
import random

src = cv2.imread('../images/namecard1.jpg')
print(src.shape)  # (810, 1080, 3)

if src is None:
    print('Error')
    sys.exit()

# 이미지 크기 줄이기
src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
# 이진화를 위해서 그레이스케일로 변환함
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 이미지 가로, 세로를 행렬로 변환
h, w = src.shape[:2]
# 레이블링과 외곽선 저장용 3차원 행렬 만들기
dst1 = np.zeros((h, w, 3), np.uint8)  # 각 픽셀에 기록할 숫자의 자료형 1바이트 비부호정수로 정함, 기본 0으로 채워짐
dst2 = np.zeros((h, w, 3), np.uint8)

# 이진화 처리
th, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 외곽선 검출 : 모드를 다르게 해서 2가지 출력 확인
countour1, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
countour2, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# 외곽선 그리기
'''
for i in range(len(countour1)):
    # 랜덤하게 rgb 색 만듦
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst1, countour1, i, random_color, 1)  # 테두리선 그리기

for i in range(len(countour2)):
    # 랜덤하게 rgb 색 만듦
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst2, countour2, i, random_color, 1)  # 테두리선 그리기
'''

# 외곽선 그리기 & 좌표값 추출
for i in range(len(countour1)):
    pts = countour1[i]
    # print('pts : ', pts)  # 외곽선 좌표값 확인
    
    # 랜덤하게 rgb 색 만듦
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst1, countour1, i, random_color, 1)  # 테두리선 그리기

    # 면적이 너무 작은 객체는 제외시킴
    if cv2.contourArea(pts) < 1000:
        continue  # 아래 내용 실행하지 말고 다음 인덱스의 외곽선으로 넘어가라. 위로 올라감

    # 외곽선 근사화 : 0.02 오차 범위 지정
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
    # print(approx)

    # 컨벡스(닫혀진 다각형)가 아니면 제외
    if not cv2.isContourConvex(approx):
        continue

    # 4각형이면 외곽선 그리기
    if len(approx) == 4:
        cv2.drawContours(dst2, countour1, i, random_color, 2)
        # 좌표값 추출
        extLeft = tuple(pts[pts[:, :, 0].argmin()][0])
        extRight = tuple(pts[pts[:, :, 0].argmax()][0])
        extTop = tuple(pts[pts[:, :, 1].argmin()][0])
        extBottom = tuple(pts[pts[:, :, 1].argmax()][0])
        print('좌표값 : ', extLeft, extRight, extTop, extBottom)
# for close -----------------------------------------

# 각 단계별 이미지 처리 결과 확인
cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()



