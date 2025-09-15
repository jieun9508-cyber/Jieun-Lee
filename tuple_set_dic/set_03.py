# 합집합
    # 연산자 '|' (파이프 연산자)  --> or
set_a = {1,2,3}
set_b = {3,4,5}
union_set = set_a | set_b 
print(union_set)
    # 메서드 .union()

# 교집합
    # 연산자 '&'  --> and
set_a, set_b = {1,2,3,4}, {2,3,5}
print(set_a & set_b)
    # 메서드 .intersection()
print(set_a.intersection(set_b))
# 차집합
    # 연산자 '-' 
print(set_a - set_b)
    # 메서드 .difference
print(set_a.difference(set_b))