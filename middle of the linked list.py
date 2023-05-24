# https://leetcode.com/problems/middle-of-the-linked-list/
# 25% 57%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        middle_node = head
        this_node = head
        update_middle = True

        while this_node.next:
            this_node = this_node.next
            if update_middle:
                middle_node = middle_node.next
            update_middle = not update_middle
        return middle_node