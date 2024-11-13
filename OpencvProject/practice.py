import cv2

'''이미지 읽기 및 표시'''


def read_image():
    # 이미지 읽기
    img = cv2.imread('ringowithhorn.jpg')

    # 이미지 보기
    cv2.imshow('Image', img)

    # 키 입력 대기 후 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()


'''그레이스케일 변환'''


def grayscale():
    # 이미지 읽기
    img = cv2.imread('ringowithhorn.jpg')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


'''비디오 스트림 처리'''


def video_stream():
    cap = cv2.VideoCapture(0)  # 0: 기본 카메라 사용

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q'누르면 종료
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    while True:
        print("\n=== OpenCV 기능 선택 ===")
        print("1. 이미지 읽기 및 표시")
        print("2. 그레이스케일 변환")
        print("3. 비디오 스트림 처리")
        print("0. 종료")

        choice = input("선택: ")

        if choice == '1':
            read_image()
        elif choice == '2':
            grayscale()
        elif choice == '3':
            video_stream()
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")


if __name__ == '__main__':
    main()
