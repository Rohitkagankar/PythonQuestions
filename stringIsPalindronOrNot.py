#program to check given string is pallindron or not
string=input("enter the string :")
rev=string[ : :-1]
if string==rev:
    print("Given string is pallidron.")
else:
    print("string is not a pallindron.")