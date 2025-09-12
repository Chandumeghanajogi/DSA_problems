class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
   
    def hasCycle(self,head):
        fast=head
        slow=head
        cycle=False
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next

            if fast==slow:
                cycle=True
                break
        
        if not cycle:
            return None
        l=0
        while slow.next!=fast:
            l+=1
            slow=slow.next
        l+=1
        fast=head
        slow=head
        for i in range(l):
            fast=fast.next
        while slow!=fast:
            fast=fast.next
            slow=slow.next
        return slow

    

        

        
            
            


















head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next = head  # cycle back to head



# # Create cycle: tail connects to node with value 2
# head.next.next.next.next = head.next

sol = Solution()
sol.hasCycle(head)

  # Output: True
