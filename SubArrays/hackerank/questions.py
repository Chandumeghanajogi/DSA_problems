s="abccddde"
for i in range(len(s)):
    for j in range(i,len(s)):
        a=s[i:j+1]
        print(a)

def alternatingCharacters(s):
    # Write your code here
    count=0
    l=0
    for r in range(1,len(s)):
        if s[l]==s[r]:
            count+=1
        else:
            count+=0
        l+=1
    return count
print(alternatingCharacters("AAABBB"))

# def funnyString(s):
#     # Write your code here
#     n=len(s)
#     sa=s[::-1]
#     a=[]
#     b=[]
#     for i in range(1,n):
#         ans=ord(s[i-1])-ord(s[i])
#         bns=ord(sa[i-1]-ord(sa[i]))
#         a.append(ans)
#         b.append(ans)
#     return sum(a)==sum(b)
# print(funnyString("acxz"))

#other one
# s="aebcdefghij"
# l=0
# temp=[]
# vowels="aeiou"
# flag=False
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         a=s[i:j+1]
#         if len(a)>2:
#             if all(char in vowels for char in a):
#                 flag=True
#                 break
        
# if flag:
#     print("Happy")
# else:
#     print("sad")

s="abcdeeafg"
l=0
temp=[]
vowels="aeiou"
flag=False
for r in range(len(s)):
    temp.append(s[r])
    if r-l>2:
        temp.remove(s[l])
        l+=1
    if r-1+1>2:
        a="".join(map(str,temp))
        if all(char in vowels for char in a):
            flag=True
if flag:
    print("Happy")
else:
    print("sad")

    
    

        