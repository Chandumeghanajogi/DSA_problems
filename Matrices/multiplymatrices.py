# # Matrix A (2x3)
# a = [
#     [1, 4, 7],
#     [2, 5, 8]
# ]

# # Matrix B (3x2)
# b = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# rows=len(a)
# rowsa=len(a[0])
# cols=len(b)
# colsa=len(b[0])



# res=[[0 for i in range(colsa)] for j in range(rows) ]
# for i in range(rows):
#     for j in range(colsa):
#         for k in range(cols):
#             res[i][j]+=a[i][k]*b[k][j]
# for f in res:
#     print(*f)



a = [
    [1, 4, 7],
    [2, 5, 8],
    [2, 5, 8]
]

b = [
    [1, 4, 7],
    [2, 5, 8],
    [2, 5, 8]
]

# l=len(a[0])
# # print(l)
# res=[[0 for i in range(l)] for j in range(len(b))]
# print(res)
# for i in range(len(a)):
#     for j in range(l):
#          res[i][j]=a[i][j]+b[i][j]
# print(res)
        
arow=len(a)
acol=len(a[0])
brow=len(b)
bcol=len(b[0])
res=[[0 for i in range(bcol) ]for j in range(arow)]
for i in range(arow):
    for j in range(bcol):
        for k in range(acol):
            res[i][j]+=a[i][k]*b[k][j]
print(res)
    
    
        