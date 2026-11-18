# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        values.reverse()
        new_head = ListNode(values[0])
        current = new_head
        for i in values[1:]:
            current.next = ListNode(i)
            current = current.next
        return new_head
        