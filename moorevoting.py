# The code to check for the same repaeation of more elements :
from collections import Counter
arr = [1, 2, 1, 1, 3, 2, 2]
acount=0
bcount=0
ele1=float("-inf")
ele2=float("-inf")
for i in range(len(arr)):
    if acount==0 and ele2!=arr[i]:
        ele1=arr[i]
        acount+=1
    elif bcount==0 and ele1!=arr[i]:
        ele2=arr[i]
        bcount+=1
    elif ele1==arr[i]:
        acount+=1
    elif ele2==arr[i]:
        bcount+=1
    else:
        acount-=1
        bcount-=1
print(ele1,ele2)
acount2=0
bcount2=0
for i in range(len(arr)):
    if arr[i]==ele1:
        acount2+=1
    else:
        bcount2+=1
mini=len(arr)//3
if acount2>mini and bcount2>mini:
    print([ele1,ele2])

# To find out the single element
count=0
ele=None
n=len(arr)
for i in range(len(arr)):
    if count==0:
        count+=1
        ele=arr[i]
    elif ele==arr[i]:
        count+=1
    else:
        count-=1
count1=0
for i in range(len(arr)):
    if arr[i]==ele:
        count1+=1
if count1>n//2:
    print(ele)
    
