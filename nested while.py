# Write a program print the following pattern using while loop
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
i=1
while(i<6):
    j=1
    while(j<=i):
        print(j,end = ' ') 
        j+=1
    print()
    i+=1