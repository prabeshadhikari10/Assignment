#Write a program to ﬁnd the sum of natural numbers entered by the user

n = int(input("Enter the number:"))
sum=0
for i in range(0,n+1):
    sum=sum+i
print("The sum of ",n,"is",sum)