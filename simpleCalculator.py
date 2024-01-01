#program to make simple calculator---
a=int(input("enter the first number: "))
choice=input("enter the operation(+,-,*,/): ")
b=int(input("enter the seconf number: "))

if choice=="+":
    print(f"{a} {choice} {b} = {a+b}")
elif choice=="-":
    print(f"{a} {choice} {b} = {a - b}")
elif choice=="*":
    print(f"{a} {choice} {b} = {a * b}")
elif choice=="/":
    print(f"{a} {choice} {b} = {a / b}")
else:
    print("invalid input.")

