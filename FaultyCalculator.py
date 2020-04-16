# Faulty Calculator

# 45 * 3 = 345 \\ 78/9 = 67\\ 67+78 = 678

print("Enter First Number For Calculation")
num1 = int(input())
print("Enter second Number For Calculation")
num2 = int(input())
print("Enter operator  For Calculation")
operator = input()

if operator=="*":
    if num1==45 and num2==3 or num2==45 and num1==3:
        ans = 345
        print("Multiplication is",ans)
    else:
        print("Multiplication is",num1*num2)
elif operator=="+":     
    if num1==67 and num2==78 or num1==78 and num2==67:
        ans = 678
        print("Addition is",ans)
    else:
        print("Addition is",num1+num2)
elif operator=="/":
    if num1==78 and num2==9 or num1==9 and num2==78:
        ans = 6723
        print("division is",ans)
    else:
        print("division is",num1/num2)
            
