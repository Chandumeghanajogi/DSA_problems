# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
from collections import defaultdict

def string(strs):
    dici=defaultdict(list)
    for i in strs:
        word="".join(sorted(i))
        dici[word].append(i)
    return (dici.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(string(strs))


# using the pure dictionary for this:


def sort(strs):
    dici={}
    for i in strs:
        sorte="".join(sorted(i))
        if sorte in dici:
            dici[sorte].append(i)
        else:
            dici[sorte]=[i]
    return dici

strs = ["eat","tea","tan","ate","nat","bat"]
print(sort(strs))



def grop(a):
    start=a[0]
    stalen=len(start)
    for i in a[1:]:
        while start!=i[0:stalen]:
            stalen-=1
            if stalen==0:
                return ""
            start=start[0:stalen]
    return start


a=["flower","flowght","flowerol"]
print(grop(a))

    


