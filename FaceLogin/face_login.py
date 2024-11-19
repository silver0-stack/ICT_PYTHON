import cv2
import face_recognition
import pickle
import os



# 얼굴 등록 함수
# 사용자의 얼굴을 캡쳐하고 얼굴 인코딩 데이터를 저장한다
def register_face(username):
    # DirectShow 백엔드 사용하여 카메라 연결
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 0은 기본 카메라
    if not camera.isOpened():  # 카메라가 열리지 않는 경우
        print("카메라를 열 수 없습니다.")
        return

    # 이미 등록된 사용자인지 확인
    if os.path.exists("face_data.pkl"):
        with open("face_data.pkl", "rb") as file:
            data = pickle.load(file)
        if username in data: # 사용자가 이미 존재하는 경우
            print("이미 가입된 사용자입니다.")
            return


    print("얼굴을 캡쳐하려면 's'를 누르세요. 종료하려면 'q'를 누르세요.")
    while True:
        ret, frame = camera.read()
        if not ret:  # 프레임을 읽을 수 없는 경우
            print("카메라에서 프레임을 읽을 수 없습니다.")
            break

        cv2.imshow("얼굴 등록", frame)
        key = cv2.waitKey(1) & 0xFF  # 키 입력 대기

        if key == ord('s'):  # 's' 키 입력 시 얼굴 데이터 저장 시도
            face_locations = face_recognition.face_location(frame)  # 얼굴 위치 탐지
            if len(face_locations) == 1:  # 한 명의 얼굴만 감지된 경우
                face_encoding = face_recognition.face_encodings(frame, face_locations)[0]  # 얼굴 인코딩 생성
                save_face_data(username, face_encoding)  # 얼굴 데이터를 저장
                print(f"{username}님의 얼굴 데이터 저장 완료!")
                break
            elif len(face_locations) > 1:  # 여러 명의 얼굴이 감지된 경우
                print("여려 명의 얼굴이 감지되었습니다. 한 명만 화면에 표시해주세요.")
            else:  # 얼굴이 감지되지 않은 경우
                print("얼굴을 감지하지 못했습니다. 다시 시도해주세요.")
        elif key == ord('q'):  # 'q' 키 입력 시 ㅈ오료
            break

    camera.release()  # 카메라 리소스 해제
    cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기


# 얼굴 데이터 저장
# face_data.pkl 파일 생성
# pickle: 데이터를 직렬화하여 저장
#  기존 데이터를 파일에서 불러와 새 데이터를 추가하고 저장
def save_face_data(username, face_encoding):
    data = {}  # 기존 데이터 저장용 딕셔너리
    if os.path.exists("face_data.pkl"):  # 파일이 존재하면
        with open("face_data.pkl", "rb") as file:
            data = pickle.load(file)  # 기존 데이터를 로드

    data[username] = face_encoding  # 여러 명의 회원가입을 위해서 새 사용자 데이터를 추가

    with open("face_data.pkl", "wb") as file:  # 데이터를 파일에 저장
        pickle.dump(data, file)


# 페이스 로그인 함수
# 얼굴을 감지하고 등록된 사용자와 비교하여 로그인 여부 판단
def face_login():
    # 저장된 얼굴 데이터 확인
    if not os.path.exists("face_data.pkl"):  # 얼굴 데이터 파일이 없으면
        print("등록된 얼굴 데이터가 없습니다. 먼저 회원가입을 진행하세요.")
        return False

    with open("face_data.pkl", "rb") as file:
        registered_faces = pickle.load(file)  # 등록된 얼굴 데이터를 로드

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 카메라 초기화
    if not camera.isOpened():
        print("카메라를 열 수 없습니다.")
        return False

    print("페이스 로그을 진행합니다. 종료하려면 'q'를 누르세요.")
    while True:
        ret, frame = camera.read()
        if not ret:  # 프레임을 읽을 수 없는 경우
            print("카메라에서 프레임을 읽을 수 없습니다.")
            break

        cv2.imshow("페이스 로그인", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # 'q'키로 종료
            break

        face_locations = face_recognition.face_locations(frame)
        if len(face_locations) == 1:  # 한 명의 얼굴만 감지된 경우
            face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
            for username, registered_encoding in registered_faces.items():
                matches = face_recognition.compare_faces([registered_encoding], face_encoding)
                if matches[0]:  # 일치하는 얼굴이 있는 경우
                    print(f"{username}님, 페이스 로그인 성공!")
                    camera.release()
                    cv2.destroyAllWindows()
                    return True
        elif len(face_locations) > 1:
            print("여러 명의 얼굴이 감지되었습니다. 한 명만 화면에 표시해주세요.")
        else:
            print("얼굴을 감지하지 못했습니다. 다시 시도해 주세요.")
    camera.release()
    cv2.destroyAllWindows()
    return False


# 메인 메뉴
def main_menu():
    while True:
        print("\n=== 메뉴 ===")
        print("1. 회원가입")
        print("2. 페이스 로그인")
        print("3. 종료")
        choice = input("선택하세요: ")

        if choice == "1":
            username = input("등록할 사용자 이름을 입력하세요: ")
            register_face(username)
        elif choice == "2":
            success = face_login()
            if success:
                break
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")


if __name__ == "__main__":
    main_menu()
