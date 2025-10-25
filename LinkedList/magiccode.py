#the  first code of magic number here
# def sum(n):
#     sum1=0
#     for i in n:
#         sum1+=int(i)
#     return sum1
# a=[]
# res=[]
# count=0 
# for i in range(1,10+1):
#     a.append(bin(i)[2:].zfill(3))
# for i in a:
#     a="".join(["1" if ch=="0" else "2" for ch in i])
#     if sum((a))%2==1:
#         count+=1
    
# print(count)

# #the second code 

# from collections import Counter
# num=[1,2,1,1,2,4,3,3]
# b=Counter(num)
# for key,value in b.items():
#     print(f"{key} occured {value} times")

#the longest substring 

def longest(s):
    startindex=0
    max1=float("-inf")
    set1=set()
    l=0
    for r in range(len(s)):
        while s[r] in set1:
            set1.remove(s[l])
            l+=1
        set1.add(s[r])
        curr= r-l+1
        if curr>max1:
            max1=curr
            startindex=l
        
    return s[startindex:startindex+max1]




s="aaaaabcghgh"
print(longest(s))

print(12334//10)

    


