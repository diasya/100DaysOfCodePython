import random

number = random.randint(1, 100)

a = input("Type 'easy' or 'hard' to choose difficulty: ")
if a == "easy":
    dif = 10
else:
    dif = 5

for attempt in range(dif, -1, -1):
    for _ in f"You have {attempt} attempts remained.":
        print("-", end="")
    print(f"\nYou have {attempt} attempts remained.")
    guess = int(input("Make a guess: "))

    if guess == number + 1:
        print("You're high")
    elif guess == number - 1:
        print("You're low")
    elif guess > number:
        print("You're too high")
    elif guess < number:
        print("You're too low")
    else:
        print(f"You guessed right. The answer was {number}")
        break
