ip = int(input("Enter 1 or 2 for the respective tasks\n"))
#Task1
if ip==1:
    year = int(input("Enter a year in AD:\n"))
    if (year%4==0 and year%100!=0) or year%400==0:
        print("It's a leap year")
    else:
        print("Not a leap year")
#Task2
else:
    print("Enter the sides of the triangle:\n")
    s1 = float(input("First side:\n"))
    s2 = float(input("Second side:\n"))
    s3 = float(input("Third side:\n"))
    if s1==s2 and s1==s3:
        print("It's an equilateral triangle")
    elif s1==s2 or s2==s3 or s1==s3:
        print("It's an isosceles triangle")
    else:
        print("Scalene triangle")

