def show_balance(balance):
    print(f"Your current balance is ${balance:.2f}")


def deposit(balance):
    while True:
        deposit_amount = input("Enter amount to deposit: ")
        try:
            float(deposit_amount)
        except ValueError as bad_data:
            print(bad_data, "You must enter a dollar amount.")
            continue

        if float(deposit_amount)>0:
            return balance + float(deposit_amount)
        print("You must deposit an amount greater than $0.00 dollars")

    
def withdraw(balance):
    while True:
        withdraw_amount = input("Enter an amount to withdraw: ")
        try:
            float(withdraw_amount)
        except ValueError as bad_data:
            print(bad_data, "You must enter a dollar amount.")
            continue

        #user should not be able to withdraw more than the amount of their balance
        if float(withdraw_amount) <= balance:
            return balance - float(withdraw_amount)
        print("The amount you want to withdraw is more than your balance.")

    
   

def log_out(name):
    logout_varify = input("Are you sure you want to log out?: (Y?N) ")
    if logout_varify[0].lower() == "y":
        print(f"Thank you {name}. Have a great day.")
    
    return logout_varify.lower()
