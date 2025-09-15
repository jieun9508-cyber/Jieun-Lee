# 가위 바위 보 게임 (computer vs user)
# 가위 : 1, 바위 : 2, 보 : 3
# 규칙 : 컴퓨터가 임의로 숫자를 선택 : random 이용
# 인간이 숫자를 입력                : input
# 승패를 기록 
# 3번마다 계속할지 물어보기          : for

import random
# 1: 가위
# 2: 바위
# 3: 보
# 랜덤하게 선택한 컴퓨터의 값
def get_com_num(start=1,end=3):
    '''
    랜덤값 출력 (start ~ end)
    '''
    return random.randint(start,end)
    

def get_user_num():
     return int(input("입력(1 : 가위, 2 : 바위, 3 : 보) : "))

com_choice = get_com_num()
# 사용자의 값
user_choice = get_user_num()

def check_winner(com_num, user_num):
     if user_choice == com_choice :
        print("무")
     else :
        if (user_choice == 1 and com_choice == 3) or \
            (user_choice == 2 and com_choice == 1) or \
            (user_choice == 3 and com_choice == 2):
            print("승")
        else :
                    print("패")

# 승패 확인
print(com_choice)   # 디버깅용. 개발이 완료되면 삭제

if user_choice == com_choice :
        print("무")
else :
    if (user_choice == 1 and com_choice == 3) or \
        (user_choice == 2 and com_choice == 1) or \
        (user_choice == 3 and com_choice == 2):
        print("승")
    else :
        print("패")

for i in range(1,101):
    if i%3 == 0:
        is_continue = input('Continue? (Y/y)').upper()
        if not is_continue == 'Y' :
            break
    else

    # 랜덤하게 선택한 컴퓨터의 값





# 가위 - 바위      1-2  1%3 1
# 바위 - 보        2-3  1%3 1
# 보 - 가위        3-1  -2%3 1
