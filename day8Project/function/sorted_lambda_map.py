# 추가 예제: 딕셔너리 리스트 정렬하기
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20},
    {'name': 'David', 'age': 28}
]

# 나이를 기준으로 오름차순 정렬
sorted_people = sorted(people, key = lambda x: x['age'])

print(sorted_people)
# [{'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'David', 'age': 28}, {'name': 'Bob', 'age': 30}]



