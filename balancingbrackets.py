def balancingbrackets(s):
    stack=[]
    bal_map={")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in bal_map.values():
            stack.append(char)
        elif char in bal_map:
            if not stack or stack[-1]!=bal_map[char]:
                return False
            stack.pop()
        else:
            return False
    return len(stack)==0
s="{((){}]"
print(balancingbrackets(s))

def brackets20(ss):
    stack=[]
    for s in ss:
        if s=="(" or s=="{" or s=="[":
            stack.append(s)
        else:
            if not stack:
                return False
            else:
                top=stack.pop()
                if (s==")" and top=="(") or (s=="}" and top=="{" )or (s=="]" and top=="["): 
                    continue
                else:
                    return False
    if len(stack)==0:
        return True
    else:
        return False
        




ss="[({}){}[]]"
print(brackets20(ss))