def permutations(n):
    fact=1
    for i in range(n,1,-1):
        fact*=i
    return fact

n,r=map(int,input().split(" "))
p=permutations(n)//permutations(n-r)
print(p)