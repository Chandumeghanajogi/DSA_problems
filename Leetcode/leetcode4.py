

# # a=[3,0,2,0,2,1,0]
# # print(a)
# # i=0
# # j=i+1
# # while i<j:
# #     if a[i]==0:
# #         a[i],a[j]=a[j],a[i]
# #     i+=1
# #     j-=1
# # print(a)

# def rev(n):
#     r=0
#     while n>0:
#         temp=n%10
#         r=r*10+temp
#         n//=10
#     return r

# n=123
# print(rev(n))


s="chandu"
flag=False
l=0
count=0
temp=""
for r in range(len(s)):
    if s[r] in "aeiou":
        temp+=s[r]
    while s[r] not in "aeiou":
        temp=temp[1:]
        l+=1
    print(temp[l:r+1])
    if len(temp)>2:
        flag=True
if flag:
    print("true")
else:
    print("false")