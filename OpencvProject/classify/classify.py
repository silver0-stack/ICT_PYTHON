# caffemodel에서 제공하는 학습된 ai 모델을 사용해서 사진에서 사물을 분류 처리하는
# 분류할 사물의 종류는 클래스파일에 이름이 100개 작성되어 제공되고 있음
# 구글에서 다운받음: ai 학습모델파일(.caffemodel), 구성파일(.prototxt), 클래스파일(class_... .txt) 3개

import numpy as np
import cv2
import sys

filename='space_shuttle.jpg'

#  실행 시 외부에서(명령 프롬프트| 터미널 | 파워쉘) 전달오는 인자(파일명.jpg)가 있다면
if len(sys.argv) > 1 : # 실행파일명 전달이자1 전달인자2 ...... 엔터
    filename = sys.argv[1]

img=cv2.imread(filename)
if img is None:
    print("Image load filed")
    sys.exit()

# ai 학습모델 laod
net = cv2.dnn.readNet('bvlc_googlenet.caffemodel', 'deploy.prototxt.txt')
