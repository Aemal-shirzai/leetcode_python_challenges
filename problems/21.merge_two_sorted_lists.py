from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = [*self.return_values(list1), *self.return_values(list2)]
        new_list.sort()
        
         # Create Output ListNode
        head = ListNode(None)
        current = head
        for val in new_list:
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