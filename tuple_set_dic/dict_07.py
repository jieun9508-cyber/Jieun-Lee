# enumerate(), zip(),  .items()  .keys()   .values()
# map(), 정렬  --> 람다함수를 적용
# 함수의 파라미터 - 키워드 파라미터, 가변 키워드 파라미터

# list_a = ['사과', '포도', '딸기']
# for index, value in enumerate(list_a) :
#     print(f'{index} : {value}')

# a,b = [10, 20]

# a,b = (0, '포도')
# print(b) 

list_a = ['사과', '포도', '딸기']
for idx, data in enumerate(list_a) :
    print(f'idx = {idx}  data = {data}')


# zip() 두 개의 리스트 또는 집합을 각 원소별로 묶어준다
names = ['홍길동', '이순신']
ages = [25, 35]
print(zip(names, ages))
print(list(zip(names, ages)))  # [('홍길동', 25), ('이순신', 35)]
print(dict(zip(names, ages)))  #  {'홍길동' : 25, '이순신' : 35}
for name, age in zip(names, ages) : 
    print(f'name:{name}, age:{age}')

# .items()
dict_1 = {'취미' : '수영', '좋아하는 음식' : '떡볶이'}
print(f'dict_1 = {dict_1}')
print(f'keys = {dict_1.keys()}')
print(f'values = {dict_1.values()}')
print(f'.items() = {dict_1.items()}')