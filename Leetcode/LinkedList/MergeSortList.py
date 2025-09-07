class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked:
    def build(self,arr):
        self.head=node(arr[0])
        curr=self.head
        for i in arr[1:]:
            curr.next=node(i)
            curr=curr.next
        return self.head
    
    def mainalgo(self,left,right):
        dummy=curr=node(0)
        while left!=None and right!=None:
            if left.data<right.data:
                curr.next=left
                left=left.next
            else:
                curr.next=right
                right=right.next
            curr=curr.next
        curr.next=left if left else right

        return dummy.next
    
    def mergealgo(self,h1):
        
        head=h1
        slow=head
        fast=head
        if head==None or head.next==None:
            return head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            
        mid=slow.next
        slow.next=None
        
        left=self.mergealgo(head)
        right=self.mergealgo(mid)

        return self.mainalgo(left,right)
        
        







arr=[12,30,20,1,5,7]
obj=Linked()
h1=obj.build(arr)
res = obj.mergealgo(h1)
curr = res
while curr:
    print(curr.data, end=' ')
    curr = curr.next
print()





