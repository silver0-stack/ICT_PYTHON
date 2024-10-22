# 샘플 Python 스크립트입니다.

# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.
# 안녕


# (들여쓰기) print(f'Hi, {name})
def print_hi(name):
    print(f'Hi, {name}')


def test_function():
    a = 1  # int
    b = '1'  # str
    c = 1.1  # float
    d = True  # bool
    e = 9999999999999999999999999999999999999999999999  # int
    f = 4 + 1j  # complex
    print(type(a), type(b), type(c), type(d), type(e), type(f))


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
# 스크립트가 직접 실행될 때만 아래의 코드를 실행하도록 합니다. 다른 스크립트에서 모듈로 임포트될 경우에는 실행되지 않습니다.
if __name__ == '__main__':
    print_hi('PyCharm')
    test_function()  # 함수 실행 구문
    a = "안녕"
    b = "하세요"
    print(a + b)  # a 출력
