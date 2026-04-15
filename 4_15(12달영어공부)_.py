kotoen = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
month = input("숫자 입력 (1~12):")
if month in kotoen:
    print("해당 달:", kotoen[month])
else:    
    print("1에서 12 사이의 숫자를 입력하세요.")