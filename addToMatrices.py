A=[[4,5,7],[2,6,5],[8,4,2]]
B=[[5,6,2],[1,3,2],[6,3,9]]

result=[[0,0,0],[0,0,0],[0,0,0]]
# print(len(A),len(A[0]))
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]+B[i][j]
#print(result)
for i in result:
    print(i)

print("--------using functions------------")
def matrix(m,n):
    outer=[]
    for i in range(m):
        inner=[]
        for j in range(n):
            inp=int(input(f"enter the elements of [{i}][{j}] is: "))
            inner.append(inp)
        outer.append(inner)
    return outer


def sum(A,B):
    output=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        output.append(row)
    # return output
    for i in output:
        print(i)


m=int(input("enter the value of rows: "))
n=int(input("enter the value of columns: "))
print("matrix A: ")
A=matrix(m,n)
print("matrix B: ")
B=matrix(m,n)
s=sum(A,B)
print(s)

