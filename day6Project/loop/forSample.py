# path: loop/forSample.py or loop\\forSample.py
# module: loop.forSample
# 파이썬에서의 for 문 사용 테스트 스크립트

'''
for 문 작성형식 1:
for 변수 in 리스트 | 튜플 | 딕셔너리 | 집합 | 문자열: (콜론주의)
    반복 실행할 구문들 작성 (들여쓰기 중요)
주의사항: in 오른쪽에는 값 하나(리터럴) 사용 못 함 (TypeError)

for 문 작성형식 2:
'''


def test_for1():
    # list 사용
    for i in [1, 2, 3, 4, 5]:
        print(i)

    # for k in 10:
    #     print(k)  # TypeError: 'int' object is not iterable

    # tuple 사용
    for t in (10, 15, 20, 25):
        print(f'{t} is even' if t % 2 == 0 else f'{t} is odd')
