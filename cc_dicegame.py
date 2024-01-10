import random

high_score = 0

def dice_game():
    return random.randint(1, 6)

while True:
    print(f"""
Current High score: {high_score}
1) Roll Dice
2) Leave Game""")
    choice = input("Enter your choice: ")
    if choice == "2":
        break
    print()
    
    x1 = dice_game()
    print(f"You roll a... {x1}")
    x2 = dice_game()
    print(f"You roll a... {x2}\n")
    x=x1+x2
    print(f"You have rolled a total of: {x}")

    if high_score < x:
        high_score=x
        print()
        print("New high score!")

print("Goodbye!")
