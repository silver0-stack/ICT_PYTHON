import cv2
from fer import FER

# 카메라 연결
cap = cv2.VideoCapture(0)
"""
cv2.VideoCapture(0): 카메라와 연결하는 함수
- 매개변수 0: 기본 카메라 선택
- 다른 외부 카메라를 연결할 경우 1, 2, 3 등의 번호를 사용
- 반환된 객체 'cap'을 사용하여 비디오 프레임 캡쳐
"""


emotion_detector = FER(mtcnn=True)  # 표정 분석 모델
"""
FER 라이브러리를 사용하여 표정 분석 모델 초기화
- FER(mtcnn=True): mtccn(Multi-task Cascaded Convolutional Networks) 모델을 사용해 얼굴 감지
- 표정 감지 및 분석을 위한 객체 생성
"""

print("q를 눌러 종료하세요.")
while True:
    ret, frame = cap.read()
    """
    cap.read(): 카메라로부터 비디오 프레임을 읽는 함수
    - ret: 프레임 읽기 성공 여부 (True/False 반환) 
    - frame: 읽어온 비디오 프레임 (이미지 데이터)
    - 프레임을 제대로 읽지 못한 경우 (ret이 False), 루프 종료
    """
    if not ret:
        print("카메라에서 프레임을 읽을 수 없습니다.")
        break

    # 좌우 반전 제거 (flipCode=1 -> 좌우반전)
    frame=cv2.flip(frame,1)
    """
    cv2.flip(): 이미지를 반전시키는 함수
    - 매개변수 1: 좌우 반전(거울 모드 제거)
    - 이 코드에서는 카메라 기본 설정으로 인해 반전된 이미지를 원래 상태로 되돌림
    """


    # 얼굴 감지 및 표정 분석
    emotions = emotion_detector.detect_emotions(frame)
    """
    emotion_detector.detect_emotions(frame): 프레임에서 얼굴을 감지하고 표정을 분석
    - frame: 현재 비디오 프레임
    - 반환값: 얼굴 감지 정보와 표정 분석 결과 (리스트 형태)
    """
    for result in emotions:
        """
        result: 감지된 얼굴 및 표정 데이터
        - result['box']: 얼굴 위치 정보 (x, y, w, h)
        - result['emotions']: 감지된 표정의 확률값
        """
        bounding_box = result['box']  # 얼굴 위치 정보 (x,  y, 너비, 높이)
        emotions = result['emotions']  # 표정 분석 결과 (각 표정의 확률값)
        dominant_emotion = max(emotions, key=emotions.get)
        """
        max(): 가장 높은 확률값을 가진 표정을 반환
        - emotions: 감지된 표정 데이터 딕셔너리
        - key=emotions.get: 확률값 기준으로 최댓값 찾기
        """



        # 얼굴 영역 표시
        x, y, w, h = bounding_box
        """
        얼굴 위치 데이터를 변수에 저장
        - x, y: 얼굴의 좌상단 좌표
        - w: 얼굴이 너비
        - h: 얼굴의 높이
        """
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        """
        cv2.rectangle(): 이미지 위에 사각형 그리기
        - frame: 비디오 프레임
        - (x, y): 사각형 좌상단 좌표
        - (x + w, y + h): 사각형 우하단 좌표
        - (255, 0, 0): 사각형 색상 (BGR 형식, 파란색)
        - 2: 선의 두께
        """
        cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        """
        cv2.putText(): 이미지 위에 텍스트 추가
        - frame: 비디오 프레임
        - dominant_emotion: 가장 높은 확률의 표정 이름
        - (x, y - 10): 텍스트 위치 (얼굴 좌상단보다 위쪽)
        - cv2.FONT_HERSHEY_SIMPLEX: 글꼴 스타일
        - 0.8: 글꼴 크기
        - (0, 255, 0): 텍스트 색상 (녹색)
        - 2: 텍스트 두께
        """

    # 비디오 출력
    cv2.imshow("Emotion Detector", frame)
    """
    cv2.imshow(): 현재 비디오 프레임을 화면에 표시
    - "Emotion Detector": 창 이름
    - frame: 처리된 비디오 프레임
    """

    # q를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        """
        cv2.waitKey(): 키 입력을 대기하는 함수
        - 매개변수 1: 1밀리초 대기
        - & 0xFF: 플랫폼 호환성을 위해 하위 8비트만 사용
        - ord('q'): 입력된 키가 'q'인지 확인
        - 'q'를 입력하면 루프 종료
        """
        break

# 리소스 해제
cap.release()
"""
cap.release(): 카메라 장치 해제
- 시스템 리소스를 반환하여 다른 프로그램에서 카메라를 사용할 수 있도록 함
"""
cv2.destroyAllWindows()
"""
cv2.destoryAllWindows(): OpenCV 창을 닫는 함수
- 비디오 스트림을 종료한 후 모든 창을 닫음
"""