class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Convert linked list to array
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        
        # Reorder
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left].next = arr[right]
            left += 1
            if left == right:
                break
            arr[right].next = arr[left]
            right -= 1
        
        arr[left].next = None