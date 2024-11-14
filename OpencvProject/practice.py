from dbm import error

import cv2
import os

'''이미지 읽기 및 표시'''
def read_image():
    # 이미지 읽기
    img = cv2.imread('ringowithhorn.jpg') # 이미지를 파일에서 읽어오는 함수
    """
    이미지를 파일에서 읽어오는 함수
    이미지를 메모리에 로드해 놓고 imshow 단계에서 표시하거나 변환하는데 필요함
    - return: 이미지를 NumPy 배열로 변환한 결과
    - 'img' 변수에는 읽어온 이미지의 데이터가 저장됨.
    """

    # 이미지 보기
    cv2.imshow('Image', img)
    """
    이미지를 화면에 표시하는 함수
    로드한 이미지를 화면에 표시하여 확인
    - 'Image': 창의 제목을 설정
    - 'img': 화면에 표시될 이미지의 데이터
    - 이 함수는 별도의 창을 열어 이미지를 렌더링한다
    - imshow()는 읽어온 이미지가 제대로 표시되는지 확인하는 데 사용됨
    """

    # 키 입력 대기 후 창 닫기
    cv2.waitKey(0)
    """
    키 입력을 대기하는 함수
    - 매개변수 0: 무한정 대기하며 키 입력을 기다림
    - 키 입력이 감지되면 대기를 멈추고 다음 코드로 진행
    - 주의: 이 함수가 없으면 창이 즉시 닫혀 이미지가 보이지 않음
    """
    cv2.destroyAllWindows()
    """
    모든 OpenCV 창을 닫는 함수
    - imshow()로 생성된 창을 닫기 위해 호출됨
    - 프로그램 종료 전에 모든 창을 닫아 리소스 낭비 방지
    - 프로그램 종료 시 필수적으로 호출해야 함
    """



'''그레이스케일 변환'''
def grayscale():
    # 1. 이미지 읽기
    img = cv2.imread('ringowithhorn.jpg')
    """
    - return: 이미지를 NumPy 배열로 변환한 결과
    - 'img' 변수에는 읽어온 이미지의 데이터가 저장됨. 
    """

    # 2. 컬러 이미지를 그레이스케일로 변환
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    """
    cv2.cvtColor(): 이미지의 색상 공간을 변환하는 함수
    - img: 변환할 원본 이미지
    - cv2.0COLOR_BGR2GRAY: BGR(컬러)에서 Grayscale(회색조)fh qusghks
    - return: 변환된 그레이스케일 이미지
    - 색상을 없애고 밝기만을 남겨 데이터 처리나 시각적 확인을 단순화
    """

    # 3. 이미지 출력
    cv2.imshow('Grayscale Image', gray_img)
    """
    cv2.imshow(): 이미지를 화면에 표시하는 함수
    - 'Grayscale Image': 창의 제목으로 설정됨
    - 'gray_img': 화면에 표시할 그레이스케일 이미지 데이터
    - 변환 결과를 확인하는 데 사용됨
    """

    # 4. 키 입력 대기
    cv2.waitKey(0)
    """
    cv2.waitKey(): 키 입력을 대기하는 함수
    - 매개변수 0: 무한정 대기하며 키 입력을 기다림
    - 키 입력이 감지되면 대기를 머추고 다음 코드로 진행
    - 이 함수가 없으면 창이 즉시 닫혀 변환 결과를 확인할 수 없음
    """

    # 5. 창 닫기
    cv2.destroyAllWindows()
    """
    cv2.destroyAllWindows(): 모든 OpenCV 창을 닫는 함수
    - imshow()로 생성된 창을 닫기 위해 호출됨
    - 리소스를 정리하고 프로그램 종료 전 창을 다아야 함
    """



'''비디오 스트림 처리'''


