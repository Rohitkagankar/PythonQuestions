#program to sort words from string in alphabetic order----
string=input("enter the string here: ")
sort=string.split()
for i in range(len(sort)):
    sort[i]=sort[i].lower()
sort.sort()
print(sort)