# 가변 매개함수
    #  함수 정의할 때, 매개변수의 개수를 지정하지 않습니다.
    #  함수 내부에서는 리스트로 간주합니다.
    #  함수를 호출하는 쪽에서는 편안하게.. 1,2,3,4 or 1,2,3,4,5,1,4,5

def myFunc1(*args):
    for i in args:
        print(i)

datas = [10,20,50,60]
myFunc1(datas)

myFunc1(10,20,50,60)   # args에 *이 붙었기에 리스트 값으로 인식되어(값이 하나하나 입력되어) 작동됨  *___ : Packing

def myFunc2(args):
    for i in args:
        print(i)
myFunc2([10,20,50,60])


a,b = [10,20]         # unpacking : packing된 값을 풀어서 단일코드로
print(f'a = {a}')
print(f'b = {b}')