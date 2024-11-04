# path: loop\\list_in_for.py | loop/list_in_for.py
# module: loop.list_in_for
# 파이썬에서의 for문 사용 테스트 스크립트

# 리스트 내포 (리스트 안의 for) 테스트용 스크립트

# 리스트 안에 값 추가를 위한 for문을 포함하는 구문
# 작성형식: [기록할값 for value in iterable object if condition]
#  주의) 기록할 값과 변수의 이름이 반드시 같아야 함
# 시퀀스 객체(Iterable): range(10), [1,2,3,4,5], ('a'b,'c'), {'key": 'value'}, set([1,2,3,4,5])
# 시퀀스 객체 대신에 range([시작값,], 끝값, 간격) 함수 사용 가능함

#  리스트에 값 기록 1: append() 사용
def list_append():
    sample_list = list() # sample_list = []
    for i in range(10):
        sample_list.append(i)
    print(sample_list)


# 리스트 내포로 바꾼다면
def list_append2():
    sample_list = [n for n in range(1, 6)]
    print(sample_list)

#  리스트 내포 시에 if문도 같이 포함할 수 있음
def list_append3():
    sample_list = [n for n in range(1, 6) if n % 2 ==0]
    print(sample_list)

#  for문 안에 for문이 사용되는 경우 (다중 for문)
def list_append4():
    sample_list = list()
    for i in range(1, 6): # 1, 2, 3, 4, 5
        for m in range(1, 6): # 1, 2, 3, 4, 5
            sample_list.append(i * m)  # 2, 3, 4, 5, ...
            print(f'{i} x {m} = {i * m}')
        print('\n')


#  리스트 내포로 바꾼다면
def list_append5():
    sample_list = [i * m for i in range(1, 6) for m in range(1, 6)]
    print(sample_list)


# 구구단 2단~ 9단 곱하기 결과값을 리스트에 저장 처리함
# 리스트 내포로 작성함
def list_append6():
    sample_list = [n * m for n in range(2, 10) for m in range(1, 10)]
    print(sample_list)



#  이 파일 안에서 작성된 함수를 바로 실행해 보고자 한다면
# 띄어쓰기 조심!
if __name__ ==  '__main__':
    # 함수 실행 구문 작성
    # list_append()
    # list_append2()
    # list_append3()
    # list_append4()
    # list_append5()
    list_append6()