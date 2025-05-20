def zero(n1):
    n=str(n1)
    l=[]
    for i in n:
        if(i=="1"):
            l.append("0")
        else:
            l.append("1")
    return "".join(map(str,l))
    
    
n1=1001
print(zero(n1))

def zero1(n):
    n1=str(n)
    n1.replace("0","1")
    return n1

print(zero("0110"))

        