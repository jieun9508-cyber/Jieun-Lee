# 매개변수 O, 반환값 O
# 매개변수 O, 반환값 X
# 매개변수 X, 반환값 O
# 매개변수 X, 반환값X

def Year(Past, Present) :
    period = Present - Past
    return period
A = 2018
B = 2025 
print(Year(A, B))

def profile(name, age) :
    print(f"제 이름은 {name}이고 {age}살 입니다.")
name = "Jane"
age = 28
profile(name,  age)

import datetime
def time_now() :
    return datetime.datetime.now()
print(time_now())

def say_hello() : 
    print("안녕하세요")
say_hello()