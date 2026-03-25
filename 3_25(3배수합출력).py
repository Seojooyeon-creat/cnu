count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += i

print("1부터 100사이의 모든 3의 배수의 합은", count, "입니다")