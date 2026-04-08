import random

cointosslist = []
cn = []
cnt = 1  

for i in range(20):
    cointosslist.append(random.randint(0, 1))

for j in range(1, 20):
    if cointosslist[j] == cointosslist[j - 1]:
        cnt += 1
    else:
        cn.append(cnt)
        cnt = 1  

cn.append(cnt)

print("coin toss list = ", cointosslist)
print("max consecutive length =", max(cn))