# Python password Generator
import random
import string

def generate_password(length: int = 10):
    alphabets = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabets) for i in range(length))
    return password

password = generate_password()
print(f"Generate password: {password}")
