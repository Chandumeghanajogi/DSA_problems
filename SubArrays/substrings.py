# # Input
# # Output
# # 4
# # aeiouaeiou
# # abxy
# # aebcdefghij
# # abcdeeafg
# # Happy
# # Sad
# # Sad
# # Happy

# s="abcdeeafg"
# vowels="aeiou"
# # flag=False
# # for i in range(len(s)):
# #     for j in range(1,len(s)):
# #         a=s[i:j+1]
# #         if len(a)>2 and all(ch in vowels  for ch in a):
# #             flag=True
# # if flag:
# #     print("happy")
# # else:
# #     print("sad")


def longest(s):
    l=0
    unique=set()
    maxcount=0
    for r in range(len(s)):
        if s[r] in unique:
            unique.remove(s[l])
            l+=1
            
        if s[r] not in unique:
            unique.add(s[r])
        print(s[l:r+1])
        maxcount=max(maxcount,r-l+1)
    print(maxcount)

s="abcabcbb"
print(longest(s))
    







            
        