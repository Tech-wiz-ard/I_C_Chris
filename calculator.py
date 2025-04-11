# Welcoming the user

print("Welcome to Basic Calculator!\n")
print("Available operations:\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division\n")

# Operation choosing

operation = input("Enter any operation of your choice between 1,2,3,4 :")

# Results formation

if operation == "1":
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    print("Results :\n",num1,"+",num2,"=",num1+num2)
elif operation == "2":
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    print("Results :\n",num1,"-",num2,"=",num1-num2)
elif operation == "3":
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    print("Results :\n",num1,"*",num2,"=",num1*num2)
elif operation == "4":
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    if num2 != 0 :
        print("Results :\n",num1,"/",num2,"=",num1/num2)
    else :
        print("Math error!")
else :
    print("Invalid input!")