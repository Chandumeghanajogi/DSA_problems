#Thye Brute Force Appraoch:
def rowmatrix(i,matrix,n):
    for j in range(m):
        if matrix[i][j]!=0:
            matrix[i][j]=-1
def colmatrix(j,matrix,n):
    for i in range(m):
        if matrix[i][j]!=0:
            matrix[i][j]=-1
def zeromat(matrix,n,m):     
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                rowmatrix(i,matrix,n)
                colmatrix(j,matrix,n)
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==-1:
                matrix[i][j]=0
    return matrix
            


    
matrix= [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n=len(matrix)
m=len(matrix[0])
a=zeromat(matrix,n,m)
for i in a:
    print(*i)

#The Better Apporach:

def zeromat(matrix,n,m):
    row=[0]*n
    col=[0]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j]=0
    return matrix
                
    
matrix= [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n=len(matrix)
m=len(matrix[0])
a=zeromat(matrix,n,m)
for a1 in a:
    print(*a1)

#analyzing the time complexity of the set matrix zeroes:
# Time complexity is :
# O(2*n*m)
# the space complexity is O(n)+O(m)   one for the extra row taken and other for the col taken 
