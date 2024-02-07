ip = int(input("Press 1 or 2:\n"))
#Task1
if ip == 1:
    name = input("Enter your name:\n")
    age = int(input("Enter your age:\n"))
    roll_number = int(input("Enter your roll number:\n"))
    phone_number = int(input("Enter your phone number:\n"))
    print("Your name is:",name, "\n"+"Your roll number is:",roll_number,"\n"+"Your age is:",age,"\n"+"Your phone number is:",phone_number)
#Task2
else:
    num = int(input("Enter a number to get the table:\n"))
    print(f"{num}x1 = {num*1}")
    print(f"{num}x2 = {num*2}")
    print(f"{num}x3 = {num*3}")
    print(f"{num}x4 = {num*4}")
    print(f"{num}x5 = {num*5}")
    print(f"{num}x6 = {num*6}")
    print(f"{num}x7 = {num*7}")
    print(f"{num}x8 = {num*8}")
    print(f"{num}x9 = {num*9}")
    print(f"{num}x10 = {num*10}")