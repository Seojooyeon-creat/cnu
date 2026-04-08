
def gcd(n, m):


    dir = 1
    for k in range(1, min(n, m) + 1):
        if n % k == 0 and m % k == 0:
            dir = k

    return dir

n = int(input("첫 번째 정수를 입력하세요:"))
m = int(input("두 번째 정수를 입력하세요:"))

print("최대공약수는", gcd(n, m), "입니다")