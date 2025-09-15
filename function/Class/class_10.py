# 숫자 맞추기 게임
# 규칙
# 1. 컴퓨터가 1~100 사이의 숫자를 랜덤으로 선택합니다.
# 2. 사용자는 숫자를 입력하여 컴퓨터가 선택한 숫자를 맞춥니다.
# 3. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 크면 "너무 큽니다."라고 출력합니다."
# 4. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 작으면 "너무 작습니다."라고 출력합니다.
# 5. 사용자가 컴퓨터가 선택한 숫자를 맞추면 "정답입니다!"라고 출력하고 게임을 종료합니다.
# 6. 사용자가 숫자를 맞출 때까지 계속 입력을 받습니다.

import random
class NumberGuessingGame:
    def __init__(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

    def get_user_guess(self):
        while True:
            try:
                guess = int(input("1부터 100 사이의 숫자를 입력하세요: "))
                if 1 <= guess <= 100:
                    return guess
                else:
                    print("숫자가 범위를 벗어났습니다. 다시 시도하세요.")
            except ValueError:
                print("유효한 숫자를 입력하세요.")

    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.number_to_guess:
            print("너무 작습니다.")
            return False
        elif guess > self.number_to_guess:
            print("너무 큽니다.")
            return False
        else:
            print(f"정답입니다! {self.attempts}번 만에 맞추셨습니다.")
            return True

    def play(self):
        print("숫자 맞추기 게임에 오신 것을 환영합니다!")
        while True:
            user_guess = self.get_user_guess()
            if self.check_guess(user_guess):
                break
