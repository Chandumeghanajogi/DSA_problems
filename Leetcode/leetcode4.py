# merge two sorted lists:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]


def merge(l1,l2):
    a=sorted(l1)
    b=sorted(l2)
    return sorted(a+b)

l1=[1,2,4]
l2=[1,3,4]
print(merge(l1,l2))


