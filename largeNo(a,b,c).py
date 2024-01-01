#program to find out largest no from three no's
a=int(input("enter first no: "))
b=int(input("enter second no: "))
c=int(input("enter third no: "))

if(a>b) and (a>c):
    print(a,"is large")
elif(b>a) and (b>c):
    print(b,"is large")
else:
    print(c,"is large")