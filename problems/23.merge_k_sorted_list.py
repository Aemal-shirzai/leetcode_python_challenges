from typing import Optional, List

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

# Test Case
  
# node1 = ListNode(1)
# node2 = ListNode(4)
# node3 = ListNode(5)
# node1.next = node2
# node2.next = node3

# node4 = ListNode(1)
# node5 = ListNode(3)
# node6 = ListNode(4)
# node4.next = node5
# node5.next = node6

# node7 = ListNode(2)
# node8 = ListNode(6)
# node7.next = node8

# obj = Solution()
# obj.mergeKLists([node1, node4, node7])