#Write a program to ﬁnd the sum of all even numbers between 1 to n 

n = int(input("Enter the number:"))
sum=0
for i in range(0,n+1):
    if(i%2==0):
        sum=sum+i
print("Sum of even number between 1 and",n,"is",sum)