import random

while True:
    top_number = input("enter a number:")
    if top_number.isdigit():
        top_number = int(top_number)

        if top_number <= 0:
            print("enter a number above 0")
        else:
            break
    else:
        print('enter a number only')

random_number = random.randint(0, top_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")