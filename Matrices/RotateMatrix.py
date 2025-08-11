# I am using the extra space complexity due to res matrix:
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n=len(arr)
res=[[0 for i in range(n)] for j in range(n)]
print(res)
for i in range(n):
    for j in range(n):
        res[j][n-1-i]=arr[i][j]
for i in range(n):
    for j in range(n):
        print(res[i][j],end=" ")
    print()
