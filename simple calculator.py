
def Addition(a,b):
    result=a+b
    print("a+b = ",result)

def Subraction(a,b):
    result=a-b
    print("a-b = ",result)

def Multiplication(a,b):
    result=a*b
    print("a*b = ",result)

def Division(a,b):
    result=a/b
    print("a/b = ",result)

a=int(input("Enter The First Number: "))
optr=input("Enter The Operator: ")
b=int(input("Enter The Second Number: "))

if optr=="+":
    Addition(a,b)
elif optr=="-":
    Subraction(a,b)
elif optr=="*":
    Multiplication(a,b)
elif optr=="/":
    Division(a,b)
else:
    print("Invalid Operator:?")    
