a={5:"p",1:"a",2:"b",3:"c",4:"r"}
print(a[1])
print(a.get(8,0))

a.popitem()
print(a)

print(a.keys())

a=sorted(a.items(),key=lambda item:item[0])
print(a)

dici={}
for i in range(1,10+1):
    dici[i]=i%3
print(dici)

dici={}
a={"dataaa","science","ai","ml","pythonww"}
for key in a:
    if len(key)%2==0:
        dici[key]=len(key)
print(dici)


from collections import Counter
dici={}
s="chandu"
dici[i]=dici.get(i,0)+1
print(dici)
b=Counter(s)
print(dict(b))

n,m=11,10
dis=(10*n)/100
print(dis)
final=n-dis
print(final)

if final<m :
    print("ONLINE")
elif m<final:
    print("DINING")
else:
    print("EITHER")


# s={"chandu11","meghana","meena"}
s="abc"
dici={}
for i in s:
    dici[i]=ord(i)
print(dici)
    

a,b=7,7    #pro1=100 #pro2=200


f1=a*100/100   
dis1=100-f1
f2=b*200/100
dis2=200-f2
if dis1<dis2:
    print("FIRST")
elif dis1>dis2:
    print("SECOND")
else:
    print("BOTH")


n,k=5,2
total=int(n//k)
print(total)
print(total**2)