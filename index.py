import random

print("\nWelcome in game 'Guess Number'!")
print("\nI think about number 1-100")
print("Try to guess it\n")

the_number = random.randint(1, 100)
guess = int(input("This number is: "))
tries = 1

while guess != the_number:
    if guess > the_number:
        print("Too high...")
    else:
        print("Too small...")

guess = int(input("This number is: "))
tries += 1

print("Congratulations!")
print("This number is", the_number)
print("To make success you need only", tries, "tries!\n")

input("Press Enter to exit")