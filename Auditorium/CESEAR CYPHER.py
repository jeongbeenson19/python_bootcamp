alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, plain_shift):
    word_in_process = ""
    for letter in plain_text:
        position = alphabet.index(letter) + plain_shift
        if position > 25:
            position = position - 26
        new_letter = alphabet[position]
        word_in_process += new_letter
    print(word_in_process)

def decrypt(plain_text, plain_shift):
    word_in_process = ""
    for letter in plain_text:
        position = alphabet.index(letter) - plain_shift
        if position < 0:
            position = position + 26
        new_letter = alphabet[position]
        word_in_process += new_letter
    print(word_in_process)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("error")