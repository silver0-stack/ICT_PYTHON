# namecard\\threshold_otsu.py
# 2단계 : 명함 이미지 이진화 처리를 위한 threshold 연산 다중 적용한 경우
'''Otsu 알고리즘을 활욯한 자동 임계값 이진화'''
"""
다수의 명함 이미지를 이진화하여 각 이미지의 Otsu 임계값을 계산하고 적용
자동으로 적절한 임계값을 선택하여 이진화 수행
"""

import sys
import cv2

filenames = ['../images/namecard1.jpg', '../images/namecard2.jpg', '../images/namecard3.jpg']

for filename in filenames:
    src = cv2.imread(filename, cv2.IMREAD_COLOR)   # BGR 로 읽음

    if src is None:
        print('Image file load failed!')
        sys.exit()

    src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
    # 이진화를 위해서 그레이스케일로 변환함
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # 이진화 처리
    th, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print('Threshold : ', th)

    cv2.imshow('src', src)
    cv2.imshow('src_gray', src_gray)
    cv2.imshow('src_bin', src_bin)
    cv2.waitKey()

cv2.destroyAllWindows()
