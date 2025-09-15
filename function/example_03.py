def get_data(start, end, input_str = '입력 : ') :
    while True:
        try:
            h_num = int(input(f'{input_str}({start}~{end})'))
            if not start <= h_num <= end:
                raise ValueError (f'{start}~{end}  범위 초과')
        except Exception as e : 
            print(f'오류 : {e}')
        else :
            return h_num

def check_winner(computer, human) :

# 랜덤점수 - 컴퓨터가 선택한 값
    import random as rd
start, end = 1, 100      # 튜플로 인식
computer = rd. randint(start,end)

count = 0
game_history = []
while True :
    count += 1
    human = get_data(start,end)
    # 게임
    if human > computer :
        print("크다")
        game_history.append((human,'크다'))
    elif human < computer : 
        print("작다")
        game_history.append(human,'작다')
    else :
        print("f'정답 횟수 : {count}")
        for guess_value, state in game_history :
            print(f'{guess_value} - {state}')

        break


    count = 0
    game_history = []
    while True :
        count += 1
        human = get_data(start, end)
        # 승자선택 로직
        if check_winner(human, computer) :
            break
