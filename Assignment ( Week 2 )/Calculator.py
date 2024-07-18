# Code for Simple Calculator

# Method to perform Additon Operation
def addition(a,b):
    print("Addition of ",a," and ",b," is : ",a+b)

# Method to perform Subtraction Operation
def subtraction(a,b):
    print("Subtraction of ",a," and ",b," is : ",abs(a-b))

# Method to perform Multiplication Operation
def multiplication(a,b):
    print("Multiplication of ",a," and ",b," is : ",a*b)

# Method to perform Division Operation
def division(a,b):
    res=0
    if a>=b: res=a/b
    else: res=b/a
    print("Division of ",a," and ",b," is : ",res)

# Method to perform Floor Division Operation
def floorDivison(a,b):
    res=0
    if a>=b: res=a//b
    else: res=b//a
    print("Floor Division of ",a," and ",b," is : ",res)

# Method to perform Remainder Operation
def remainder(a,b):
    res=0
    if a>=b: res=a%b
    else: res=b%a
    print("Remainder after performing division of ",a," and ",b," is : ",res)

# Method to perform Exponentiation Operation 
def exponentiation(a, b):
    print("Exponentiation of ", a, " to the power ", b, " is : ", a ** b)

# Main Method to call all the above methods according to requirement
def main():
    run=True
    while(run):
        # Menu Options
        print("Options :")
        print("---------------------------------")
        print("Enter 1 for Addition(+) ")
        print("Enter 2 for Subtraction(-) ")
        print("Enter 3 for Multiplication(x) ")
        print("Enter 4 for Divison(/) ")
        print("Enter 5 for Floor Division(//) ")
        print("Enter 6 for Remainder(%) ")
        print("Enter 7 for Exponent(^) ")
        print("Enter 8 to Exit")
        print("---------------------------------")
        choice=int(input("Enter your Choice : "))
        a=0
        b=0
        # Handling Edge Cases
        # If the user choices are not between(1-7) then taking the input is irrelevant
        if(choice>=1 and choice<=7):
            print("---------------------------------")
            a=int(input("Enter the First Number : "))
            b=int(input("Enter the Second Number : "))
            print("---------------------------------")
        if choice==1:addition(a,b)
        elif choice==2:subtraction(a,b)
        elif choice==3:multiplication(a,b)
        elif choice==4:division(a,b)
        elif choice==5:floorDivison(a,b)
        elif choice==6:remainder(a,b)
        elif choice==7:exponentiation(a,b)
        elif choice==8:
            print("Program  Terminated : Run the program again to perform the Operations(+,-,x,/,//,%,^)")
            break
        else:
            print("Invalid Option Opted !")
        print("---------------------------------")
        print("Do you want to perform calculation again ? ")
        ch=input("Enter your choice( y/n ) : ")
        if(ch=='y'):run=True
        else:
            print("Program  Terminated : Run the program again to perform the Operations(+,-,x,/,//,%)")
            run=False

# calling the above main method
main()

