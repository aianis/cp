"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""
head = [1,2,3,4,5,6] 
class Solution:
    def middleNode(self, head):        # 1. Find the length of the linked list
        slow = head 
        fast = head 

        while fast and fast.next:       # 2. Move the fast pointer to the end of the linked list 
            slow = slow.next            # 3. Move the slow pointer to the middle of the linked list 
            fast = fast.next.next       # 4. Return the slow pointer 
        return slow 
    

