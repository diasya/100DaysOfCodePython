from Data import data
import random


def print_celeb(osman):
    for key in osman:
        if key == "name" or key == "description":
            print(osman[key], end=", ")
        if key == "follower_count":
            continue
        if key == "country":
            print(osman[key], end=". ")


def higher_one():
    if first["follower_count"] > second["follower_count"]:
        return "a"
    else:
        return "b"


score = 0
while True:
    first = data[random.randint(0, 49)]
    second = data[random.randint(0, 49)]

    print("A", end=": ")
    print_celeb(first)
    print("\nVS.")
    print("B", end=": ")
    print_celeb(second)

    guess = input("\nWhich has more follower do you think? 'A' or 'B': ").lower()

    if guess == higher_one():
        score += 1
        print("---------------------------")
        print(f"You've guessed right. {first['name']}: {first['follower_count']}M and {second['name']}: "
              f"{second['follower_count']}M | Your score is {score}")
    else:
        print(f"\nYou've guessed wrong. {first['name']}: {first['follower_count']}M and {second['name']}: "
              f"{second['follower_count']}M | You finished the game with Score: {score}")
        break

