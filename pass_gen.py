import random

lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

def password_generator():
    ch = int(input("Enter the length of the password to be generated: "))

    # Ensure the password length is at least 8 
    if ch < 8:
        print("Password length should be at least 8 characters.")
        return
        

    passw = ""

    for i in range(ch - 4):  # Use ch - 4 to account for 1 uppercase, and 3 symbol requirements
        passw += lowercase_letters[random.randint(0, 25)]

    passw += lowercase_letters[random.randint(0, 25)].upper()

    for i in range(3):
        passw += symbols[random.randint(0, 7)]

    passw_list = list(passw)
    random.shuffle(passw_list)
    shuffled_passw = ''.join(passw_list)

    print("Your generated password is",shuffled_passw)

    cho=input("Do you want to re-generate the pass ? yes/no: ")

    if cho.lower()=="yes":
        password_generator()
    else:
        print("Thanks for using the program")

password_generator()
