# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head or not head.next:
            return False

        slowP = head
        fastP = head

        while fastP and fastP.next:
            slowP = slowP.next
            fastP = fastP.next.next
            if fastP is None:
                return False
            if slowP.val == fastP.val:
                return True
        return False