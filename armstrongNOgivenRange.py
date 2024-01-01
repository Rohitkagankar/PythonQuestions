#program to find armstrong numbers in given range
lower=int(input("enter the lower limit: "))
upper=int(input("enter the upper limit: "))

for num in range(lower,upper+1):
    temp=num
    sum = 0
    while temp>0:
        digit=temp%10
        sum+=digit**len(str(num))
        temp//=10
    if num==sum:
        print(num)
#another logic---------
print("--------------------------")
lower=int(input("enter the lower limit: "))
upper=int(input("enter the upper limit: "))

for num in range(lower,upper+1):
    a = []
    for i in str(num): a.append(i)
    add = 0
    for i in a:
        j = int(i) ** len(str(num))
        add = add + j
    if add == int(num):
        print(f"the {num} is armstrong number.")
