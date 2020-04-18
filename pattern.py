# input any number n=no of rows
# boolean true pattern 
# *
# **
# ***
# ****


# boolean false pattern 
# ****
# ***
# **
# *

rows = int(input("Enter any number\n"))
num = int(input("Enter either 1 or 0"))
boolean = bool(num)


def patterndraw(n,boolean):
    if boolean==True:
        for i in range(0,n):
            for j in range(0,i+1):
                print("*",end="")
            print("\n") 


    elif boolean==False:
        for i in range(0,n):
            for j in range(0,n-i):
                print("*",end="")
            print("\n") 


patterndraw(rows,boolean)