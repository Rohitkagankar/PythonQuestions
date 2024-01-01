#program to find prime no

num=int(input("enter the no: "))
for i in range(2,num):
    if num ==1:
        print("Not a prime number.")
        break
    elif num % i==0:
        print("Not a prime number.")
        break
    else:
        print("Number is prime.")
        break

##prime no's in given range:

lower=int(input("enter the lower limit here: "))
upper=int(input("enter upper limit here: "))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)