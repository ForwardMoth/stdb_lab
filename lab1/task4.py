def foo():
    text = input("Enter your text: ")
    max_text_sequence = ""
    n = len(text)

    for i in range(n):
        if text[i].upper() == text[i] and text[i].isalpha():
            needed_text = text[i]
            for j in range(i+1, n):
                if text[j].isalpha():
                    needed_text += text[j]
                else:
                    break

            if len(max_text_sequence) < len(needed_text):
                max_text_sequence = needed_text

    print(max_text_sequence)

if __name__ == '__main__':
    foo()