def video_stream():
    # 1. 카메라 연결
    cap = cv2.VideoCapture(0)  # 0: 기본 카메라 사용, 만약 카메라가 두 대 있다면 VideoCapture(0), VideoCapture(1) ...
    """
    cv2.VideoCapture(): 카메라 장치를 연결하는 함수
    - 매개변수 0: 기본 카메라를 사용 (0은 시스템의 기본 카메라를, 1은 두 번째 카메라를 의미)
    - return: 비디오 캡쳐 객체(cap), 이 객체로 비디오 프레임을 읽음
    """
    if not cap.isOpened():
        print("카메라를 열 수 없습니다")
        return

    # 비디오 저장 설정
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) # 파일이름, 코덱, FPS, 프레임 크기

    print("비디오 녹화를 시작합니다. 'q'를 눌러 종료하세요.")
    while True:
        # 2. 비디오 프레임 읽기
        ret, frame = cap.read()
        """
        cap.read(): 카메라로부터 비디오 프레임을 읽는 함수
        - return ret: 프레임 읽기가 성공하면 True, 실패하면 False
        - return frame: 읽은 비디오 프레임 (이미지 형태로 반환)
        - 읽기 실패 시, 루프를 종료하기 위해 `if not ret`: 조건 추가
        """

        if not ret:
            print("카메라에서 프레임을 읽을 수 없습니다.")
            break # 비디오 스트림 읽기 실패 시 종료

        out.write(frame)

        # 3. 현재 프레임 표시
        cv2.imshow('Video Stream', frame)
        """
        cv2.imshow(): 현재 읽은 비디오 프레임을 창에 표시하는 함수
        - 'Video Stream': 창의 제목
        - frame: 카메라에서 읽은 비디오 프레임
        - 각 프레임을 빠르게 화면에 출력하여 비디오처럼 보이도록 함
        """

        # 4. 키 입력 확인
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q'누르면 종료
            """
            cv2.waitKey(1): 1밀리초 동안 키 입력을 기다림
            - & 0xFF: 키 입력의 마지막 8비트를 확인 (플랫폼 호환성 고려)
            - ord('q'): 입력 키가 'q'인지 확인, 'q' 입력 시 루프 종료
            - 사용자가 'q'를 입력하면 비디오 스트림 종료
            """
            print("비디오 녹화를 종료합니다.")
            break

    # 5. 자원 정리 및 창 닫기
    cap.release()
    """
    cap.release(): 카메라 장치를 해제하는 함수
    - 시스템 리소스를 해제하여 카메라를 다른 프로그램에서 사용할 수 있도록 함
    """
    out.release()
    """
    out.release(): 비디오 저장 ��치를 해제
    - 비디오 저장을 위해 파일 이름, FPS, 프레임 크기를 설정했으므로 이를 해제
    """
    cv2.destroyAllWindows()
    """
    cv2.destroyAllWindows(): 모든 OpenCV 창을 닫는 함수
    - imshow()로 생성된 창을 닫아 리소스를 정리
    """


'''녹화된 비디오 재생'''
def play_video():
    video_path='output.avi'

    if not os.path.exists(video_path): # 비디오 파일이 존재하는지 확인
        print("현재 존재하는 영상 파일이 없습니다.")
        return

    cap=cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("비디오 파일을 열 수 없습니다.")
        return

    print("녹화된 비디오를 재생합니다. 'q'를 눌러 종료하세요.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Recorded Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    while True:
        # 비디오 파일 존재 여부 확인
        video_exists = os.path.exists('output.avi')

        print("\n=== OpenCV 기능 선택 ===")
        print("1. 이미지 읽기 및 표시")
        print("2. 그레이스케일 변환")
        print("3. 비디오 스트림 처리")
        if video_exists:
            print("4. 녹화된 비디오 보기")
        print("0. 종료")

        choice = input("선택: ")

        if choice == '1':
            read_image()
        elif choice == '2':
            grayscale()
        elif choice == '3':
            video_stream()
        elif choice == '4' and video_exists:
            play_video()
        elif choice == '4' and not video_exists:
            print("현재 존재하는 영상 파일이 없습니다.")
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")


if __name__ == '__main__':
    main()
