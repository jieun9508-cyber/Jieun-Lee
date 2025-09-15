# 간단한 함수
# 함수 내의 로직인 한 줄로 표현 가능한 함수들
def my_add(a,b) :
    return a+b

# 람다 함수 - 한 줄로 표현한 함수  lambda 키워드 사용
# 간단한 함수를 즉석에서 만들 때 유용
# 무조건 값을  return하는 함수 -->  return 키워드 사용 X

test = lambda a,b : a + b   # def my_add(a,b) = lambda a,b

a,b = 10, 20
print(f'{a}+{b} = {test(a,b)}')