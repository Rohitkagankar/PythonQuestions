print("print no's divisible by given number.")
num=int(input("enter the number:"))
print(f"numbers divisible by {num} in range upto 100")

for i in range(1,101):
    if i %num ==0:
        print(i)
print("using lamda funtion------")
result=list(filter(lambda x: x% num==0,range(1,101)))
#print(result)
for i in result:
    print(i)