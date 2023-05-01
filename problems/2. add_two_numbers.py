from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            # Get List node values and sum both lists
            list1 = self.return_values(l1)[::-1]
            list2 = self.return_values(l2)[::-1]
            list_sum = int(''.join(map(str, list1))) + int(''.join(map(str, list2)))

            # Create Output ListNode
            head = ListNode(None)
            current = head
            for val in [int(x) for x in str(list_sum)][::-1]:
                current.next = ListNode(val)
                current = current.next
            head = head.next # This will remove the beginning none node.
            return head

    def return_values(self, node, result=None):
        if not result: result = []
        if node == None: return result
        result.append(node.val)
        self.return_values(node.next, result=result)
        return result