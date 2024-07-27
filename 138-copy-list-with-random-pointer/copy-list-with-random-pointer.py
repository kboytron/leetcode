"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        
        # Step 1: Create new nodes and insert them after each original node
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Step 2: Set random pointers for the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Separate the new nodes to form the copied list
        current = head
        new_head = head.next
        while current:
            new_node = current.next
            current.next = new_node.next
            current = current.next
            if new_node.next:
                new_node.next = new_node.next.next
        
        return new_head
        