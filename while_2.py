import time   #    5초 단위로 사용자한테 계속 할건지 물어본다..  "To be Continued?(Y/N)"
count = 0
while True :
    count += 1
    print(f'{count}초')
    time.sleep(1)   # 1초간 지연

    if count % 5 == 0 :
        is_continue = input('To be Continued? (Y/N)')
        is_continue = is_continue.upper()
        if is_continue == 'N' :
            break    