from abc import ABC, abstractmethod
class Parents(ABC):
    def make_money(self) :
        raise NotImplementedError
    def save_money(self) :
        print("저축")

@abstractmethod    #추상메서드 : 상속한 애들이 반드시 save_money(self)를 다 가지고 있어야함(무조건). 없으면 개체 형성 불가
def save_money(self) :
    pass

class Child(Parents) :
    def make_money(self) :  #부모의 make_money 재정의(override)
        print('장사')   # 필요하면 재정의
    def save_money(self) :
        print('투자')
    

c = Child()  # 부모의 추상메서드를 상속받으면 클래스에서 반드시 재정의 안하면 객체 생성불가
c.make_money() # 다형성   # 자식클래스에서 재정의 안하면 예외 발생하도록 설계