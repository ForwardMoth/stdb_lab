
def foo():
    a = int(input("Enter your number: "))
    sum = 0
    while a != 0:
        sum += a % 10
        a //= 10
    print("Result:", sum)

if __name__ == '__main__':
    foo()
