import random

Computer = random.randint(1, 100)

Player = input("Enter a number between 1-100: ")
Player = int(Player)

if Player == Computer:
    print("You guessed correctly.")
else:
    print("You didn't guessed correctly.")

print("The number was:", Computer)

# Starte mit "Yes", damit die Schleife überhaupt losgeht
choice = "Yes"

while choice == "Yes":
    Computer = random.randint(1, 100)
    Player = input("Enter a number between 1-100: ")
    Player = int(Player)
    
    if Player == Computer:
        print("You guessed correctly!")
    else:
        print("You didn't guessed correctly.")
    print("The number was:", Computer)
    
    choice = input("Do you wanna try again? (Yes/No): ")