import cv2
import numpy as np

# 카메라 연결
cap=cv2.VideoCapture(0)

# 초기 배경 초기화
ret, frame = cap.read()
if not ret:
    print("카메라에서 프레임을 읽을 수 없습니다.")
    cap.release() # 카메라 장치 해제 함수: 시스템 리소스 해제해여 카메라를 다른 프로그램에서 사용할 수 있도록
    exit()

# 첫 번쨰 프레임을 그레이스케일로 저장
background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
background=cv2.GaussianBlur(background, (21, 21), 0)

print("q를 눌러 종료하세요.")

while True:
    # 현재 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 현재 프레임 그레이스케일 변환 및 블러 처리
    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame=cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # 배경과 현재 프레임의 차이 계산
    frame_diff = cv2.absdiff(background, gray_frame)

    # 차이를 이진화(Threshold)
    _, thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)

    # 팽창(Dilation)으로 노이즈 제거
    thresh=cv2.dilate(thresh, None, iterations=2)

    # 윤곽선 찾기
    contours, _=cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 윤곽선 그리기 및 모션 감지 영역 표시
    for contour in contours:
        if cv2.contourArea(contour)<500: # 너무 작은 움직임은 무시
            continue
        x, y, w, h=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w,y+h), (0, 255, 0),2)

    # 프레임 출력
    cv2.imshow('Motion Detection', frame)
    cv2.imshow("Threshold", thresh)

    # q를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()

