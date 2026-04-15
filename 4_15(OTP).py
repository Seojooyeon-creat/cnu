import random
import string

def generate_otp():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase  
    digits = string.digits              
    symbols = string.punctuation        

    
    password = [random.choice(lowercase), random.choice(uppercase), random.choice(digits), random.choice(symbols)]

    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=4)

    random.shuffle(password)

    return ''.join(password)

otp = generate_otp()
print(f"생성된 OTP: {otp}")