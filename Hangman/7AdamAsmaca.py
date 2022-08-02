import random
from hangman_art import stages
from hangman_words import word_list

chosen_word = random.choice(word_list)

word = []
for x in range(len(chosen_word)):
  word.append("-")
lives = 6

while "-" in word:
    guessDum = input("Guess a letter: ").lower()
    guess = []
    guess.append(guessDum)
    a = -1
    b = False
    for letter in chosen_word:
        a += 1
        if letter == guess:
            word[a] = letter
            b = True
    print(word)
    if not b:
        lives -= 1

    print(stages[lives])
    if lives == 0:
        print("YOU LOST")
        break
print("YOU WON")

