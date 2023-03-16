#Write a program to check whether a given number is a palindrome or not.

n = int(input("Enter a number:"))
y=0
temp=n
while(temp>0):
    x=temp%10
    y=(y*10)+x
    temp=temp//10

if(n == y):
    print(n,"is a palindrome number")
else:
    print(n,"is not a palindrome number")