# loop\\forSample.py | loop/forSample.py
# module: loop.forSample
# 파이썬에서의 while 문 사용 테스트 스크립트

'''

while 반복에 대한 조건식: (콜론주의)
      반복 실행 구문들 (들여쓰기 주의)

반복에 대한 조건식은 무한루프가 되지 않게 작성할 것 ( 주로 종료값 제시)
만약 조건식에 그냥 True를 사용한다면, 반드시 루프 안에서 종료에 대한 조건문을 작성해야 함

while True:
    반복 실행 구문
    if 종료조건:
       break
'''

def test_while():
    num = 5
    while num > 0:
        print(num)
        num -= 1
        if num == 0:
            break # 0이면 출력 안됨



#  반복 횟수가 정해지지 않은 경우 while문 주로 사용함
#  예: 문자 하나 입력받아서 그 문자의 유니코드를 출력 처리하는 구문이 반복 실행됨
#  단 , '0'이 입력되면 반복이 종료됨
def test_while_infinite():
    while True:
        char = input('Enter a character (Enter "0" to exit): ')
        if char == '0':
            print('Exiting... Program terminated. Goodbye! ^^')
            break
        elif len(char) != 1: # 문자열을 입력하면
            print('Error: Please enter exactly one character.')
            continue  # 다시 입력을 받기 위해 루프의 처음으로 돌아감
        print(f'{char} is unicode {ord(char)}')


# 파이썬에서는 여러 줄의 문자열 값을 표현할 때 3쌍의 따옴표를 이용할 수 있음
def display_menu():
    prompt = '''
        *** 원하는 메뉴 번호를 선택하세요 ***
        1. 추가
        2. 삭제
        3. 출력
        4. 종료
    '''
    # print(prompt)
    while True:
        print(prompt)
        no =int(input('번호 입력: '))

        if no == 4:
            print('프로그램을 종료합니다.')
            break
        print('---------END---------')













