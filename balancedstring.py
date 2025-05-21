n='({})}}'
c=0
temp=False
for i in n:
    if i=="(" or i=="{" or i=="[" :
        c+=1
    else:
        c-=1
if c==0:
    print("True")
else:
    print("false")

a="abcdefghijklmnopqrstuvwxyz"
b="Sphinx of black quartz, judge my vow"
n=b.lower()
pan=True
for i in n:
    if i not in a:
        pan=False
        break
    
if pan==True:
    print("no")
else:
    print("yes")


#to print the isogram of the strings- an isogram is something that letter appears only once

n="helo  aaaa   candu".lower()
n1=n
a=set()
isa=True
for char in n1:
    if char.isalpha():
        if char in a:
            isa=False
        else:
            a.add(char)
if isa==True:
    print("its iso")
else:
    print("nooooooooooo")


from collections import Counter

a="chandumeghana"
c=Counter(a)
print(c)
for char in a:
    if c[char]==1:
        print( char)