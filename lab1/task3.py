alphabet = "abcdefghijklmnopqrstuvwxyz"


def foo():
    text, number = input("Enter your text: "), int(input("Enter number: "))
    new_text = ""
    for ch in text:
        new_pos = alphabet.find(ch) + number
        if ch in alphabet:
            new_text += alphabet[new_pos]
        else:
            new_text += ch
    return new_text, number


def decoding_text(text, number):
    old_text = ""
    for ch in text:
        old_pos = alphabet.find(ch) - number
        if ch in alphabet:
            old_text += alphabet[old_pos]
        else:
            old_text += ch
    print("Decoded text:", old_text)


if __name__ == '__main__':
    coded_text, number = foo()
    print("Coded text ", coded_text)
    decoding_text(coded_text, number)
