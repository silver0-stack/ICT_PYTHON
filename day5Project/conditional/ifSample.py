# path: conditional\\ifSample.py or conditional/ifSample.py
# module: conditional.ifSample

# 제어문: 조건문
#  if, elif, else 사용 테스트 스크립트

'''
 제어문 종류: 조건문, 반복문, 분기문
 조건문: whrjsdmf wptlgotj rufrhkrk

'''

# 조건문에서는 조건 표현식(expression) 작성이 중요함
#  조건 표현식은 반드시 결과가 참 또는 거짓이 나오게끔 작성해야 함
#  비교, 논리 연산자 주로 사용됨

'''
if 조건식:
    조건의 결과가 참일 때 실행할 구문들(반드시 들여쓰기함), 구문은 최소 1개는 작성해야 함
'''


#  조건문 작성형식 1: if만 사용한 경우
#  입력받은 정수 숫자가 1이냐?
def test_if():
    num = int(input('(1인지 확인)숫자 입력: '))
    if num == 1:
        print(f'num is {num}')
    else:
        print(f'num is not 1')


# 정수를 입력받아 짝수인지 확인
# 짝수: 2의 배수를 말함, 2로 나눈 나머지가 0인 수
# 홀수: 2의 배수가 아님, 2로 나눈 나머지가 1인 수
def test_even():
    num = int(input('정수 숫자 입력: '))
    if num % 2 == 0:
        print(f'{num} is even number')
    else:
        print(f'{num} is odd number')


# 정수를 하나 입력받아서, 1부터 100 사이의 값이면 입력값의 제곱을 출력하고 100 이상이면 "1~100 사이의 값만 입력하세요"을 출력
def test_square():
    num = int(input('1~100 사이의 정수 입력: '))
    if num <= 100:
        print(f'{num}의 제곱: {num ** 2}')
    else:
        print('1~100 사이의 값만 입력하세요')


# in 연산자: list, tuple, set, dict, str, bytes, range, bytesarray, bytearray object
# 변수 또는 값 in iterable object: x in s => s 안에 x가 있느냐?
# iterable object: list, tuple, set, dict, str, bytes, range, bytesarray, bytearray object
# for문 사용 가능한 객체들과는 다 호환 가능함
# x not in s => s 안에 x가 없느냐? => x가 없으면 True, x가 있으면 False 리턴
def test_in():
    print(2 in [1, 2, 3])  # True
    print(2 not in [1, 2, 3])  # False
    print('a' in 'abcdef')  # True
    print('a' not in 'abcdef')  # False


def checkPayment():
    payment = ['card', 'money', 'mobile']
    price = 5000

    if 'money' in payment:
        print(f'현금 {price}원으로 결제')
    else:
        print(f'결제할 수 없습니다.')

    if 'bank' in payment:
        print(f'{price}원을 현금 지불했습니다.')
    else:
        print(f'다른 결제 수단을 선택하세요.')


# 조건문 작성형식 3: 다중 if 문
# if ... elif ... else ...
# if ... elif ... elif... elif....
def checkPayment2():
    payment = ['결제수단', '카드', '현금', '모바일', '제로페이']
    print('================결제수단 선택 ================')
    print('1. 카드')
    print('2. 현금')
    print('3. 모바일')
    print('4. 제로페이')

    no = int(input('결제할 번호를 입력하세요: '))
    price = int(input('결제할 금액: '))

    if no == 1:
        print(f'{price} 원을 {payment[no]}로 결제했습니다.')
    elif no == 2:
        print(f'{price} 원을 {payment[no]}로 결제했습니다.')
    elif no == 3:
        print(f'{price} 원을 {payment[no]}로 결제했습니다.')
    elif no == 4:
        print(f'{price} 원을 {payment[no]}로 결제했습니다.')
    else:
        print('1~3 번호만 입력하세요.')



# 간단 if문
# 변수 = 참일 때 실행값 if 조건식 else 거짓일 때 실행할 값들
def shortCondition():
    a = 1
    message = 'a is 1' if a == 1 else 'a is not 1'
    print(message)