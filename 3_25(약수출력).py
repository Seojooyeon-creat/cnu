n = int(input("정수를 입력하세요:"))
for i in range(n):
    if n % (i + 1) == 0:
        print(i+1, end=" ")
    else:
        continue
