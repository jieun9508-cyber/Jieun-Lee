# 파이썬 클래스에서 getter setter 사용법
import random
class Person:
    def __init__(self, name, age):
        self.name = name  # private 변수(class 안에서만 사용)로 설정
        self._age = age    # private 변수로 설정
    @ property     # getter (메서드(함수)를 변수처럼 사용 가능하게 함)
    def age(self) :
        return self._age
    
    @age.setter  # setter (속성값을 안전하게 변경할 때 사용)
    def age(self, value) :
        self._age = value
# getter setter는 쌍으로 움직인다

p1 = Person('홍길동', 20)
print(p1.age)
print(p1.name)
del print(p1.name)
print(p1.name)  # 'Person' object has no attribute 'name'

