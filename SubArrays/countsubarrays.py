#to count the subarrays with the maximum 1S
arr=[0,1,3,1,1,6,7,1,0,1]
l=0
k=2
temp=0
count=0
for r in range(len(arr)):
    if (arr[r]==1):
        temp+=1
    while temp>k:
        if arr[l]==1:
            temp-=1

        l+=1

    count=max(count,r-l+1)
    print(count)
print(count)

s="cbbd"
def palin(s):
    if s==s[::-1]:
        return True
    return False
l=0
temp=[]
ans=[]
for r in range(len(s)):
    a=((s[l:r+1]))
    if len(a)>1 and palin(a):
        ans.append(a)
    else:
        l+=1
print(ans)
    
    

  

  

    

   



