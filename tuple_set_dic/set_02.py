#  집합연산이 가능
import random
list_a = random.sample(range(10), 6)
list_b = [1,5,4,1,2,1,5,1,7,1]
find_list = []
for a in list_a:
    for b in list_b:
        if a == b :
            find_list.append(a)
print(f'list_a = {list_a}')
print(f'list_b = {list_b}')
print(f'set(find_list) = {set(find_list)}')
# 13번 라인에서 set을 사용하지 않고 원래 로직(6~9라인)을 개선해서
# find_list에 중복값이 저장되지 않도록

import random
list_a = random.sample(range(11),7)  # 0~10 중복되지 않은 임의의 7개
list_b = random.sample(range(11),7)

# 중복을 허용하면서 0~10 임의의 추출
# random.randint(0,10) -> 임의의 한계
list_c = []
for _ in range(7) : # 변수(ex. i)의 역할이 없기 때문에 '_'을 사용하여 자리만 채워주면 됨
    list_c.append(random.randint(0,10))
