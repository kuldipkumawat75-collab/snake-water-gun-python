import random

choices = ["snake", "water", "gun"]

print("===== SNAKE WATER GUN GAME =====")
print("1. Snake")
print("2. Water")
print("3. Gun")

while True:
    user = input("\nEnter your choice (snake/water/gun): ").lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("Your choice:", user)
    print("Computer's choice:", computer)

    if user == computer:
        print("It's a Draw!")

    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        print("You Win!")

    else:
        print("Computer Wins!")

    play_again = input("\nPlay again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break

