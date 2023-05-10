from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def return_list_values(node, result=None):
            if not result: result = []
            if node == None: return result
            result.append(node.val)
            return_list_values(node.next, result=result)
            return result
        
        single_list = []
        for list in lists:
            single_list += return_list_values(list)
        single_list.sort()
       
        # Create new node
        head = ListNode(None)
        current = head
        for item in single_list:
            current.next = ListNode(item)
            current = current.next
        head = head.next
        return head