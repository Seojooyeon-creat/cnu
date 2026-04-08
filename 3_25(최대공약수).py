n = int(input("첫번째 정수 입력: "))
m = int(input("두번째 정수 입력: "))

dir = 1
for k in range(1, min(n, m) + 1):
    if n % k == 0 and m % k == 0:
        dir = k

print("최대공약수는", dir, "입니다")