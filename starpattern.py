#Write a program to print the following pattern:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for x in range(1,6):
    y=1
    for y in range(1,x+1):
        print("*",end = ' ')
    print()
for x in range(6,1,-1):
    y=1
    for y in range(1,x-1):
        print("*",end = ' ')
    print()