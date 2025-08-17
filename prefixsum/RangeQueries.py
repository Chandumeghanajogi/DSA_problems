# RangeQueries is the problem in which use the prefixsum
# -->start compute the prefix sum
# -->they given the queries 
# the formula for this is sum(l,r)=prefix[r]-prefix[l-1]
# if we got the zero in the l then we need to handle it sum(l,r)=prefix[r]


nums = [42]  
queries = [(0, 0)]  




prefix=[0]*len(nums)
prefix[0]=nums[0]
for i in range(1,len(nums)):
    prefix[i]=prefix[i-1]+nums[i]
print(prefix)
res=[]
for i in queries:
    l=i[0]
    r=i[1]
    if l==0:
        ans=prefix[r]
    else:
        ans=prefix[r]-prefix[l-1]
    res.append(ans)
print(res)