alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


status = input("Type decode or encode: ")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def split(word):
    return [char for char in word]


def encrypt(text, shift):
    x = split(text)
    for i in range(len(x)):
        place = int(alphabet.index(x[i]))
        x[i] = alphabet[place + shift]
    print("".join(x))


def decrypt(text, shift):
    x = split(text)
    for i in range(len(x)):
        place = int(alphabet.index(x[i]))
        x[i] = alphabet[place - shift]
    print("".join(x))


if status == "encode":
    encrypt(text, shift)

if status == "decode":
    decrypt(text, shift)
