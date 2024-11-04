# path: loop\\loopSample.py | loop/loopSample.py
# module: loop.loopSample
from loop.forMission import practice
from loop.whileMission import sungjuk_process


#  연습 1
#  리스트 안의 튜플 아이템의 값들에 대해 둘 중의 큰 값과 작은 값을 분류해서 출력 처리


#  방법 1: 조건식 직접 작성
def practice1():
    nlist = [(1, 25), (2, 3), (30, 2), (4, 1)]
    # for 문 안에 if문 사용
    for item in nlist:
        if item[0]>item[1]:
            print(f'큰 값: {item[0]}')
            print(f'작은 값: {item[1]}')



#  방법 2: 내장함수 max(), min() 사용
def practice2():
    nlist = [(1, 25), (2, 3), (30, 2), (4, 1)]

    for item in nlist:
        min_val = min(item[0], item[1])
        max_val = max(item[0], item[1]) # max_val = max(item for item in nlist)
        print(f'큰 값: {max_val}')
        print(f'작은 값: {min_val}')

# 활용실습:
# 리스트 안에 있는 군자료형ㅇ들이 가진 값들 중에서 각각 가장 큰 값을 골라내서
# 별도의 리스트에 저장 처리하고 출력 확인

# 조건문을 직접 사용해서 해결
def practice3():
    lists = [[43, 1, 2], (41, 5, 7, 3), {8, 2, 50, 10}]
    max_list = []


    # for sub_list in lists:
    #     # 조건문 직접 사용해서 해결


# 내장함수 사용해서 해결: max(Iterable)
def practice4():
    lists = [[43, 1, 2], [5, 7, 3], [8, 2, 10]]
    max_list = []
    for sub_list in lists:
        max_list.append(max(sub_list))
    print(max_list) # [43, 7, 10]



#  while문으로 변경
def practice_while():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [10, '이순신', 95]]

    # for student in sungjuk_list:
    index = 0
    while index < len(sungjuk_list):
        student = sungjuk_list[index]
        if student[2] >= 60:
            print(f'{student[0]} 번 {student[1]} 학생은 합격입니다')
        else:
            print(f'{student[0]} 번 {student[1]} 학생은 불합격입니다')


# 연습문제 함수 실행
if __name__ == '__main__':
    # practice1()
    # practice2()
    # practice3()
    # practice4()
    # practice2()
    practice_while()