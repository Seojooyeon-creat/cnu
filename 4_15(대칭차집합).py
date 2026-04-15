A = set(map(int, input("A 입력 :").split()))
B = set(map(int, input("B 입력 :").split()))

ch = A & B
ch1 = A - ch
ch2 = B - ch

chto = ch1 | ch2

print("대칭차집합:", chto)