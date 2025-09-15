# 사용자 입력 처리 함수
# 이름 get_data()
# 파라미터
    # start : 시작값
    # end : 종료값
    # input_str : 가이드문구
# 사용자 입력은 input()
# return 정수로 변환된 입력값

while True :
    try:
        h_num = int(input('정수를 입력하세요(1~100)'))
        if not 0 <= h_num <= 100 :
            raise ValueError('1~100 범위 초과')
        break
    except Exception as e:
        print(f'오류 : {e}')
    else :
        break


while True :
    try :
        h = int(input('키를 입력하세요(120~180)'))
        if not 120<=h<=180 :
            raise ValueError ('120~180 범위 초과')
        break
    except Exception as e :
        print(f'오류 : {e}')
    else :
        break

while True :
    try :
        c = input('원하는 색깔을 고르세요(빨강, 파랑, 노랑, 보라)')
        if not c in ["빨강", "파랑", "노랑", "보라"] :
            raise ValueError ('유효하지 않은 값입니다')
        break
    except Exception as e :
        print(f'오류 : {e}')
    else :
        break 