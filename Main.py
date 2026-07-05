# snack, Water, Gun Game
import random

def get_user_choice():
    choice = input("Enter your choice (snack, water, gun): ").lower()
    while choice not in ["snack", "water", "gun"]:
        print("Invalid choice. Please enter snack, water, or gun.")
        choice = input("Enter your choice (snack, water, gun): ").lower()
    return choice

def get_computer_choice():
    return random.choice(["snack", "water", "gun"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "snack" and computer_choice == "water") or \
         (user_choice == "water" and computer_choice == "gun") or \
         (user_choice == "gun" and computer_choice == "snack"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to the Snack, Water, Gun Game!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()