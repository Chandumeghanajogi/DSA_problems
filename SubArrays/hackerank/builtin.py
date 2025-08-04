#
a="hello welcome aei to you"
print(a.title())
print(a.lower())
print(a.capitalize())
print(a.count("o"))


s=a.split(" ")
print("Aei".index("e"))
temp=[]
vowels="aeiouAEIOU"
for i in s:
    ab=i.capitalize()
    if all(char in vowels for char in ab):
        temp.append(ab)
print(temp)


# strs = ["flower","flow","flight"]
# start=strs[0]
# prelen=len(start)
# for i in strs:
#     while start!=i[0:prelen]:
#         prelen-=1


#         start=start[0:prelen]
# print(start)



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

