# # nums=[0,1,0,3,12]
# # left=0
# # for right in range(len(nums)):
# #     if nums[right]!=0:
# #         nums[right],nums[left]=nums[left],nums[right]
# #         left+=1
# # #toreverse a string
# # s=["c","h","a","n"]
# # left=0
# # right=len(s)-1
# # while left<right:
   
# #     s[left],s[right]=s[right],s[left]
# #     left+=1
# #     right-=1
# # print(s)


# # Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# # Output: 6
# # Explanation: 
# # - First sentence has 5 words.
# # - Second sentence has 4 words.
# # - Third sentence has 6 words.
# # The maximum number of words in a single sentence is 6.

# def sentence(s):
   
#    for char in s:
#     #    return max(len(char.split( )) for char in s)
        
#          return max(len(char.split( )))
       

# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# # print(sentence(sentences))

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
haystack = "sadbutsad", needle = "sad"

n=len(haystack)
n2=len(needle)
dict={}
for i in range(0,n,3):
    if needle==i[]





