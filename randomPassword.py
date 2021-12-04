import random
import string

characters = string.ascii_letters + string.punctuation  + string.digits
number = input('>>>[+]Number of passwords to be created: ')
number = int(number)
length = input('>>>[+]Enter the password length 8/24: ')
length = int(length)

if length <7 or length >25:
    print("The length must be between 8 and 24!")
else:
    for password in range(number):
        pw = ''
        for char in range(length):
            pw += random.choice(characters)
        print("[*]Password: ",pw)