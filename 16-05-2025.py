# 1.Write a Python program to check whether a number is even or odd.

# 2.Write a program to find the largest of three numbers.

# 3.Write a Python function that returns the factorial of a number.

# 4.Write a program to print all numbers from 1 to 100 that are divisible by 5.

# 5.Write a program that reverses a string entered by the user.

# 6.Write a program to check if a number is positive, negative, or zero.

# 7.Write a Python program that accepts a user's age and tells if they are eligible to vote (18+).

# 8.Take two numbers as input and print the maximum.

# 9.Write a program to check whether a character is a vowel or consonant.

# 10.Write a program to determine whether a given year is a leap year.

# 11.Write a program to generate Fibonacci series up to n terms.

# 12.Write a program to check whether a number is an Armstrong number.

# 13.Write a program to check whether a number is prime.

# 14.Write a Python function to check whether a string is a palindrome.

# 15.Write a program to sort a list in ascending order without using sort().

#1 to check for the even or not:
def even(n):
    if n%2==0:
        return True
    return  False
# n=int(input())
print(even(8))

#2 
def largest(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return f"{n1} is greater"
    elif n2>=n3:
        return f"{n2} is greater"
    else:
        return f"{n3} is greater"
    
print(largest(15,15,10))

#3
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))

#4:
def div(n):
    a=[]
    for i in range(1,n+1):
        if i%5==0:
            a.append(i)
        else:
            continue
    return a

    
        
print(div(100))

#5:
def reverse(s):
    return "".join(reversed(s))
print(reverse("chandu"))
#
def reverse(s):
    a=""
    for char in s:
        a=char+a
    return a

print(reverse("chandu"))

def pos(n1):
    if n1>0:
        return "positive number"
    elif n1<0:
        return "negative numver"
    else:
        return "zero"
print(pos(-1))

def vote(n):
    if n>=18:
        return "eligible to vote"
    return f"not eligible to vote"
print(vote(177))

def max1(a,b):
    return max(a,b)
print(max1(10,2))

def voco(a):
    vowels="aeiou"
    if a in vowels:
        return True
    return False
print(voco("i"))

def year1(year):
    if year%4==0 and year%400==0 or  year%100!=0:
        return True
    return False
print(year1(2000))

def fib(n,wanted):
    a=0
    b=1
    a1=[]
    a1.append(a)
    for i in range(n):
        a,b=b,a+b
        a1.append(a)
    if wanted in a1:
        return True
    return -1

    

print(fib(50,wanted=20))

#armstrong

def arm(n):
    n1=n
    sum=0
    while (n>0):
        temp=n%10
        sum+=temp**3
        n//=10
    if sum==n1:
        return True
    return False
print(arm(133))

def prime(n):
    for i in range(2,n):
        if n%i!=0:
            return True
        return False
print(prime(30000))


def palin(s):
    left=0
    right=len(s)-1
    while(left<right):
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
print(palin("amma"))


def sort(n):
    for i in range(len(n)):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n


n=[12,23,13,0,1,3]
print(sort(n))


def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)
n=6
print(fib(n-1))

# Abundant Number
# A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number.
# Let's try and understand the concept better using an example

# Example
# Input : Number = 12
# Output : Yes, It's an Abundant Number
# Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
# Now the sum of the factors except the number itself is :
# 1 + 2 + 3 + 4 + 6 = 16
# as the number 16>12 , the number itself.
# It's an abundant number.

def abu(n):
    sum1=0
    n1=n
    for i in range(1,n):
        if n%i==0:
            sum1+=i
    if sum1>n1:
        return True
    return False

print(abu(16))

def co(n,factors):
    for i in range(1,n):
        if n%i==0:
            factors.append(i)

    return factors

n=12
print(co(12,[]))
    
        





