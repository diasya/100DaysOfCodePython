import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def kart_cek():
    return random.choice(cards)


def score(a):
    print("------------------------------------------------------")
    print(f"Your cards are: {your_cards} | Your score is {sum(your_cards)}.")
    if a == dealer_cards:
        print(f"Dealer's cards are: [{a}] | Dealer's score is {sum(dealer_cards)}.")
    else:
        print(f"Dealer's cards are: [{a}]")


def sit_check():
    if sum(your_cards) > 21:
        print("You Lost")
        return False
    elif sum(your_cards) == 21:
        print("BLACKJACK. You Won")
        return False
    else:
        return True


def sit_check_two():
    if sum(dealer_cards) > 21:
        print("You Won")
        return False
    elif sum(dealer_cards) > sum(your_cards):
        print("You Lost")
        return False
    elif sum(dealer_cards) < sum(your_cards):
        print("You Won")
        return False
    elif sum(dealer_cards) == sum(your_cards):
        print("Draw")
        return False
    else:
        return True


your_cards = []
dealer_cards = []

your_cards.extend((kart_cek(), kart_cek()))
dealer_cards.extend((kart_cek(), kart_cek()))

a = True
while a:
    score(dealer_cards[0])
    if not sit_check():
        break

    if input("press 'y to draw new card or 'n' to pass: ") == "n":
        while sum(dealer_cards) < 17:
            dealer_cards.append(kart_cek())
        if sum(your_cards) < 21:
            score(dealer_cards)
            if not sit_check_two():
                break
        score(dealer_cards[0])
        if not sit_check_two():
            break
    else:
        your_cards.append(kart_cek())
