# Rotate a Linked List Problem
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0: return head
        temp = head
        count = 1
        while temp.next:
            count += 1
            temp = temp.next
        temp.next = head
        
        head_index = count - k%count
        temp = head
        for i in range(head_index):
            prev = temp
            temp = temp.next
        prev.next = None
        head = temp
        return head
