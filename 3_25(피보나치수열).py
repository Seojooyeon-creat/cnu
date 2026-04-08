n = int(input("몇 번 항까지 구할까요?"))

a, b = 0, 1

for i in range(n + 1):
    print(a, end=" ")
    a, b = b, a + b