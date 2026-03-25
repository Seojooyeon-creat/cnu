x = int(input("첫 번째 정수 입력:"))
y = int(input("두 번째 정수 입력:"))
z = int(input("세 번째 정수 입력:"))

if y > x and z > x:
    print(x)
elif x > y and z > y:
    print(y)
elif x > z and y > z:
    print(z)