def longestcommon(arr):
    start=arr[0]
    prefixlen=len(start)
    for i in arr[1:]:
        while start!=i[0:prefixlen]:
            prefixlen-=1
            if prefixlen==0:
               return ""
            start=start[0:prefixlen]
    return start

strs = ["flower","flow","flight"]
print(longestcommon(strs))