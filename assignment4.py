ip = int(input("Enter 1 or 2 for the respective tasks:\n"))
#1.Factorial
if ip==1:
    num = int(input("Enter an integer:\n"))
    fact=1
    if num<0:
        print("Invalid input")
    else:
        for i in range(1,num+1):
            fact*=i
        print("The factorial is",fact)
else:
#2.Fibonacci
    n = int(input("Enter the number of terms:\n"))
    a,b = 0,1
    print("The series is:")
    for i in range(0,n):
        print(a,end=" ")
        a,b=b,a+b