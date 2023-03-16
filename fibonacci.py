#Write a program to print the Fibonacci series. 

n=int(input("Enter the number of terms:"))
a=0
b=1
print(a,b,end=" ")
for i in range(n-1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c