import math

def f(tree_circumference):
    diameter = tree_circumference / math.pi
    return diameter >= 50

if __name__ == "__main__":
    print(f(200))
    print(f(100))
