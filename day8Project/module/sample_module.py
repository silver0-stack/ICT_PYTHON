# path: module\\samples_module.py
# module: module.sample_module
# 파이썬에서 모듈 만들어서 사용하기

# 모듈: 파이썬 소스 파일이다.(파일명.py)
# 파일명이 모듈명이 됨
# 모듈용 소스 파일에는 함수와 전역변수, 클래스가 저장됨
# 모듈용 소스 파일에는 main이 있으면 안 됨(필요시 주석 처리함)


'''
모듈이란 파이썬 코드의 재사용 가능한 단위로,
변수, 함수, 클래스 등을 하나의 파일에 정의한 것이다.
모듈을 사용하면 코드의 중복을 줄이고, 프로젝트를 더 체계적으로 관리할 수 있다.

모듈의 장점
 1. 재사용성: 동일한 코드를 여러 번 작성하지 않고 필요한 곳에서 불러와 사용한다
 2. 구ㅜ조화: 프로젝트를 논리적인 단위로 나누어 관리한다
 3. 유지보수성: 코드를 더 쉽게 관리하고 수정한다
 4. 협업: 여러 개발자가 동시에 작업할 때 코드 충돌을 줄이고 역할을 분담할 수 있다.
'''

# 변수
greeting = "안녕하세요! 저는 모듈입니다."


# 함수
def add(a, b):
    return a + b


def substract(a, b):
    return a - b


# 클래스
class Calculator:
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "0으로 나눌 수 없습니다."


# 모듈 검색 경로 이해하기
#  파이썬은 모듈을 임포트할 때, 특정한 검색 경로에서 모듈을 찾는다.
# sys.path: 파이썬의 모듈 검색 경로 리스트
import sys

print(sys.path)
# ['D:\\python_workspace\\day8Project', 'D:\\python_workspace\\day8Project', 'C:\\Program Files\\JetBrains\\PyCharm 2024.2.3\\plugins\\python-ce\\helpers\\pycharm_display', '...]


# 패키지 만들기
# 모듈이 많아지면, 관련 모듈들을 하나의 디렉토리(폴더)에 모아 패키지로 구성할 수 있다
# 패키지는 디렉토리와 __init__.py 파일로 구성된다

'''
my_package/
│
├── __init__.py
├── module1.py
├── module2.py
└── sub_package/
    ├── __init__.py
    └── module3.py


    __init__.py: 패키지 초기화 파일로, 패키지를 모듈로 인식하게 한다. (파이썬 3.3부터 없어도 패키지로 인식되지만, 포함하는 게 좋다)
    모듈 파일: module1.py, module2.py, module3.py... 등 실제 기능을 담은 파이썬 파일
    서브 패키지: 패키지 내에 또 다른 패키지를 포함할 수 있다.
'''

# 표준 라이브러리 및 외부 라이브러리 활용하기

# 파이썬은 방대한 Standard Library 를 제공하며 외부 라이브러리도 손쉽게 설치하여 사용할 수 있다.
# math 모듈 사용하기
import math

print(math.sqrt(16))  # 4.0
print(math.pi)  # 3.141592653589793
print(math.factorial(5))  # 120

# datetime 모듈 사용하기
from datetime import datetime

now = datetime.now()
print(now)  # 2024-11-04 12:26:07.163487

#  외부 라이브러리 설치 및 사용하기
# STEP1) 패키지 관리자(PIP)를 사용하여 설치하기
# pip install requests

# STEP2) 외부 라이브러리 사용하기
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.json())

'''
{
'current_user_url': 'https://api.github.com/user', 
 'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}', 
 'authorizations_url': 'https://api.github.com/authorizations',
 'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}', 
 'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}', 
 'ser_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}', 
...
}

'''


# 모듈 내에서 외부에 비공개하고 싶은 변수나 함수는 언더스코어(_)로 시작한다
def _priavate_function():
    print("이거 안보이지롱~")


#  모듈을 임포트할 때는 테스트 코드가 실행되지 않지만, 직접 실행할 때는 테스트가 수행된다.
if __name__ == "__main__":
    # 모듈을 직접 실행할 때만 실행됨
    print("모듈을 직접 실행했습니다.")
    print(add(10, 5))
