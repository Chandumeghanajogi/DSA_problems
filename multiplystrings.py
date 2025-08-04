# num="25"
# nu2="25"
# num1=num[::-1]
# num2=nu2[::-1]

# res=[0]*(len(num1)+len(num2))
# for i in range(len(num1)):
#     for j in range(len(num2)):
#         mul=int(num1[i])*int(num2[j])
#         res[i+j]+=mul
#         res[i+j+1]+=res[i+j]//10
#         res[i+j]=res[i+j]%10
# while len(res)>1 and res[-1]==0:
#        res.pop()
# print(res[::-1])


#addition of 2 strings:
a="99"
b="98"
num1=a[::-1]
num2=b[::-1]
carry=0
res=[]
for i in range(len(num1)):
    digit=int(num1[i])+int(num2[i])+carry
    res.append(str(digit%10))
    carry=digit//10
if carry:
    res.append(carry)
print(res[::-1])
          

