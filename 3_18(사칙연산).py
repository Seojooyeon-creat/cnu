import random

x = random.randint(1, 100)
y = random.randint(1, 100)
operator = random.choice(["+", "-", "*", "/"])

print(f"{x} {operator} {y} =")

z = int(input("정답을 입력하세요: "))

if operator == "+":
    if z == x + y:
        print("정답입니다.")
    else:
        print("틀렸습니다.")

elif operator == "-":
    if z == x - y:
        print("정답입니다.")
    else:
        print("틀렸습니다.")

elif operator == "*":
    if z == x * y:
        print("정답입니다.")
    else:
        print("틀렸습니다.")

elif operator == "/":
    if z == x / y:
        print("정답입니다.")
    else:
        print("틀렸습니다.")


    
