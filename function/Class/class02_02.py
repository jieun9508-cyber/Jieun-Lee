# 정수값이고 주어진 범위를 벗어나면 발생하는 Exception
class OutOfRangeError(Exception) :
    def __init__(self,  strname) :
        super().__init__(strname)
    def show_info(self) :
        print('사용자가 정의한 예외입니다.')

try :
    number = 100
    if not 0 <= number <= 10 :
        raise OutOfRangeError ('0과 10 사이를 벗어났습니다.')
    int('sdfasfg')
except OutOfRangeError as e :   # 새로운 개념의 에러를 새로 만들었으니 그걸 except에 넣어준다
    print(e.show_info())
except ValueError as e :
    print(e)