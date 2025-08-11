
def longest(s,k):
    l=0
    dici={}
    count=float("-inf")
   
    for r in range(len(s)):
        if s[r] in dici:
            dici[s[r]]+=1
        else:
            dici[s[r]]=1
        
        if dici[s[r]]>=k:

            count=max(count,r-l+1)
    return count



s = "ababbc"
k = 2
print(longest(s,k))