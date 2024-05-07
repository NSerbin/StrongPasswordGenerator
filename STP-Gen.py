#!/usr/bin/env python
import argparse
import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
SPECIALCHARS = string.punctuation

def password_gen(length):
    characters = f"{LETTERS}{NUMBERS}{SPECIALCHARS}"
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Generate a strong random password.')
    parser.add_argument('-l', '--length', type=int, default=16,
                        help='Length of the password to generate. Default is 16 characters.')
    
    args = parser.parse_args()
    
    # Generate the password
    password = password_gen(args.length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
