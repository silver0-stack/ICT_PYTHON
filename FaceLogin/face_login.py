import cv2
import face_recognition
import pickle
import os

# 얼굴 등록 함수
def register_face(username):
    # DirectShow 백엔드 사용
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not camera.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    print("얼굴을 캡처하려면 's'를 누르세요. 종료하려면 'q'를 누르세요.")
    while True:
        ret, frame = camera.read()
        if not ret:
            print("카메라에서 프레임을 읽을 수 없습니다.")
            break

        cv2.imshow("얼굴 등록", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            face_locations = face_recognition.face_locations(frame)
            if len(face_locations) == 1:
                face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
                save_face_data(username, face_encoding)
                print(f"{username}님의 얼굴이 등록되었습니다.")
                break
            else:
                print("한 명의 얼굴만 화면에 표시해주세요.")
        elif key == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


# 얼굴 데이터 저장
def save_face_data(username, face_encoding):
    data = {}
    if os.path.exists("face_data.pkl"):
        with open("face_data.pkl", "rb") as file:
            data = pickle.load(file)

    data[username] = face_encoding

    with open("face_data.pkl", "wb") as file:
        pickle.dump(data, file)

if __name__ == "__main__":
    username = input("등록할 사용자 이름을 입력하세요: ")
    register_face(username)