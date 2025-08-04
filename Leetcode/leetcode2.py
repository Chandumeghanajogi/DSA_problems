for i in [1,2,3,4][::-1]:
    print(i,end="")

z=set("abc")
z.add("pq")
z.update({1,2,3})
print(z)

n=10
if n%2==0:
    print("even number")
else:
    print("odd number")


arr1=[1,2,3,4,5]
arr2=[5 ,6,7,4 ]
max1=float("-inf")
i=j=0
while i<len(arr1) and j<len(arr2):
    if arr1[i]!=arr2[j]:
        if arr1[i]<arr2[j]:
                i+=1
        else:
             j+=1
    else: 
        max1=max(max1,arr1[i])
        i+=1
        j+=1
if max1!=float("-inf"):
    print(max1)
else:
    print("-1")

# Input
# Output
# 5
# 3 1 2 4 5
# 3 1 5 2 4

# sort the array by the parity
nums=[3,1,2,4,5]
odds=[]
evens=[]
for i in range(len(nums)):
    if nums[i]%2==0:
        evens.append(nums[i])
    else:
        odds.append(nums[i])
odds.extend(evens)
print(odds)
        
    
     
nums=[1,2,3,6,9,10]
l=0
mincount=1
for i in range(1,len(nums)):
    if nums[i]-nums[l]<=2:
        mincount+=1
        l+=1
maxcount=1
r=len(nums)-1
print(r-1)
for i in range(r-1,-1,-1):
    if nums[r]-nums[i]<=2:
        maxcount+=1
        r-=1


print(mincount,maxcount)



    
          
     