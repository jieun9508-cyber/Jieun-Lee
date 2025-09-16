# 학생 정보를 담은 딕셔너리가 있고,
# 함수로 “학생 이름 + 도시” 조합 문자열을 반환하는 함수를 작성해봐.

# student = {
#     "name" : "Jane",
#     "city" : "Incheon"}

# profile = f"{student["name"]} + {student["city"]}"

# print(profile)


# def plus(n) :
#     print(n**2)
# result = plus(3) 
# print("result =", result)

1. 
# n = list(map(int, input().split()))
# print(min(n))
# print(max(n)


# class Circle :
#     def __init__(self, radius) :
#         self.radius = radius

#     @property
#     def radius(self) :
#         return self._radius
#     @radius.setter
#     def radius(self, value) :
#         if value > 0 :
#             self._radius = value
#         else :
#             print("반지름은 0보다 커야 합니다.")

# class BankAccount :
#     def __init__(self, balance) :
#         self.balance = balance
#     @property
#     def balance(self) :
#         return self._balance
#     @balance.setter
#     def balance(self, value) :
#         if value >= 0 :
#             self._balance = value
#         else :
#             print("잔액은 0 이상이어야 합니다")
        
# class Student :
#     def __init__(self, score) :
#         self.score = score
#     @property
#     def score(self) :
#         return self._score
#     @score.setter
#     def score(self, value) :
#         if 0 <= value <= 100 :
#             self._score = value
#         else :
#             print("점수는 0 이상 100 이하여야합니다.")

class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

b = B()
