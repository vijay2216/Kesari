# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = temp = head
        if not head or not head.next: return
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                break
        while slow.next:
            if(slow == temp):
                return temp
            slow = slow.next
            temp = temp.next
        return
