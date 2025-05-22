#problem1:  a valid anagram or not determination

# 242. Valid Anagram
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

#how I solved this

from collections import Counter
def function(s,t):
    if len(s)!=len(t):
        return False
    else:
        a=Counter(s)
        b=Counter(t)
        if a==b:
            return True
        return False
    
s="cat"
t="rat"
print(function(s,t))

#2
from collections import Counter
def function1(s,t):
    if len(s)!=len(t):
        return False
    else:
        return Counter(s)==Counter(t)
    
s="cat"
t="rat"
print(function1(s,t))

#3
def function3(s,t):
    if len(s)!=len(t):
        return False
    return sorted(s)==sorted(t)
t="anagram"
s="anramag"

print(function3(s,t))



    

    



