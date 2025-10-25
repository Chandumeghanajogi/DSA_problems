class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked:
    def build(self,str1):
        self.head=node(str1[0])
        curr=self.head
        for i in str1[1:]:
            curr.next=node(i)
            curr=curr.next
        return self.head
        
    def new(self,l1,l2):
        dummy=curr=node(0)
        while l1 and l2:
            if l1.data<l2.data:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        curr.next=l1 if l1 else l2
        return dummy.next
        
    def merge(self,h1):
        head=h1
        if not head or not head.next:
            return head
        fast=head.next
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        mid=slow.next
        slow.next=None
        
        left=self.merge(head)
        right=self.merge(mid)
        
        return self.new(left,right)
        
        
    def intersect(self,h1,h2):
        dummy=curr=node(0)
        seen=set()
        while h1:
            seen.add(h1.data)
            h1=h1.next
        while h2:
            if h2.data in seen:
                curr.next=node(h2.data)
                curr=curr.next
            h2=h2.next
        return dummy.next
            
            
        
    # def inter(self,head1,head2):
    #     h1=head1
    #     h2=head2
    #     dummy=curr=node(0)
    #     while h1 and h2:
    #         if h1.data==h2.data:
    #             curr.next=node(h1.data)
    #             curr=curr.next
    #             h1=h1.next
    #             h2=h2.next
    #         elif h1.data<h2.data:
    #             h1=h1.next
    #         else:
    #             h2=h2.next
           
    #     return dummy.next
                
            
                
            
        
    def display(self,h1):
        temp=h1
        while temp:
            print(temp.data,end="--->")
            temp=temp.next
        print(None)
    
    
    
    
    
    



l1=[11,200.32,322,2,4]
l2=[1,4,5]
obj=linked()
h1=obj.build(l1)
h2=obj.build(l2)
a=obj.merge(h1)
b=obj.merge(h2)
res=obj.intersect(a,b)
obj.display(res)





