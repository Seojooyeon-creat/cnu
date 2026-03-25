import random

x = random.randint(1, 3)

y = int(input("가위(1), 바위(2), 보(3) 중 하나를 입력하세요: "))



if x == y:
    print("비겼습니다.")
elif (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
    print("컴퓨터가 이겼습니다.")

else:
    print("당신이 이겼습니다.")
        
