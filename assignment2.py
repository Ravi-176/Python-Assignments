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
    if n1>n2:
        print("First number is greater")
    elif n1<n2:
        print("First number is lesser")
    else:
        print("Both are equal")
#Task3
else:
    num = float(input("Enter a number:\n"))
    sq = num*num
    cube = num*num*num
    print("The square is:"+str(sq)+"\n"+"The cube is:"+str(cube))