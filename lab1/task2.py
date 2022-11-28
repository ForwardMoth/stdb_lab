def is_palindrom(n):
    return str(n) == str(n)[::-1]


def foo():
    a = int(input("Enter your number: "))
    i = 0
    while i < 10:
        if is_palindrom(a):
            print("Palidrom number:", a)
            return
        else:
            a = int(a) + int(str(a)[::-1])
        i += 1
    print("It is impossible!")


if __name__ == '__main__':
    foo()
