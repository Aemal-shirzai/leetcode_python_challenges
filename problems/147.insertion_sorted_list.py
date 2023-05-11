from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def return_list_values(node, result=None):
            if not result: result = []
            if node == None: return result
            result.append(node.val)
            return_list_values(node.next, result=result)
            return result
        
        single_list = return_list_values(head)
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
  
# head = ListNode(-1)
# node2 = ListNode(5)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(0)
# head.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# obj = Solution()
# obj.mergeKLists(head)