"""
키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.

입력 내용 :
    학생이름 : 홍길동 (name : str)
    학년 : 2 (grade : int)
    반 : 3 (s_class : int)
    번호 : 12 (s_no : int)
    점수 : 87.5 (score : float)

처리 내용 :
    입력받은 값들을 리스트(student_list)에 순서대로 저장 처리함

출력 내용 :
    리스트에 저장된 값들을 출력함
    2학년 3반 12번 홍길동의 점수는 87.50 입니다.
    -> 점수는 소수점 아래 둘째 자리 까지 표시
    -> format() 사용함
"""

student_list = []

name = input('학생이름 : ')
grade = int(input('학년 : '))
s_class = int(input('반 : '))
s_no = int(input('번호 : '))
score = float(input('점수 : '))

student_list.append(name)
student_list.append(grade)
student_list.append(s_class)
student_list.append(s_no)
student_list.append(score)


print(f'{student_list[1]}학년 {student_list[2]}반 {student_list[3]}번 {student_list[0]}의 점수는 {student_list[4]:.2f} 입니다.')
# format() 사용
print('{}학년 {}반 {}번 {}의 점수는 {:.2f} 입니다.'.format(student_list[1], student_list[2], student_list[3], student_list[0], student_list[4]))

print('\n 사용자로부터 입력을 받아 리스트에 저장한 후 format()을 사용한 출력')

# 학생 정보 입력 받아 리스트에 저장
student_list = [
    input('학생이름 : '),
    int(input('학년 : ')),
    int(input('반 : ')),
    int(input('번호 : ')),
    float(input('점수 : '))
]

# 리스트의 값을 포맷팅하여 출력
print('{}학년 {}반 {}번 {}의 점수는 {:.2f} 입니다.'.format(*student_list))


print('\n 리스트 대신 딕셔너리 사용')
# 학생 정보 입력 받아 딕셔너리에 저장
student = {
    'name': input('학생이름 : '),
    'grade': int(input('학년 : ')),
    'class': int(input('반 : ')),
    'no': int(input('번호 : ')),
    'score': float(input('점수 : '))
}

# 딕셔너리의 값을 포맷팅하여 출력
print('{}학년 {}반 {}번 {}의 점수는 {:.2f} 입니다.'.format(
    student['grade'], student['class'], student['no'], student['name'], student['score']
))



print('\n 함수화, 입력과 출력을 함수로 분리하면 코드의 재사용성과 가독성을 높인다.')

def get_student_info():
    return [
        input('학생이름 : '),
        int(input('학년 : ')),
        int(input('반 : ')),
        int(input('번호 : ')),
        float(input('점수 : '))
    ]

def print_student_info(student_list):
    print('{}학년 {}반 {}번 {}의 점수는 {:.2f} 입니다.'.format(*student_list))

student_list = get_student_info()
print_student_info(student_list)

