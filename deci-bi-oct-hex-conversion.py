deci=int(input("enter the decimal no: "))
print(bin(deci),"in binary")
print(oct(deci),"in octal")
print(hex(deci),"in hexadecimal")
print("-------------------------")
print("by using recursion.")
def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')

DecimalToBinary(deci)

