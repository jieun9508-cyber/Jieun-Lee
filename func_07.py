# 함수
# 함수명 add 
# 파라미터는 2개 op1, op2
# 결과를 반환한다

# 생성
def add(op1, op2) :
    return op1 + op2  # result = op1 + op2 --> return(result)도 가능

# 사용
print(add(10,20))
two_number_lab = [add(10,30)]
numbers = [add(10,20), add(10,30) ]

# 매개변수 받아서 출력하는 함수
# 함수명 : show_number
# 매개변수형 : data
def show_number(data) : 
    return (f'numbers = {data}')


print(show_number(add(10,2)))



def greet(data) :
    return len(data)

hello = '안녕하세요'
print(greet(hello))

def transit(data1, data2) :
    return (f'{data1}은 영어로 {data2}입니다')

data1 = "파이썬"
data2 = "Python"
print(transit(data1, data2))
