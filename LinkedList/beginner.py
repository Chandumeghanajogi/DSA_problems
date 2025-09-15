# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#         def __init__(self):
#             self.head=None
#         def insertatbegin(self,data):
#            new=node(data)
#            if self.head is None:
#                self.head=new
#            else:
#                new.next=self.head
#                self.head=new
#         def atend(self,data):
#             new=node(data)
#             self.head=None
#             if self.head is None:
#                 self.head=new
#                 return 
#             temp=self.head
#             while(temp.next):
#                 temp=temp.next
#                 temp.next=new
                
            
            
            
#         def display(self):
#             temp=self.head
#             while temp:
#                 print(temp.data,end="---")
#                 temp=temp.next
#             print("none")
        
        
        
        
# obj=linkedlist()

# obj.insertatbegin(30)
# obj.insertatbegin(20)
# obj.atend(300)
# obj.display()


n="geeksforgeeks"
sub1="for"
main=len(n)
sub=len(sub1)
print(main)
print(sub)
for i in range((main-sub)+1):
    print(n[i:i+3])
    if n[i:i+(sub)]==sub1:
        print("true")
        print(i)
    else:
        continue







# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#         def __init__(self):
#             self.head=None
#         def insertatbegin(self,data):
#            new=node(data)
#            if self.head is None:
#                self.head=new
#            else:
#                new.next=self.head
#                self.head=new
#         def atend(self,data):
#             new=node(data)
#             if self.head is None:
#                 self.head=new
#                 return 
#             temp=self.head
#             while(temp.next):
#                 temp=temp.next
#             temp.next=new
                
#         def atpos(self,pos,data):
#             new=node(data)
#             if pos==0:
#                 self.insertatbegin(data)
#                 return 
#             temp=self.head
#             count=0
            
#             while temp is not None and count<pos-1:
#                 temp=temp.next
#                 count+=1
#             if temp is None:
#                 print("index out")
#             new.next=temp.next
#             temp.next=new
            
            
#         def display(self):
#             temp=self.head
#             while temp:
#                 print(temp.data,end="---")
#                 temp=temp.next
#             print("none")
        
        
        
        
# obj=linkedlist()

# obj.insertatbegin(30)
# # obj.insertatbegin(20)
# obj.atpos(0,400)
# obj.atend(300)
# obj.display()




# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linked:
#     def __init__(self):
#         self.head=None


#     def insertatbeg(self,data):
#         new=node(data)
#         new.next=self.head
#         self.head=new
        
#     def insertatend(self,data):
#         new=node(data)
#         if self.head is None:
#             new.next=self.head
#             self.head=new
#             return
#         else:
#             curr=self.head
#             while curr.next is not None:
#                 curr=curr.next
#             curr.next=new
#     def posi(self,pos,data):
#         new=node(data)
#         if pos==0:
#             self.insertatbeg(data)
#             return 
#         else:
#             curr=self.head
#             count=0
#             while curr.next is not None and count<pos-1:
#                 curr=curr.next
#                 count+=1
#             new.next=curr.next
#             curr.next=new
#     def deleteatbeg(self):
#         if self.head is None:
#             print("not possible")
#         else:
#             self.head=self.head.next
#     def deleteatend(self):
#         if self.head is None:
#             print("not poosible")
#         else:
#             current=self.head
#             while current.next.next is not None:
#                 current=current.next
#             current.next=None
#     def deleteatpos(self,k):
#         if self.head is None:
#             print("not possible")
#         elif k==0:
#             self.head=self.head.next
#             return 
#         else:
#             curr=self.head
#             count=0
#             while curr is not None and count<k-1:
#                 curr=curr.next
#                 count+=1
#             curr.next=curr.next.next
            
#     def search(self,key):
#         if self.head is None:
#             print("cant find it")
#         else:
#             flag=False
#             pos=0
#             count=0
#             curr=self.head
#             while curr is not None:
#                 count+=1
#                 if curr.data==key:
#                     flag=True
                
                
#                 curr=curr.next
#                 pos+=1
#         print(count)
#         if flag:
#             print("found")
#             print(pos)
#         else:
#             print("not here")
                
        
            
                
            
            
            
            
            
#     def display(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.data,end="-->")
#             temp=temp.next
#         print(None)
# obj=linked()
# obj.insertatbeg(100)
# obj.insertatbeg(299)
# obj.insertatbeg(399)
# obj.insertatend(1)
# obj.insertatend(2)
# obj.search(5)
# obj.insertatend(5)
# obj.search(5)
# # obj.posi(1,111)
# # obj.deleteatbeg()
# # obj.deleteatend()
# # obj.deleteatpos(0)
# # obj.display()