# 클래스 콜백함수
# __eq__ : ==
# _ne__ : !=
# __lt__ : < A less than B
# __le__ : > A greater than B
# # __gt__ : <= A less thatn or equal to B
# __ge__ : >= A greater than or equal to B
# __str__ : print() 함수 호출 시 자동 호출

class Student:
    def __init__(self, name, score) :
        self.name = name
        self.score = score
    
    def __str__(self) :
        return f'이름 : {self.name}, 점수 : {self.score}'
    
    def __eq__(self, other):
        print('__eq__ 호출')

s1 = Student('이지은', 90)
s2 = Student('이지은', 90)
s1 == s2
print(s1)