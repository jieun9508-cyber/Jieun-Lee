# 예외 상황 확인하기
# 예외가 발생할 수 있는 코드

print("# 숫자를 입력받습니다.")
number_input_a = int(input("정수 입력> "))

print("# 출력합니다.")
print("원의 반지름 :", number_input_a)
print("원의 둘레 :", 2 * 3.14 * number_input_a)
print("원의 넓이 : ", 3.14 * number_input_a * number_input_a)

try :     
    num1, num2 =  map(int, input('공백을 기준으로 두개의 숫자를 입력').split())
    calc_lists = [num1 + num2, num1 - num2, num1 * num2, num1 / num2]
    print('1. 더하기', end = '\t')
    print('2. 빼기', end = '\t')
    print('3. 곱하기', end = '\t')
    print('4. 나누기')
    choice = int(input('원하는 결과를 입력하세요 '))
    print(f"결과는 = {calc_lists[choice-1]}")
except:
    print('오류발생')
print('프로그램 종료')