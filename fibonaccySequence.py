#fibonaccy sequence
a=0
b=1
num=int(input("enter the num to obtain fibonaccy sequence: "))
if num==0:
    print(a)

else:
    print(a)
    print(b)
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c)

#using recursion------
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-2)+fibo(n-1)
n=int(input("enter the number here: "))
if n<=0:
    print("enter the positive number.")
else:
    print("fibonacy sequence ")
    for i in range(n):
        print(fibo(i))