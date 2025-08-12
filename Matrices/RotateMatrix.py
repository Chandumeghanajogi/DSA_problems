# I am using the extra space complexity due to res matrix:
# Your extra space complexity (excluding input) is O(n²) because of the res matrix.

# Total space used (including input) is O(n²).
                                        



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


#The optimal solution with out taking the extra space
# the time complexity is O(n**2)
# But the space complexity for prevoius one is 


matrix= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n=len(matrix)
for i in range(n):
    for j in range(i,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for i in range(n):
    matrix[i].reverse()

for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()
