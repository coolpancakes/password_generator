# Simple password generator.

import random
import string

def main():
    length = 14
    password = ""

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    special_characters = string.punctuation
    numbers = string.digits

    combined = uppercase + lowercase + special_characters + numbers
    for combo in range(length):
        combo_choice = random.choice(combined)
        password += combo_choice

    print("Your generated password: {}".format(password))

if __name__ == "__main__":
    main()


