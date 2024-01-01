num=int(input("enter the number of terms here: "))

result=list(map(lambda x:2**x, range(num+1)))
#print(result)
for i in range(num+1):
    print(f"the value of 2 raised to power {i} is : {result[i]} ")