ip = int(input("Press 1,2 or 3 for executing the respective tasks\n"))

#Task1
if ip==1:
    r = float(input("Enter the radius of the circle:\n "))
    area = 3.14*r*r
    print("The area is:"+str(area))
#Task2
elif ip==2:
    n1 = int(input("Enter first number:\n"))
    n2 = int(input("Enter second number:\n"))
    case_1 = (n1>n2)
    case_2 = (n1<n2)
    case_3 = (n1==n2)
    print("First number is greater than second:",case_1)
    print("First number is lesser than second:",case_2)
    print("First and second numbers are equal:",case_3)
#Task3
else:
    num = float(input("Enter a number:\n"))
    sq = num**2
    cube = num**3
    print("The square is:"+str(sq)+"\n"+"The cube is:"+str(cube))