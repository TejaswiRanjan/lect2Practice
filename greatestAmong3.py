#WAP to find the greatest of 3 number numbers entered by the user.

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

if(num1>num2 and num1>num3):
    print(num1 ," : is the greatest number")
elif(num2>num1 and num2>num3):
    print(num2 ," : Second is the greatest number")
elif(num3>num1 and num3>num2):
    print(num3 ," : Third number is greatest number")
else:
    print("MAy be you entered two  or all equal numbers")