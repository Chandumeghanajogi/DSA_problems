# #armstrong number with the range:
# def armstrong(n):
#     sum=0
#     num=n
#     while n>0:
#         temp=n%10
#         sum+=temp**3
#         n//=10
#     if sum==num:
#         return True
#     return False
    
# def rangearm(lower,upper):
#     a=[]
#     for i in range(lower,upper):
#         if armstrong(i):
#             a.append(i)
#     return a

# print(rangearm(100,160))

# #satrong number:

# def factorial(n):
#     if n==0:
#         return 1
#     elif n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# def strong(n):
#     sum=0
#     num=n
#     while n>0:
#         temp=n%10
#         sum+=factorial(temp)
#         n//=10
#     if sum==num:
#         return True
#     return False

# print(strong(145))

# #automorphic number
# #5----25
# #376---141376

# def auto(n):
#     n1=n*n
#     n2=str(n1)
#     n=str(n)
#     if n2.endswith(n):
#         return True
#     return False

# print(auto(7))

#friendly pair
def friendly(number):
    factors=[]
    for i in range(1,number):
        if (number%i)==0:
            factors.append(i)
    return sum(factors)/number

if __name__=="__main__":
    n1=6
    n2=28
    if friendly(n1)==friendly(n2):
        print("True")
    else:
        print(False)

#gcd or hcf of two numbers:
#solved using the euclidean algorithmn:
#a*b=lcm(a*b)/gcd(a*b)


def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)


def lcm(a,b):
    lcm=a*b//gcd(a,b)
    return lcm

print(lcm(2,3))



    

