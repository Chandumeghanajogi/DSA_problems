class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
        def __init__(self):
            self.head=None
        def insertatbegin(self,data):
           new=node(data)
           if self.head is None:
               self.head=new
           else:
               new.next=self.head
               self.head=new
        def deletebeg(self):
            if self.head==None:
                return 
            else:
                curr=self.head
                self.head=curr.next
        def deleteend(self):
            if self.head==None:
                print("not possible")
            else:
                curr=self.head
                while curr.next.next!=None:
                    curr=curr.next
                curr.next=None
        
                
            
            
            
        





#Question1:  The middle element is the linkedList
     






#Question2:  Delete the node in the linked list
#Question3:  Remove the nth node from the linkedlist
# approach 1 is using the formula i.e is length-k+1  
# appraoch 2 is using the slow and fast pointers
        def removenthnode(self,k):
            slow=self.head
            fast=self.head
            for i in range(k):
                fast=fast.next
            print(fast.data)
            if fast==None:
                self.head=self.head.next
                return 
            while fast.next is not None:
                fast=fast.next
                slow=slow.next
            slow.next=slow.next.next






#Question4:  Remove the duplicates from the Sorted linkedlist
# mY try its see:
        def removedup(self):
            curr=self.head

            # the corner case is  
            if self.head==None:
                return self.head
            while curr.next is not None:
                if curr.data!=curr.next.data:
                    curr=curr.next
                else:
                    curr.next=curr.next.next

# THE GOLDEN QUESTION:
#Question5:  To Reverse the LinkedList
        def reverse(self):
                curr=self.head
                nxt=None
                prev=None
                while curr is not None:
                    nxt=curr.next
                    curr.next=prev
                    prev=curr
                    curr=nxt
                self.head=prev

        def palin(self):
            # the approach is to get the middle element ,the second part is to reverse the second and later to check the element or not
            #to get the middle element
            slow=self.head
            fast=self.head
            while fast!=None and fast.next is not None:
                slow=slow.next
                fast=fast.next.next
            #the reverse logic here:
            prev=None
            nxt=None
            curr=slow
            while curr is not None:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            left=self.head
            right=prev
            flag=True
            while left:
                if left.data!=right.data:
                    flag=False
                    break
                left=left.next
                right=right.next
            if flag:
                print("true")
            else:
                print("false not a palin")


        # def rotatek(self,k):
        #     count=0
        #     curr=self.head
        #     while curr.next!=None:
        #         count+=1
        #         curr=curr.next
        #     count+=1
        #     while self.head==None and self.head.next is None:
        #         return self.head
        #     k=k%count
        #     new=self.head
        #     for i in range(count-k-1):
        #         new=new.next
        #     curr.next=self.head
        #     self.head=new.next
        #     new.next=None
            
        
        #rorate a linkedlist

        def rotation(self,k):
            l=0
            curr=self.head
            while curr.next!=None:
                l+=1
                curr=curr.next
            l+=1
            k=k%l
            new=self.head
            for i in range(l-k-1):
                new=new.next
            curr.next=self.head
            self.head=new.next
            new.next=None

        # def addnumber(self,l1,l2):
        #     dummy=curr=node(0)
        #     carry=0
        #     while l1 or l2 or carry:
        #         if l1:
        #             carry+=l1.data
        #             l1=l1.next
        #         if l2:
        #             carry+=l2.data
        #             l2=l2.next
        #         curr.next=node(carry%10)
        #         curr=curr.next
        #         carry//=10
        #     return dummy.next
        
        



            
            


                        
           
            


        
                  

            
            









        def display(self):
            temp=self.head
            while temp:
                print(temp.data,end="--->")
                temp=temp.next
            print("none")



obj=linkedlist()
obj.insertatbegin(50)
obj.insertatbegin(50)
obj.insertatbegin(50)
obj.insertatbegin(40)
obj.insertatbegin(40)
obj.insertatbegin(30)
obj.insertatbegin(30)
obj.insertatbegin(20)
obj.insertatbegin(10)
obj.insertatbegin(10)
obj.removedup()
# obj.deletebeg()
# obj.deleteend()
# # obj.reverse()
# obj.palin()
obj.removenthnode(3)
# obj.rotatek(4)
# obj.rotation(3)
# obj.reve()
# obj.addnumber(21,21)
obj.display()



#about the intresection of the two linkedlist:

# def intersection(p1,p2):



