# Password generator project no 02
# a tool that automatically creates strong, random, and hard-to-guess password

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
           ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~']

print("Welcome to password generator.")
nlet = int(input("How many letters you want in your password?\n"))
nnum = int(input("How many numbers you want in your password?\n"))
nsym = int(input("How many symbols you want in your password?\n"))

password =[]

for i in range(0,nlet +1) :    # This is used to make i/p add in the empty list password
    char = random.choice(letters)
    password += char

for i in range(0,nnum +1) :
    char = random.choice(numbers)
    password += char

for i in range(0,nsym +1) :
    char = random.choice(symbols)
    password += char

random.shuffle(password)
pasl = ""
for i in password : # This is used to convert password from list to a char format 
    pasl += i

print(f"The generated password is {pasl}")
