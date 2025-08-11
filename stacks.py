# s="(())"
# stack=[]
# valid=True
# for i in s:
#     if i=="(":
#         stack.append(i)
#     elif not stack :
       
#         valid=False
#         break
#     else:
#         stack.pop()
# if valid and  len(stack)==0:
#     print("true")
# else:
#     print("false")

# def paren(s):
#     stack=[]
#     for i in s:
#         if i in "{[(":
#             stack.append(i)
#         elif i in "}])":
#             if not stack:
#                 return False
#             top=stack[-1]
#             if top=="{" and i!="}" or  top=="[" and i!="]"  or top=="(" and i!=")" :

#                 return False
#             stack.pop()
            
#     if len(stack)==0:
#         return True
#     else:
#         return False



# print(paren("([)]"))  


# # Input: s = "abbaca"
# # Output: "ca"
# # Explanation:
# # - Remove "bb" → "aaca"  [a,b]
# # - Remove "aa" → "ca"


# stack=[]
# s = "abbbaaccz"



# for i in s:
#     if stack and stack[-1]==i:
#         stack.pop()
#     else:
#         stack.append(i)

# print(stack)

# # Input:  s = "ab#c", t = "ad#c"
# # Output: True
# # Explanation: Both become "ac"

def string(s):
    stack=[]
    for i in s:
        if i=="#":
            if stack:
                stack.pop()
        else:
            stack.append(i)
    return stack
s = "ab#c"
t = "ad#c"

if string(s)==string(t):
    print("true")
else:
    print("false")

