import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
nr_letters = int(input("How many letters do you want in your password: "))
nr_numbers = int(input("How many numbers do you want in your password: "))
nr_symbols = int(input("How many symbols do you want in your password: "))

dummy = 0
while dummy < nr_letters: