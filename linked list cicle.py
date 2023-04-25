#%%
# https://leetcode.com/problems/linked-list-cycle/
# O(n2) solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#6% 41%
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        lst = [] #Visited nodes
        while curr:
            if curr in lst:#If already visited, return true
                return True
            lst.append(curr)
            curr = curr.next
        return False


#%%

#O(n) solution
# two pointers
# Walk two nodes on each iteraction on second pointer
#If it reaches frist pointer, than there is a loop
# 80% 67%
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        p1 = head
        if head:
            p2 = head.next
        else:
            return False
        
        while p1:
            if p1 == p2:
                return True            
            if p2 and p2.next and p2.next.next:
                p2 = p2.next.next
            else:
                return False
            p1 = p1.next
        return False
