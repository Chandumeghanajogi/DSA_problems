# Question 1
# Title: Square of Each Element in Tuple

# Problem Statement:
# You are given a single line of space-separated integers. Your task is to store them in a tuple and create a new tuple where each element is the square of the original.

# Input Format:
# A single line of space-separated integers.

# Output Format:
# A tuple with the square of each input element.

# Sample Test Cases:

# Sample Input 1:
# 2 3 4
# Sample Output 1:
# (4, 9, 16)

# Sample Input 2:
# 5 0 -2
# Sample Output 2:
# (25, 0, 4)

a=(5, 0 ,-2)
res=tuple(map(lambda x:x**2,a))
print(res)


# Question 2
# Title: Remove Even Numbers from Tuple

# Problem Statement:
# You are given a tuple of integers. Your task is to remove all even numbers and return a tuple with only odd numbers.

# Input Format:
# A single line of space-separated integers.

# Output Format:
# A tuple with only odd elements.

# Sample Test Cases:

# Sample Input 1:
# 1 2 3 4 5
# Sample Output 1:
# (1, 3, 5)

# Sample Input 2:
# 2 4 6 8
# Sample Output 2:
# () (empty tuple)
a=(2,4,6,8)
res=tuple(filter(lambda x:x%2==1,a))
print(res)


# Question 3
# Title: Tuple Index-wise Addition

# Problem Statement:
# You are given two tuples of equal length. Add the corresponding elements of both tuples and print the resulting tuple.

# Input Format:
# Two lines containing space-separated integers representing two tuples.

# Output Format:
# A tuple of element-wise sums.

# Sample Test Cases:

# Sample Input 1:
# 1 2 3
# 4 5 6
# Sample Output 1:
# (5, 7, 9)

# Sample Input 2:
# 10 20 30
# 1 1 1
# Sample Output 2:
# (11, 21, 31)
a=(10, 20, 30)
b=(4 ,5, 6)
res=tuple(e1+e2 for e1,e2 in zip(a,b))
print(res)

# Question 4
# Title: Find Second Largest Number in Tuple

# Problem Statement:
# Given a tuple of integers, find and print the second largest element.

# Input Format:
# A single line of space-separated integers.

# Output Format:
# A single integer: the second largest number in the tuple.

# Sample Test Cases:

# Sample Input 1:
# 10 20 30 40
# Sample Output 1:
# 30

# Sample Input 2:
# 3 3 2 1
# Sample Output 2:
# 2
a=(3, 3, 2, 1)
ab=tuple(sorted(a,reverse=True))
print(ab[-2])
# Question 5
# Title: Tuple Elements in Reverse Pairs

# Problem Statement:
# Given a tuple of even number of elements, group them into pairs and reverse each pair.

# Input Format:
# A single line of space-separated integers (even number of elements).

# Output Format:
# A tuple of reversed pairs.

# Sample Test Cases:

# Sample Input 1:
# 1 2 3 4
# Sample Output 1:
# (2, 1, 4, 3)

# Sample Input 2:
b=(5, 6, 7 ,8 ,9, 10)
# Sample Output 2:
# (6, 5, 8, 7, 10, 9)
res=[]
for i in range(1,len(b),2):
    res.extend([b[i],b[i-1]])
final="".join(map(str,res))
print(tuple(final))


# Question 6
# Title: Filter Positive Numbers from Tuple

# Problem Statement:
# Given a tuple of integers, filter out all negative numbers and print a tuple containing only the positive values.

# Input Format:
# A single line of space-separated integers (positive and/or negative).

# Output Format:
# A tuple containing only the positive numbers.

# Sample Test Cases:

# Sample Input 1:
# 1 -2 3 -4 5
# Sample Output 1:
# (1, 3, 5)

# Sample Input 2:
# -5 -6 -7
# Sample Output 2:
# ()

# Question 7
# Title: Create Tuple from First N Natural Numbers

# Problem Statement:
# Given a number N, create a tuple that contains the first N natural numbers (starting from 1).

# Input Format:
# A single integer N.

# Output Format:
# A tuple containing numbers from 1 to N.

# Sample Test Cases:

# Sample Input 1:
# 5
# Sample Output 1:
# (1, 2, 3, 4, 5)

# Sample Input 2:
# 3
# Sample Output 2:
# (1, 2, 3)


# Question 8
# Title: Count Even and Odd Numbers in Tuple

# Problem Statement:
# Given a tuple of integers, count how many even and how many odd numbers it contains.

# Input Format:
# A single line of space-separated integers.

# Output Format:
# Two integers separated by space — count of even numbers and count of odd numbers.

# Sample Test Cases:

# Sample Input 1:
# 1 2 3 4 5 6
# Sample Output 1:
# 3 3

# Sample Input 2:
# 2 4 6 8
# Sample Output 2:
# 4 0

# Question 9
# Title: Multiply All Elements of Tuple

# Problem Statement:
# You are given a tuple of integers. Write a program to compute the product of all elements in the tuple.

# Input Format:
# A single line of space-separated integers.

# Output Format:
# A single integer: the product of all elements.

# Sample Test Cases:

# Sample Input 1:
# 2 3 4
# Sample Output 1:
# 24

# Sample Input 2:
# 1 5 0 2
# Sample Output 2:
# 0


# Question 10
# Title: Remove First and Last Element of Tuple

# Problem Statement:
# Given a tuple, create a new tuple after removing the first and last elements.

# Input Format:
# A single line of space-separated integers.

# Output Format:
# The resulting tuple after removing the first and last items.

# Sample Test Cases:

# Sample Input 1:
# 10 20 30 40 50
# Sample Output 1:
# (20, 30, 40)

# Sample Input 2:
# 1 2 3
# Sample Output 2:
# (2,)


# Question 11
# Title: Create Tuple from User-defined Range

# Problem Statement:
# Given two integers start and end, create a tuple of numbers from start to end (inclusive).

# Input Format:
# Two integers separated by space.

# Output Format:
# A tuple of integers in the given range.

# Sample Test Cases:

# Sample Input 1:
# 3 7
# Sample Output 1:
# (3, 4, 5, 6, 7)

# Sample Input 2:
# 5 5
# Sample Output 2:
# (5,)

# Question 12
# Title: Find Tuple Element with Maximum Frequency

# Problem Statement:
# Given a tuple of values, find and print the element that appears most frequently.

# Input Format:
# A single line of space-separated values.

# Output Format:
# A single value — the most frequent element.

# Sample Test Cases:

# Sample Input 1:
# apple banana apple mango apple
# Sample Output 1:
# apple

# Sample Input 2:
# 1 2 3 2 2 1
# Sample Output 2:
# 2

from collections import Counter
nums=(1 ,2, 3, 2, 2, 1)
a=Counter(nums)
freq=a.most_common(nums[0])
print(freq[0][0])