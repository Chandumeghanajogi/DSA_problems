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
        def atend(self,data):
            new=node(data)
            if self.head is None:
                self.head=new
                return 
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new
                
        def atpos(self,pos,data):
            new=node(data)
            if pos==0:
                self.insertatbegin(data)
                return 
            temp=self.head
            count=0
            
            while temp is not None and count<pos-1:
                temp=temp.next
                count+=1
            if temp is None:
                print("index out")
            new.next=temp.next
            temp.next=new
            
            
        def display(self):
            temp=self.head
            while temp:
                print(temp.data,end="---")
                temp=temp.next
            print("none")
        
        
        
        
obj=linkedlist()

obj.insertatbegin(30)
# obj.insertatbegin(20)
obj.atpos(0,400)
obj.atend(300)
obj.display()