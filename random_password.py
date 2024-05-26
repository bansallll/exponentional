import random
import string

p=int(input("enter password length"))
k=string.ascii_letters+ string.digits +string.punctuation

password=""
for i in range(p):
    password+=random.choice(k)

print("Your random password is :",password)