# path: make_class\\class_oop.py
# module: make_class.class_oop
# 파이썬에서 객체 지향 프로그래밍(OOP) 사용

class Dog:
    # 클래스 변수
    species = "Canis familiaris"

    # 생성자 메소드
    def __init__(self, name, age):
        # 인스턴스 변수
        self.name = name
        self.age = age

    # 인스턴스 메소드
    def bark(self):
        return f"{self.name} says woof!"


# Dog 클래스의 인스턴스 생성
my_dog = Dog("Buddy", 3)

# 객체의 속성 접근
print(my_dog.name)  # Buddy
print(my_dog.age)  # 3

# 객체의 메소드 호출
print(my_dog.bark())  # Buddy says woof!


class Cat:
    # 클래스 변수
    species = "Felis catus"

    # 생성자 메소드
    def __init__(self, name, age):
        # 인스턴스 변수
        self.name = name
        self.age = age


# 객체 생성
cat1 = Cat("Whiskers", 2)
cat2 = Cat("Mittens", 1)

# 클래스 변수 접근
print(Cat.species)  # Felis catus
print(cat1.species)  # Felis catus
print(cat2.species)  # Felis catus

# 인스턴스 변수 접근
print(cat1.name)  # Whiskers
print(cat1.age)  # 2


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 객체 생성 시 `__init__` 호출
person1 = Person("Alice", 25)
print(person1.name)  # Alice
print(person1.age)  # 25


class Resource:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 리소스가 생성되었습니다.")

    def __del__(self):
        print(f"{self.name} 리소스가 소멸되었습니다.")


# 객체 생성 및 소멸
res = Resource("Database")  # 파일 리소스가 생성되었습니다.
del res  # 소멸자 호출 # 파일 리소스가 소멸되었습니다.


class Circle:
    def __init__(self, radius):
        self.radius = radius

        # 인스턴스 메소드

    def area(self):
        return 3.14 * (self.radius ** 2)


# 객체 생성
circle = Circle(5)
print(circle.area())


class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

    # 클래스 메소드, 첫번째 매개변수로 cls
    @classmethod
    def get_total_books(cls):
        return cls.total_books


# 객체 생성
book1 = Book("To Kill a Mockingbird")
book2 = Book("1984")

# 클래스 메소드 호출
print(Book.get_total_books())  # 2


class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# 정적 메소드 호출
print(Math.add(3, 5))  # 8
print(Math.multiply(3, 5))  # 15



class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "소리를 냅니다."

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"


# 객체 생성
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, dog.speak()) # Buddy, 멍멍!
print(cat.name, cat.speak()) # Whiskers, 야옹!












