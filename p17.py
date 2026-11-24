def f(number):
    if number == 0 or number == 1:
        return True
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number

if __name__ == "__main__":
    print(f(5))
    print(f(4))
