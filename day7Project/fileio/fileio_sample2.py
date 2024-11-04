# path : fileio\\fileio_sample2.py
# module : fileio.fileio_sample2

import os
import pickle

# 파이썬의 기본 파일 입출력은 텍스트 파일 입출력임
# 텍스트가 아닌 자료형의 파일을 다룰 때는 pickle 모듈 활용함
# 바이너리(binary : 이진데이터) 형식의 파일로 저장함 <= pickle 모듈 사용시
# 열기모드 : wb, rb, ab 로 표기해야 함

def test_binary_io():
    data = {1: 'python', 2: 'you need'}
    # 객체 상태로 그대로 저장하고자 한다면, 바이너리 모드로 저장해야 함
    f = open('btest.dat', 'wb')
    pickle.dump(data, f)
    f.close()

def test_binary_io2():
    f = open('btest.dat', 'rb')
    read_data = pickle.load(f)  # 파일에 기록된 객체 전체가 한번에 읽어들임
    f.close()
    print(read_data)
    print(type(read_data))

# 표준 입출력을 파일로 대상을 변경할 수 있음
# 표준 입력 : 키보드 입력 (컴퓨터 기본 입력장치임), sys.stdin 표현
# 표준 출력 : 모니터 출력 (컴퓨터 기본 출력장치임), sys.stdout 표현
import sys

def change_stdinout():
    # 시스템 표준출력을 따로 변수에 저장함 (원래 상태로 되돌리기 위해 필요함)
    stdout = sys.stdout

    f = open('test.txt', 'w', encoding='utf-8')
    sys.stdout = f      # 표준출력을 파일로 바꿈
    print('표준 출력을 바꾸어 파일에 내용이 기록됨')
    f.close()

    sys.stdout = stdout  # 원래 상태로 돌려놓음
    print('콘솔에 출력 확인')

# os 모듈의 함수 사용
# 디렉토리 만들기 : mkdir(), 작업 디렉토리 변경하기 : chdir()
# 사용자계정 조회 : getlogin(), 현재 작업 디렉토리 조회 : getcwd()
# 시스템 환경변수, 디렉토리, 파일 다룰 때 주로 이용함

def test_os():
    # listdir() : 해당 디렉토리 안의 파일들과 하위 디렉토리 목록 조회
    print(os.listdir('.'))  # . : 현재 디렉토리를 의미함
    print(os.listdir('../'))    # ../ : 상위 디렉토리를 의미함

    # rename() : 파일과 디렉토리의 이름 바꾸기함
    # os.rename(원래이름, 바꿀이름)
    # os.rename('test.txt', 'sample.txt')
    print(os.listdir('.'))

    # path.exists() : 파일이나 디렉토리의 존재 여부 확인
    print(os.path.exists('example.txt'))   # 파일이 없으면 False
    print(os.path.exists('sample.txt'))     # 파일이 있으면 True

    # path.abspath() : 파일이나 디렉토리의 절대경로 조회
    # print(os.path.abspath('sample.txt'))
    # f = open(os.path.abspath('sample.txt'), 'a', encoding='utf-8')
    # f.write(os.path.abspath('sample.txt'))
    # f.close()

    # path.basename(), dirname(), split() : 파일명, 경로명, 각가 분리
    current_path = os.path.abspath('sample.txt')
    print('current_path : ', current_path)
    print('basename : ', os.path.basename(current_path))  # 파일명.확장자 추출
    print('dirname : ', os.path.dirname(current_path))  # 경로만 추출
    print('split : ', os.path.split(current_path))  # (경로명, 파일명.확장자')

    # path.splitdrive(), splittext() : 경로에서 드라이브명만, 확장자만 추출
    print(os.path.splitdrive(current_path))  # ('드라이브명', '나머지경로' )
    print(os.path.splitext(current_path))   # ('경로와파일명', '확장자')


# 함수 실행
if __name__ == '__main__':
    # test_binary_io()
    # test_binary_io2()
    # change_stdinout()
    test_os()




