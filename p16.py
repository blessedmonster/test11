def f(student1, student2):
    grades1 = [int(g) for g in student1.split(",")]
    grades2 = [int(g) for g in student2.split(",")]
    
    avg1 = sum(grades1) / len(grades1)
    avg2 = sum(grades2) / len(grades2)
    
    if avg1 > avg2:
        return 1
    elif avg2 > avg1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    print(f("3,4,5", "4,3"))
    print(f("3,4,5", "5,5,4,5"))
    print(f("3,4,5,4", "4,4"))
