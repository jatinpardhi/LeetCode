# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry=0
        ans=curr=ListNode(val=0)
        
        while(l1 and l2):
            summ=l1.val+l2.val+carry
            newnode=ListNode(summ%10)
            carry=summ//10
            curr.next=newnode
            curr=curr.next
            l1=l1.next
            l2=l2.next
        while l1:
            summ=l1.val+carry
            newnode=ListNode(summ%10)
            carry=summ//10
            curr.next=newnode
            curr=curr.next
            l1=l1.next
        while l2:
            summ=l2.val+carry
            newnode=ListNode(summ%10)
            carry=summ//10
            curr.next=newnode
            curr=curr.next
            l2=l2.next
        if carry==1:
            newnode=ListNode(1)
            curr.next=newnode
            
        return ans.next
            
            
        