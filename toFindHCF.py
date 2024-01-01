#program to find HCF
n1=int(input("enter the first number: "))
n2=int(input("enter the second number: "))

def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x

    for i in range(1,smaller+1):
        if(x%i==0 and y%i==0):
            hcf=i
    return hcf
print("the hcf of given two numbers is ",hcf(n1,n2))