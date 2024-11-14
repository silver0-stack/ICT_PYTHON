import cv2
from fer import FER

# 카메라 연결
cap = cv2.VideoCapture(0)
emotion_detector = FER(mtcnn=True)  # 표정 분석 모델

print("q를 눌러 종료하세요.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("카메라에서 프레임을 읽을 수 없습니다.")
        break

    # 좌우 반전 제거 (flipCode=1 -> 좌우반전)
    frame=cv2.flip(frame,1)


    # 얼굴 감지 및 표정 분석
    emotions = emotion_detector.detect_emotions(frame)
    for result in emotions:
        bounding_box = result['box']  # 얼굴 위치
        emotions = result['emotions']  # 감정 분석 결과
        dominant_emotion = max(emotions, key=emotions.get)

        # 얼굴 영역 표시
        x, y, w, h = bounding_box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # 비디오 출력
    cv2.imshow("Emotion Detector", frame)

    # q를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()