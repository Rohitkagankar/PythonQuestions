num=input("enter the num to check armstrong no: ")
a=[]

for i in num:a.append(i)
print(a)
add=0
for i in a:
    j=int(i)**len(num)
    print(f"{i} to power {len(num)} is:{j}")
    add=add+j
print("sum of powers is:",add)
if add==int(num):
    print("the num is armstrong number.")
else:
    print("the num is not armstrong number.")