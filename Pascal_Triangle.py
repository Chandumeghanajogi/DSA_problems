# def chandu(r,c):
#     res=1
#     for i in range(c):
#         res=res*(r-i)
#         res=res//(i+1)
#     return res
# n=5
# for c in range(1,n+1):
#     print(chandu(n-1,c-1),end=" ")


def gene(row):
    ans=1
    result=[1]
    for col in range(1,row):
        ans*=(row-col)
        ans=ans//col
        result.append(ans)
    return result

n=5

for i in range(1,n+1):
    print(*gene(i))



def pascalTriangleI( r, c):
        def generate(r):
            ans=1
            result=[1]
            for col in range(1,r):
                ans*=(r-col)
                ans=ans//col
                result.append(ans)
            return result
        final=[]
        for col in range(1,r+1):
            a=generate(col)
            final.append(a)
        return final

def generate(n):
    result=[1]
    ans=1
    for col in range(1,n):
        ans*=(n-col)
        ans=ans//col
        result.append(ans)
    return result
n=5    
final=[]
for i in range(1,n+1):
    a=generate(i)
    final.append(a)
print(final)

for i in final:
    for ele in i:
        print(ele,end=" ")
    print()





    

    
