# https://leetcode.com/problems/reverse-linked-list/

#%%
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_linked_list(head):
    node_head = node = ListNode(head[0])
    for i in head[1:]:
        node.next = ListNode(i)
        node = node.next
    return node_head

def print_ll(ll):
    current = ll
    while current:
        print(current.val,end=' => ')
        current = current.next
    print(' None')

#%%
# Recursive version
# 55% 5%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse_ll(head)
    def reverse_ll(self,node, prev = None):    
        
        if node is None:
            # print('fim')
            # print_ll(prev)
            return prev
        
        next = node.next
        node.next = prev    
        # print_ll(node)
        return self.reverse_ll(next,node)




#%%


#%%%
# Iterative version
#13% 79%

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            
            temp  = head.next
            
            head.next = prev
            
            prev = head
            
            head = temp
        return prev



#%%
