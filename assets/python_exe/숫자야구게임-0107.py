"""
숫자 야구 게임
- 컴퓨터가 발생한 난수를 사용자가 입력하여 맞추는 게임
- 1~9까지의 숫자 3개를 컴퓨터가 난수로 발생
- ex) 127, 239, 563
- 중복되지 않는 숫자로 발생
"""
import random

answer = []
strike, ball = 0, 0
count = 0

# 중복되지 않는 랜덤함수 생성
while len(answer) < 3:
    random_num = random.randint(0, 9)
    if random_num not in answer:
        answer.append(random_num)

# print(answer)


while (1):
    num = input("Please input the number(Exit : q) : ")
    count += 1

    # 입력할때마다 초기화
    ball = 0
    strike = 0

    if(num == 'q'):
        break

    else:
        num = list(num)

        for idx, n in enumerate(num):
            if int(n) in answer:
                if int(n) == answer[idx]:
                    strike += 1
                else:
                    ball += 1
            
        print("{} 스트라이크, {} 볼\n".format(strike, ball))

        if(strike == 3):
            print("정답입니다! %d번만에 맞추었습니다!!" % count)
            break

