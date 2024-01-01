# #program to print sum of n natural numbers
# print("using for loop")
# num=int(input("enter the number to find the sum : "))
# sum=0
# for i in range(1,num+1):
#     sum=sum+i
# print(sum)
#
# #using while loop
# print("using while loop.")
# num=int(input("enter the number to find the sum : "))
# sum=0
# while num>0:
#     sum=sum+num
#     num-=1
# print(sum)

#using recursion------
print("using recursion")
n1=int(input("enter the num to print sum: "))
def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)


print("sum of natural no's upto given num is ",sum(n1))
