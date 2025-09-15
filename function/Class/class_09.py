# 가위 바위 보 게임을 클래스로 구현하기
# 사용자로부터 입력을 받아 컴퓨터와 대결하는 가위, 바위, 보 게임
# 사용자는 "가위", "바위", "보" 중 하나를 입력하고, 컴퓨터는 무작위로 선택
# 게임의 승패를 판단하고 결과를 출력합니다.
# 가위는 1, 바위는 2, 보는 3으로 표현합니다.
# 게임이 끝나면 계속할지 물어본다.
import random
class RPSGame :
    choices = {1: "가위", 2: "바위", 3: "보"}
    
    def __init__(self) :
        self.user.choice = None
        self.computer.choice = None
            
    def get_computer_choice(self) :
        return random.randint(1, 3)
    
    def get_user_choice(self) :
        while True :
            try :
                user_input = int(input("가위(1), 바위(2), 보(3) 중 하나를 선택하세요: "))
                if user_input in self.choices :
                    return user_input
                else :
                    print("잘못된 입력입니다. 다시 시도하세요.")
            except ValueError :
                print("숫자를 입력하세요.")
    
    def determine_winner(self, user, computer) :
        if user == computer :
            return "무승부"
        elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2) :
            return "사용자 승리"
        else :
            return "컴퓨터 승리"
    
    def play(self) :
        while True :
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"사용자 선택: {self.choices[user_choice]}, 컴퓨터 선택: {self.choices[computer_choice]}")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            again = input("다시 하시겠습니까? (y/n): ")
            if again.lower() != 'y' :
                break

while True :
    game = RPSGame()
    RPSGame.play()
    again = input("다시 하시겠습니까? (y/n): ").strip().lower()
    if again != 'y' :
        print("게임을 종료합니다")
        break