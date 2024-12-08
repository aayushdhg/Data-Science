n = int (input ("How many terms from the Fibonacci series would you like to see? "))
a,b=0,1
for i in range (1,n+1):
    print(a,end=' ')
    c=a+b
    a,b=b,c

