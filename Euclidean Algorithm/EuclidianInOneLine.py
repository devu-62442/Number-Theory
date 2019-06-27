#Recursive Method
def euc(a,b):
    #Euclideans One Line Logic
    euc(b,a%b) if(a%b!=0) else print("\nThe greatest Common Divisor is: "+str(b))

# num1 and num2 are the two numbers to find the GCD for
num1=int(input("\nEnter the first number:"))
num2=int(input("Enter the second number:"))

#Checking the greater number
if(num1<num2):
    num2=num1+num2
    num1=num2-num1
    num2=num2-num1

#Calling the Recursive Euclidean Method
euc(num1,num2)

