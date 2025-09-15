# 저금통
list_a = [100,500,10,500,100,50,500,10]
# 저금통에 있는 동전의 종류  10,50,100,500

# Set
set_a = {1,2,3,1,2,3,1}
print(f'set_a = {set_a}')

# 중복을 제거(허용하지 않는다)한다
print(set(list_a))

set_2 = {1,2}
# print(set_2[0]) 지원 불가 (순서를 보장하는 것이 아니기 때문에 인덱스 확인 불가)
set_2.add(3)
print(set_2)
set_2.remove(2)
print(set_2)
print(set_2.pop())   # pop()은 실행되나 pop(index번호)는 실행되지 않는다. 이유는 인덱스 확인과 같음
