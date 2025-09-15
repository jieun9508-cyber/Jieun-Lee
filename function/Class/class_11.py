# isinstance() 함수
# 객체가 특정 클래스의 인스턴스(객체)인지 확인하는 데 사용됩니다.
# 사용하는 이유
# 1. 타입 확인: 함수나 메서드가 특정 클래스의 인스턴스를 기대할 때, 이를 확인하여 잘못된 타입의 객체가 전달되는 것을 방지할 수 있습니다.
# 2. 다형성 지원: 상속 관계에 있는 클래스들 간에 다형성을 구현할 때, 객체가 특정 클래스나 그 하위 클래스의 인스턴스인지 확인할 수 있습니다.
class Student :
    def study(self) :
        return "공부 중입니다"
class Teacher :
    def teach(self) :
        return "가르치는 중입니다"
# 리스트에 어떤 객체가 있는지 모를 때 특정 인스턴스만 기대할 수 없다
peoples = [Student(), Teacher(), Student()]
del peoples[0]
if isinstance(peoples[0], Student) :
    print(peoples[0], peoples[0].study())
else :
    print(peoples[0], peoples[0].teach())

    # __<이름>__() 형태 : 특수한 상황에 자동으로 호출되도록 만들어짐