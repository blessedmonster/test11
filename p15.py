def f(a, b):
    total = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            total += i
    return total

if __name__ == "__main__":
    print(f(1, 6))
    print(f(2, 10))
