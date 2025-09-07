# nums=[1,6,9,3,6,12,4,32]

# # //3 9 12 6 32 4
# dup=set(nums)
# main=list(dup)
# print(main)


n=5

for i in range(n):
    p=n-i
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i-1):
        print(p,end=" ")
        p-=1
    a=1
    for j in range(n-i):
        print(a,end=" ")
        a+=1
    print()
