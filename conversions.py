#decimal to the binary conversion:  n=3
def decimal(n):
    binary=""
    while (n>0):
        binary= str(n%2)+binary
        n//=2
    return binary or 0

print(decimal(3))

def octal(n):
    octal=''
    while (n>0):
        octal=str(n%8)+octal
        n//=8
    return octal

print(octal(274))

def hexa(n):
    hexadecimals="0123456789ABCDEF"
    hexa=""
    while(n>0):
        hexa=hexadecimals[n%16]+hexa
        n//=16
    return hexa

# print(hexa(14))

def binary(n):
    a=hex(n)
    return a[2:]

print(binary(1000))

# direct Conversions
# 1  decimal to any base case
# 1----> decimal to binary
n1=8
a=bin(n1)
print(a[2:])

b=oct(n1)
print(b[2:])

c=hex(14)
print(c[2:])

#2 -->conversion of anybase case to the decimal

n=int(input())
n1=str(n)

a=int(n1,2)
print(a)





 