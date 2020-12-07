#!/usr/bin/env python
import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
SPECIALCHARS = string.punctuation

def passwordGen(length):
    password = list(f"{LETTERS}{NUMBERS}{SPECIALCHARS}")
    random.shuffle(password)
    randomPassword = random.choices(password, k=length)
    randomPassword = ''.join(randomPassword)
    print(randomPassword) 

def menu():
    opt_continue = "yes"
    while opt_continue == "yes":
        print("====================================================================")
        print("Welcome to the Strong Password Generator")
        print("====================================================================")
        print("This script will generate random passwords to make them more strong.")
        print("It will includes Letters, Numbers and Special Characters.")
        print("Remember DONT SHARE YOUR PASSWORDS...")
        print("====================================================================")
        print("Please choose an option:")
        print("====================================================================")
        print("[*] 1. 16 Characters password.")
        print("====================================================================")
        print("[*] 2. 20 Characters password")
        print("====================================================================")    
        print("[*] 3. 24 Characters password")
        print("====================================================================")
        print("[*] 4. Exit")
        option = input("")
        if option == '1':
            passwordGen(16)
        elif option == '2':
            passwordGen(20)
        elif option == '3':
            passwordGen(24)
        elif option == '4':
            exit()
        else:
            raise ValueError("WRONG OPTION\nPlease choose between 1 to 4...")
        opt_continue = input("Wanna make more passwords?\nyes/no")
menu()