from collections import Counter
class Chandu:
    def top_k_elements(self,k:int,nums:list[int])->list[int]:
        c=Counter(nums)
        a=[]
        for key,freq in c.most_common(k):
            a.append(key)
        return a
    
nums=[1,1,1,2,3,2]
k=2
object=Chandu()
print(object.top_k_elements(k,nums))
            
a={1:2,2:3}
b={1:2,2:3,5:55}
flag=True
for i in a:
    if len(a)!=len(b):
        flag=False
    if i not in b:
        flag=False
    if a[i]!=b[i]:
        flag=False
if flag:
    print("same")
else:
    print("false")