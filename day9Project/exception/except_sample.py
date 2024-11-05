# day9Project\\except_sample.py
# module: exception.except_sample
# 파이썬에서의 예외 처리

"""
파이썬 에러는 크게
 - 구문에러(Syntax Error)
 - 예외(Exception)
로 구분된다

구문에러(Syntax Error)는 파이썬 코드가 문법적으로 잘못되었을 때 발생하는 에러다
코드를 실행하기 전에 파이썬 인터프리터가 코드를 분석할 때 발견된다
따라서 SyntaxError는 코드가 실행되기 전에 발생하므로,
해당 에러를 동일한 코드 내에서 try-except블록으로 잡아낼 수 없다.
try-except 블록이 실행되기 전에 이미 파이썬 인터프리터가 코드 실행 전에 에러를 발견하고 프로그램이 중단되기 때문이다.
괄호의 짝이 맞지 않거나, 잘못된 키워드 사용 등

예외(Exception)는 프로그램 실행 중에 발생하는 오류로,
코드의 논리적 문제나 예상치 못한 상황으로 인해 발생한다
프로그램 실행 중에 발생하며, 적절히 처리하지 않으면 프로그램 중단된다
0으로 나누기, 존재하지 않는 파일 열기, 인덱스 초과 등이 있다



else와 finally 사용하기
 - else: 예외가 발생하지 않았을 때 실행되는 코드
 - finally: 예외 발생 여부와 상관없이 항상 실행되는 코드

"""


def syntaxerr():
    try:
        exec("Hello ('World '") # exec() ,compile() 함수로 try-except 블록으로 syntax error를 예방할 수 있다.
    except SyntaxError as e:
        print(f"{e}: 괄호 짝이 맞지 않습니다.")


def nameerr():
    try:
        print(x) # NameError: name 'x' is not defined
    except NameError as e:
        print(f"{e}: x 가 정의되지 않았습니다.")


def typeerr():
    try:
        '2' + 3 # TypeError: can only concatenate str (not "int") to str
    except TypeError as e:
        print(f"{e}: 문자열과 숫자를 더할 수 없습니다.")


def indexerr():
    try:
        lst = [1, 2, 3]
        print(lst[3])  # IndexError: list index out of range
    except IndexError as e:
        print(f"{e} : 리스트에 존재하지 않는 인덱스를 참조했습니다.")


def keyerr():
    try:
        d = {'a': 1, 'b': 2}
        print(d['c']) # KeyError: 'c'
    except KeyError as e:
        print(f"{e}: 존재하지 않는 딕셔너리의 키를 참조했습니다.")


def valueerr():
    try:
        int('abc') # ValueError: invalid literal for int() with base 10: 'abc'
    except ValueError as e:
        print(f"{e}: 함수에 적절하지 않은 값을 인자로 전달했습니다.")



# FileNotFouncError: [Errno2] No such file or directory: 'non_existent_file.txt'
def filenotfounderr():
    try:
        with open('non_existent_file.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"{e}: 파일을 찾을 수 없습니다.")


# 객체가 특정 속성이나 메소드를 갖고 있지 않을 때 발생한다
def attributeerr():
    try:
        num = 10
        num.append(5) # AttributeError: 'int' object has no attribute 'append'
    except AttributeError as e:
        print(f"{e}: 정수형 객체는 'append' 메소드를 가지고 있지 않습니다.")



# 재귀 호출이 너무 깊어져서 호출 스택이 초과될 때 발생한다
def recursionerr():
    try:
        recursionerr() # RecursionError: maximum recursion depth exceeded
    except RecursionError as e:
        print(f"{e}: 재귀호출의 깊이가 호출 스택을 초과했습니다.")


"""
예외 계층 구조(Exception Hierarchy)
파이썬의 예외는 계층 구조로 이루어져 있으며, 모든 예외느 BaseException 에서 파생된다

[BaseException]
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
           +-- FloatingPointError
           +-- OverflowError
           +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
           +-- ModuleNotFoundError
      +-- LookupError
           +-- IndexError
           +-- KeyError
      +-- MemoryError
      +-- NameError
           +-- UnboundLocalError
      +-- OSError
           +-- BlockingIOError
           +-- ChildProcessError
           +-- ConnectionError
                +-- BrokenPipeError
                +-- ConnectionAbortedError
                +-- ConnectionRefusedError
                +-- ConnectionResetError
           +-- FileExistsError
           +-- FileNotFoundError
           +-- InterruptedError
           +-- IsADirectoryError
           +-- NotADirectoryError
           +-- PermissionError
           +-- ProcessLookupError
           +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
           +-- NotImplementedError
           +-- RecursionError
      +-- SyntaxError
           +-- IndentationError
                +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
           +-- UnicodeError
                +-- UnicodeDecodeError
                +-- UnicodeEncodeError
                +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- PendingDeprecationWarning
           +-- ResourceWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning

"""


def try_except_finally():
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    else: # else: 예외가 발생하지 않았을 때 실행되는 코드
        print(f"결과: {result}")
    finally:
        print("프로그램이 종료됩니다.")


if __name__ == "__main__":
    syntaxerr()
    nameerr()
    typeerr()
    indexerr()
    keyerr()
    valueerr()
    filenotfounderr()
    attributeerr()
    recursionerr()
    try_except_finally()
