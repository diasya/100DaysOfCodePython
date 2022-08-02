alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def split(word):
    return [char for char in word]


def encrypt(text, shift, direction):
    x = split(text)
    if shift > 26:
        shift = shift % 26

    for i in range(len(x)):
        if x[i] not in alphabet:
            continue
        place = int(alphabet.index(x[i]))
        if direction == "encode":
            x[i] = alphabet[place + shift]
        if direction == "decode":
            x[i] = alphabet[place - shift]
    print("Message:")
    print("".join(x))


while True:
    status = input("\nType decode or encode: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    encrypt(text, shift, status)
    more = input("\nYou want to do one more time. yes or no: ")
    if more == "no":
        print("Goodbye")
        break
