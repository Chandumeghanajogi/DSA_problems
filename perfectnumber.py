#to handle the all test cases for the perfect number

def perfectnumber(num):
    if num<=1:
        return False
    else:
        total=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                total+=i
                if i!=num//i:
                    total+=num//i
    if total==num:
        return True
    return False


n=28
print(perfectnumber(n))


