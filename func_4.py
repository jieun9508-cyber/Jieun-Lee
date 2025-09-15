def myAdd(num1 = 0, num2 = 0, num3 = 0) :      # default 값을 설정하는 경우 맨 마지막 변수에 넣는 게 논리적으로 맞음
    return num1 + num2 + num3          # 여러 default 값 설정 가능. 이때 맨 마지막부터 역순으로 순서대로 넣기

result1 = myAdd()
result2 = myAdd(1)
result3 = myAdd(1,2)
result4 = myAdd(1,2,3)
print(result1,result2,result3,result4)
