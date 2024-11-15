# namecard\\perspective.py
# 4 단계 : 명함이미지에서 외곽선 추출 후 외곽선 도형 모양 변형 처리 (명함을 반듯한 사각형 만들기함)
""" 투시 변환 (Perspective Transformation)
검출된 외곽선을 기준으로 명함을 평면(사각형)으로 변환하여 기울어짐을 보정함
"""

import numpy as np
import sys
import cv2

src = cv2.imread('../images/namecard1.jpg')
print(src.shape)  # (810, 1080, 3)

if src is None:
    print('Error')
    sys.exit()

w, h = 720, 400   # 결과로 만들 명함 크기 지정함
# 정해진 사각형 크기에 대한 행렬(매트릭스) 만들기  : 외곽선 추출로 명함의 위치를 가지고 행렬을 만듦)
srcQuad = np.array([[325, 307], [760,369], [718, 611], [231, 515]], np.float32)
dstQuad = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()