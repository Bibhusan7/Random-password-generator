import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$!@*&%^({}"

while True:
    password_length = int(input("Length of password: "))
    password = ""
    for x in range(password_length):
        password_char = random.choice(chars)
        password += password_char
    print(f"your password: {password}")