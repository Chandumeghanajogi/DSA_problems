# 🔸 Problem: "Sum of Middle Elements"
# You are given a list of integers. Write a Python function to:

# Remove the lowest and highest elements from the list.

# Return the sum of the remaining elements.

# If the list has less than 3 elements, return 0.

# Input: [10, 20, 30, 40, 50]
# Output: 90

# Explanation: Remove 10 and 50 → remaining: [20, 30, 40] → sum = 90



def sum_middle_elements(nums: list) -> int:
    # your code here
   
    sum1=0
    num=nums.copy()
    if len(nums)<3:
        return 0
    else:
        num.remove(min(nums))
        num.remove(max(nums))
        for i in num:
            sum1+=i
    return sum1
    
        
    
    
nums= [10, 20, 30, 40, 50]
print(sum_middle_elements(nums))
