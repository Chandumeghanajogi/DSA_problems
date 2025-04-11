# 🔹 Problem: Find the Second Largest Number in a List
# Description:

# Write a Python function that takes a list of integers and returns the second largest number in the list.
# If the list has fewer than 2 unique elements, return None.

#1 : my method

list1=[1,2,3,4,5]
def second(list1):
    list1=set(list1)
    if len(list1)<2:
        return None
    else:
        max1=max(list1)  #max1=5
        max2=0
        for i in list1:
            if i>max2 and i!=max1:
                max2=i

    return max2
    
list1=[1,1,1]
print(second(list1))

#2 the other method:

def second1(list1):
    list1=list(set(list1))
    if len(list1)<2:
        return None
    list1.remove(max(list1))
    return max(list1)
list1=[2,2,4,3000,300022]
print(second1(list1))  

#3 method 3 without the set sort etc


list1=[10,3,1]
num=10
first=10

def new(list1):
    if len(list1)<2:
        return None
    first=second=float('-inf')
    for num in list1:
        if num>first:
            second=first
            first=num
        elif first>num>second:
            second=num

    return second if second!=float('-inf') else None
    
list1=[10,9,1]
print(new(list1))


    



            


