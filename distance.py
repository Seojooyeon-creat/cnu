import math

x1 = int(input("첫 번째 점의 x 좌표 입력:"))
y1 = int(input("첫 번째 점의 y 좌표 입력:"))
x2 = int(input("두 번째 점의 x 좌표 입력:"))
y2 = int(input("두 번째 점의 y 좌표 입력:"))

print("===")

print("두 점 사이의 거리:", math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), "입니다.")


