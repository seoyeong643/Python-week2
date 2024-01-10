# File Name: app.py
# About: This is an example of an ATM working with data types, functions, and package creation.
# 7/9/22

#from banking_pkg.account import *
from banking_pkg.account import show_balance, deposit, withdraw, log_out


def atm_menu(username):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + username)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


def header():
    print("          === Automated Teller Machine ===          ")


"""
Task 1: Register the user's name and PIN.
"""

header()
name = input("Enter name to register: ")

while True:
    pin = input("Enter four digit PIN: ")

    if not pin.isdigit():
        print("Your PIN is not numerical. Please use only numbers.")
        continue

    if len(pin) < 4:
        print("Your PIN is not long enough. Please create a four digit PIN")
        continue

    if len(pin) > 4:
        print("Your PIN is too long. Please create a four digit PIN")
        continue
    break


balance = 0

print(f"{name} has been created with a balance of: ${balance:.2f}")

"""
Task 2: Log in the user, or deny if PIN is invalid
"""

while True:
    header()
    print("LOGIN TO ACCESS THE ATM...")
    validation_name = input("Enter Username: ")
    validation_pin = input("Enter PIN: ")

    if name == validation_name and pin == validation_pin:
        print("Your Login is successful.")
        break

    print("Invalid Credential...")
    print()


"""
Task 3-5: Displays ATM menue and respons to user choice
"""

while True:
    atm_menu(name)
    menu_choice = input("Choose an option: ")

    if menu_choice == "1":
        show_balance(balance)
    elif menu_choice == "2":
        balance = deposit(balance)
        show_balance(balance)
    elif menu_choice == "3":
        balance = withdraw(balance)
        show_balance(balance)

    elif menu_choice == "4":
        log_out_validation = log_out(name)
        if log_out_validation == "y":
            quit()

    else:
        print("Invalid response. Please choose a number between 1-4")
