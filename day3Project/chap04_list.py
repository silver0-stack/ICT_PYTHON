# chap03_list.py

# 리스트(list) 자료형: mutable(변경 가능)
# 파이썬이 제공하는 군집 자료형으로, 자바의 List와 같은 역할을 함
# 여러 종류의 데이터를 순차적으로 저장하는 자료형
# 저장 용량에 제한이 없으며, 저장되는 데이터의 종류에도 제한이 없음
# 저장 순서에 따른 인덱스(index)를 가짐
# 리스트 생성 방법
# 1. list() 함수 사용
list_1 = list()
print('1. list() 함수로 리스트 생성:', list_1, type(list_1))  # [] <class 'list'>

# 2. [] 대괄호 사용
list_2 = []
print('2. [] 대괄호로 리스트 생성:', list_2, type(list_2))  # [] <class 'list'>

#리스트 특징 1: 인덱싱과 슬라이싱이 가능함
list_3 = ['apple', 'banana', 'cherry', [1, -1, 5, 6], 3.45, 0, True]


# 3. 인덱싱 (Indexing)
print('\n3. 인덱싱(Indexing)')
print('list_3[0]:', list_3[0])  # 첫 번째 요소
print('list_3[-1]:', list_3[-1])  # 마지막 요소
print('list_3[3][2]:', list_3[3][2])  # 중첩된 리스트의 요소

# 4. 슬라이싱 (Slicing)
print('\n4. 슬라이싱(Slicing)')
print('list_3[1:4]:', list_3[1:4])  # 인덱스 1부터 3까지 추출
print('list_3[:4:1]:', list_3[:4:1])  # 인덱스 0부터 3까지 추출

# 리스트 특징 2: 요소 추가와 삭제가 가능함

# 5. append() 함수로 요소 추가
print('\n5. append() 함수로 요소 추가')
list_3.append('orange')  # 리스트의 끝에 'orange' 추가
print('append() 후 list_3:', list_3)

# 6. extend() 함수로 여러 요소 추가
print('\n6. extend() 함수로 여러 요소 추가')
list_3.extend([10, 20, 30])  # 리스트에 [10, 20, 30] 요소들을 추가    [~, 10, 20, 30]
list_3.append([40, 50])  # 리스트에 [40, 50] 요소들을 추가       [~ , [40, 50]]
print('extend() 후 list_3:', list_3)

# 7. insert() 함수로 특정 위치에 요소 추가
print('\n7. insert() 함수로 특정 위치에 요소 추가')
list_3.insert(3, 'grape')  # 인덱스 3 위치에 'grape' 추가
print('insert() 후 list_3:', list_3)

# 8. remove() 함수로 특정 값 제거
print('\n8. remove() 함수로 특정 값 제거')
list_3.remove('grape')  # 첫 번째로 일치하는 'grape' 제거
print('remove() 후 list_3:', list_3)

# 9. pop() 함수로 요소 제거 및 반환
print('\n9. pop() 함수로 요소 제거 및 반환')
popped_item = list_3.pop()  # 마지막 요소 제거 및 반환
print('pop()으로 제거된 요소:', popped_item)
print('pop() 후 list_3:', list_3)
popped_item = list_3.pop(0)  # 인덱스 0의 요소 제거 및 반환
print('pop(0)으로 제거된 요소:', popped_item)
print('pop(0) 후 list_3:', list_3)

# 10. clear() 함수로 모든 요소 제거
print('\n10. clear() 함수로 모든 요소 제거')
list_temp = [1, 2, 3]
list_temp.clear()
print('clear() 후 list_temp:', list_temp)

# 리스트 특징 3: 기타 유용한 함수들

# 11. index() 함수로 특정 값의 인덱스 찾기
print('\n11. index() 함수로 특정 값의 인덱스 찾기')
list_4 = ['apple', 'banana', 'cherry', 'banana']
idx = list_4.index('banana')
print("'banana'의 인덱스:", idx)

# 12. count() 함수로 특정 값의 개수 세기
print('\n12. count() 함수로 특정 값의 개수 세기')
count = list_4.count('banana')
print("'banana'의 개수:", count)

# 13. sort() 함수로 정렬하기
print('\n13. sort() 함수로 정렬하기')
numbers = [3, 1, 4, 2]
numbers.sort()
print('오름차순 정렬:', numbers)
numbers.sort(reverse=True)
print('내림차순 정렬:', numbers)

# 문자열 리스트 정렬
string_elements = ['apple', 'banana', 'cherry', 'orange']
string_elements.sort()
print('문자열 리스트 정렬:', string_elements)

# 14. reverse() 함수로 요소 순서 뒤집기
print('\n14. reverse() 함수로 요소 순서 뒤집기')
numbers.reverse()
print('reverse() 후 numbers:', numbers)

# 15. copy() 함수로 리스트 복사하기 (얕은 복사)
print('\n15. copy() 함수로 리스트 복사하기')
original_list = [1, 2, 3]
copied_list = original_list.copy()
print('original_list:', original_list)
print('copied_list:', copied_list)
original_list[0] = 99
print('원본 수정 후 original_list:', original_list)
print('원본 수정 후 copied_list:', copied_list)

# 16. len() 함수로 리스트 길이 구하기
print('\n16. len() 함수로 리스트 길이 구하기')
print('list_3의 길이:', len(list_3))

# 17. sum() 함수로 요소들의 합계 구하기
print('\n17. sum() 함수로 요소들의 합계 구하기')
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print('numbers의 합계:', total)

# 18. min(), max() 함수로 최소값, 최대값 찾기
print('\n18. min(), max() 함수로 최소값, 최대값 찾기')
print('numbers의 최소값:', min(numbers))
print('numbers의 최대값:', max(numbers))

# 19. enumerate() 함수로 인덱스와 값 함께 가져오기
print('\n19. enumerate() 함수로 인덱스와 값 함께 가져오기')
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')

# 20. 리스트 컴프리헨션 (List Comprehension)
print('\n20. 리스트 컴프리헨션 (List Comprehension)')
squares = [x ** 2 for x in range(5)]
print('0부터 4까지의 제곱수 리스트:', squares)

# 21. 이터러블(iterable) 객체를 리스트로 변환하기
print('\n21. 이터러블(iterable) 객체를 리스트로 변환하기')
s = 'hello'
char_list = list(s)
print('문자열을 리스트로 변환:', char_list)

# 22. 기타 함수 활용 예제
print('\n22. 기타 함수 활용 예제')

# 모든 공백 제거하기
ss4 = '      Hello,      World!     '
print('|', ss4.replace(' ', ''), '|', sep='')

# 연속된 공백을 하나의 공백으로 줄이기
print('|', ' '.join(ss4.strip().split()), '|', sep='')

# 정규 표현식으로 공백 줄이기
import re

print('|', re.sub(' +', ' ', ss4.strip()), '|', sep='')

# 리스트의 요소들을 하나의 문자열로 합치기
print('\n리스트의 요소들을 하나의 문자열로 합치기')
word_list = ['Python', 'is', 'fun']
sentence = ' '.join(word_list)
print('문장:', sentence)
