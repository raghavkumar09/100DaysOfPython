
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['1','2','3','4','5','6','7','8','9','10']

symbols = ['!','@','#','$','%','&','?']

print("Welcomre to the password generator prograam")

ltr = int(input("How many letter would you like in your password\n"))
num = int(input("How many number would you like in your password\n"))
sbl = int(input("How many symbols would you like in your password\n"))

          #easy level
# password = ""

# for char in range(1, ltr+1):
#     password += random.choice(letters)

# for char in range(1, num+1):
#     password += random.choice(numbers)

# for char in range(1, sbl+1):
#     password += random.choice(symbols)
# print(password)

#            Hard level

password_list = []

for char in range(1, ltr+1):
    password_list += random.choice(letters)

for char in range(1, num+1):
    password_list += random.choice(numbers)

for char in range(1, sbl+1):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(password)
