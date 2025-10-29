# 중첩 for2

list_1 = [10,20,30]
list_2 = [11,22,33]

list_2th = [list_1, list_2]
for i in range(len(list_2th)) :
    for j in range(len(list_1)):
        print(f'list_1st[{i}][{j}]  {list_2th[i][j]}')

