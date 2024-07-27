# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        heap = []

        for index, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, index, node))

        tmp = ListNode(0)
        curr = tmp

        while heap:
            val,index,node = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if node.next:
                heappush(heap, (node.next.val, index, node.next))

        return tmp.next
        
        