def f(size1, size2):
    sizes = {"S": 1, "M": 2, "L": 3}
    if sizes[size1] > sizes[size2]:
        return 1
    elif sizes[size2] > sizes[size1]:
        return 2
    else:
        return 0

if __name__ == "__main__":
    print(f("L", "S"))
    print(f("M", "L"))
    print(f("S", "S"))
