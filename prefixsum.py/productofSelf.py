a=[1,2,-4,-1,3]
n=len(a)
prefix=[0]*n
suffix=[0]*n
prefix[0]=a[0]
suffix[n-1]=a[n-1]
print(prefix)
for i in range(1,n):
    prefix[i]=prefix[i-1]*a[i]
print(prefix)
for i in range(len(a)-2,-1,-1):
    suffix[i]=suffix[i+1]*a[i]
print(suffix)
res=[0]*n
res[0]=suffix[1]
res[-1]=prefix[-2]
for i in range(1,n-1):
    res[i]=suffix[i+1]*prefix[i-1]
print(res)