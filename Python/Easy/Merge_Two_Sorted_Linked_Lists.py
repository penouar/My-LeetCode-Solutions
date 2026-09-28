# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        solution=ListNode()
        walker=solution
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                walker.next=l1
                l1=l1.next
            else:
                walker.next=l2
                l2=l2.next
            walker=walker.next
        if l2==None:
            walker.next=l1
        elif l1==None:
            walker.next=l2 
        return solution.next
