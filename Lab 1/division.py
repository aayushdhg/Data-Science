def divide(n1, n2):
    try:
        n3 = n1 / n2
        return n3
    except ZeroDivisionError:
        return "Error: Division by zero is forbidden!"

a = 10
b = 0
print(f"{divide(a,b)}")
b = 2
print(f"{divide(a,b)}")
