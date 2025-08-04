# # #simple project1:
# # #using the health conditions and symptoms:
# print("Welcome!!")
# dict1={}
# name1=input()
# password1=input()

# dict1[name1]=password1
# print(dict1)

# name11=input()
# password22=input()
# if name11 in dict1 and dict1[name1]==password22:
#     print("login success")
# else:
#     print("unsuccessfil")


# s=input("Enter the Symptoms here:")
# res=s.strip().split(" ")
# if "body temperature" or "cold" or "cough" in res:
#     print("fever")
# elif "headache" or "xxx" in res:
#     print("migraine")
# elif "heartpain" or "sweating" or "etc":
#     print("heartIssue")
# else:
#     print("sorry!!")
#     print("Enter again")



# # 
# # # age=int(input())
# # if age>=18:
# #     print("you are eligible to vote")
# # else:
# #     print("you are not eligible to vote")
# # #2

# # a=10
# # b=20
# # if a>b:
# #     print(f'{a} is big')
# # else:
# #     print(f"{b} is big")


# #to know the vowels or the consonants

# s="Chkkk"
# vowels="aeiou"
# s.lower()
# flag=True
# for i in s:
#     if i in vowels:
#         flag=False
# if flag:
#     print("no vowels")
# else:
#     print("vowels")
# # #password checker
# # a=input()
# # if len(a)==8:

# leap=2024
# if leap%4==0 or leap%400==0 and leap%100!=0:
#     print("True")
# else:
#     print("False")

# #password checker
# s="#^&dghei"
# a="sssssw"
# if all(i in a  for i in s ):
#     print("True")
# else:
#     print("false")

# # if len(s)!=8:
# #     print("false")

# # else:
# #     flag=False
# #     spe="!@#%$^&*()"
# #     for i in s:
# #         if i.isalpha() and i.isupper() or i.islower() and i in spe:
# #            flag=True
# # if flag:
# #     print("error")
# # else:
# #     print("success")


# #coding exam questions:

# n=-5
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# # l=input("Lenght is1").split()[1].strip()
# # print(l)

# # p=-153
# # rev=0
# # sign=1
# # if p>0:
# #     n=p
# # elif p<0:
# #     sign=-1
# #     n=-p


# p=-153
# if p<0:
#     n=-p
# else:
#     n=p
# rev=0
# while n>0:
#     temp=n%10
#     rev=rev*10+temp
#     n//=10
# if p<0:
#     rev=-rev

# print(rev)


# #for loop
# for  i in range(10):
#     if i==5:
#          continue
#     print(i,end=" ")


for i in range(1,5):
    for j in range(1,11):
        print(i*j,end=" ")
    print()




























