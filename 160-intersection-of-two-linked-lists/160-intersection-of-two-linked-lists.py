# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        curr1=headA
        curr2=headB
        l1=0
        l2=0
        while(curr1):
            l1+=1
            curr1=curr1.next
        while(curr2):
            l2+=1
            curr2=curr2.next
        ans1=headA
        ans2=headB
        if l1>l2:
            while l1!=l2:
                ans1=ans1.next
                l1-=1
        else:
            while l1!=l2:
                ans2=ans2.next
                l2-=1
        while ans1 and ans2 and ans1!=ans2:
            ans1=ans1.next
            ans2=ans2.next
        return ans1
            
            
            
            