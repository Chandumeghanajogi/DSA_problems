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