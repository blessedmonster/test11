def f(product_code):
    digits_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    check_digit = digits_sum % 7
    return check_digit == int(product_code[3])

if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))
