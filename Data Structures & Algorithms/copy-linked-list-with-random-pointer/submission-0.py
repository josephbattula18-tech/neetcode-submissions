"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        otn={}
        curr = head
        while curr :
            otn[curr]=Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            otn[curr].next=otn.get(curr.next)
            otn[curr].random=otn.get(curr.random)
            curr=curr.next
        return otn[head]