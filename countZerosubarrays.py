arr=[0,0,5,0,0]
dici={0:1}
temp=0
count=0
for i in range(len(arr)):
    temp+=arr[i]
    if temp in dici:
        count+=dici[temp]
        dici[temp]+=1
    dici[temp]=1
print(count)
