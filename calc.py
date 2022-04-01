"""
num1=int(input("Frist Oprends :- "))
num2=int(input("Second Oprends :- "))
oprt=input("Select Opraters +,-,*,and/ :- ")
if oprt=="+":                                 
    print('----',num1+num2,'----')
elif oprt=="-":
    print('----',num1-num2,'----')
elif oprt=="*":
    print('----',num1*num2,'----')
elif oprt=="/":
    print('----',num1/num2,'----')
else:
    print("\n--PLEACE SELECT OPREATERS--")
"""

#------------------------------------------------------------------------------------------------

#print(eval(input("Enter your full Question : ")))

#------------------------------------------------------------------------------------------------

def add(a,b):
    c=a+b
    print(c)

def sub(a,b):
    c=a-b
    print(c)

def mul(a,b):
    c=a*b
    print(c)

def div(a,b):
    c=a/b
    print(c)

a=int(input("Enter No.1 :"))
b=int(input("Enter No.2 :"))
op=input("Choose Operaters :")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)
else:
    print("---Invalid---")

#------------------------------------------------------------------------------------------------
