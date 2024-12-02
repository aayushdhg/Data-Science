def factorial(n):
    if (n>1):
        return n*factorial(n-1)
    else:
        return 1

n=int(input("Enter a whole number: "))
print(factorial(n))