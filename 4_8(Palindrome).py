def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            print(f"{s} is not a palindrome word")
            return
    print(f"{s} is a palindrome word")

n = input("단어를 입력하세요: ")
palindrome(n)