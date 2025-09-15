# def longestcommon(arr):
#     start=arr[0]
#     prefixlen=len(start)
#     for i in arr[1:]:
#         while start!=i[0:prefixlen]:
#             prefixlen-=1
#             if equlilen==0:
#                return ""
#             start=start[0:prefixlen]
#     return start

# strs = ["flower","flow","flight"]
# print(longestcommon(strs))

strs = ["geeksforgeeks","geek","geel","geezer"]
start=strs[0]
prelen=len(start)
for i in strs[1:]:
    while start!=i[0:prelen]:
        prelen-=1
        if prelen==0:
            print(" ")
        start=start[0:prelen]
print(start)

a="name "
print(a*10)
print(" ","chandu   " *10," ","akhil"," ","stays")
print(23/30)




# strs = ["flower","flow","flight"]
# start=strs[0]
# prelen=len(start)
# for i in strs:
#     while start!=i[0:prelen]:
#         prelen-=1

#         start=start[0:prelen]
# print(start)