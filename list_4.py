# 랜덤 라이브러리 가져오기
import random                                   # import : 함수 불러오기

# range(100)  0~99 범위에서 중복되지 않은 랜덤한 5개 추출
random_numbers = random.sample(range(100),5)
print(random_numbers)

# 0~10 사이 중에서 랜덤하게 한개 형성 
random_int = random.randint(0,10)

random_numbers.append(random_int)

# 50 의 포함 여부
print(50 in random_numbers)
print(random_numbers)

print('-' * 50)

# 삭제 
# del : 삭제된 데이터가 무엇인지 알려주지 않음 (삭제하고 바로 끝임)
# pop : 삭제된 데이터가 무엇인지 알려줄 수 있음 (삭제도 하지만 원하면 복원도 가능)

del random_numbers[0]
print(random_numbers)

removed_number = random_numbers.pop(0)
print(random_numbers)
print(removed_number)

