# 다양한 매개변수
    # 기본매개변수 default parameter
def myAdd(num1, num2=0) :
    return num1 + num2

result = myAdd(10,20)
print(f'result = {result}')

result = myAdd(10)        # 하나의 값을 넣어도 작동되는 이유 : num2 값이 미리 설정되어 있어서
print(f'result = {result}')