def tentotwo(n):
    result = []
    while n > 1:
        k = n % 2
        n = n // 2
        result.append(str(k))  # str로 변환
    result.append(str(n))
    result.reverse()
    return ''.join(result)  # 문자열로 합치기

n = int(input("10진수 입력: "))
print("2진수는", tentotwo(n), "입니다")