#Palindrome checker
'''def isPalindrome():
    str = input("Enter a string to check:")
    rev = str[::-1]
    if str==rev:
        print("It's a Palindrome")
    else:
        print("Sorry,it isn't a Palindrome")'''
def isPalindrome():
    str = input("Enter a string to check:")
    rev=''
    for c in str:
        rev = c+rev
    if str == rev:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
#Factorial
def calcFactorial(num):
    fact=1
    if num<0:
        return -1
    else:
        for i in range(1,num+1):
                fact*=i
    return fact
ip = int(input("Enter 1 for Palindrome and 2 for factorial\n"))
if ip==1:
    isPalindrome()
else:
    n = int(input("Enter a number to get your factorial\n"))
    ans = calcFactorial(n)
    print("The factorial is:"+str(ans)+"!Thanks and have nice day!")