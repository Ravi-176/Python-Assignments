#Task1-Anagram
def isAnagram(str1,str2):
    if len(str1)!=len(str2):
        print("Not an anagram")
    else:
        if sorted(str1)==sorted(str2):
            print("It's an anagram")
        else:
            print("Not an anagram")

#Task2-Counting vowels and consonants in a string
def count(st):
    vowelCnt=0
    consonantCnt=0
    for ch in st:
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            vowelCnt+=1
        else:
            consonantCnt+=1
    print("The vowel count is:"+str(vowelCnt)+"\n"+"The consonant count is:"+str(consonantCnt))
#Task3-Find substring in a string
def findSubstr(str1,subStr):
    if str1.find(subStr)==-1:
        print("Substring not found")
    else:
        print("Substring is present")
ip = int(input("Enter 1,2 or 3 for the respective tasks:\n"))
if ip==1:
    str1 = input("Enter first string:\n")
    str2 = input("Enter second string:\n")
    isAnagram(str1,str2)
elif ip==2:
    st = input("Enter a string:\n")
    count(st)
else:
    str1 = input("Enter the main string:\n")
    subStr = input("Enter the substring:\n")
    findSubstr(str1,subStr)