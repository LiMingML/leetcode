"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        O(n) time and O(1) space.
        Because it is in O(1) space, we can not reverse
        the list totally.
        :param head:
        :return:
        """
        # Base case.
        if head is None or head.next is None:
            return True

        slow = head
        fast = head
        prev = None

        # find the medium node or nodes
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        medium_right = slow.next

        # cut the linked list into two
        if fast.next is None:
            # if medium left == medium right
            # there is no need to compare them
            prev.next = None
        elif fast.next.next is None:
            slow.next = None

        # reverse the left linked list
        medium_left = self.reverseList(head)

        # judge the palindrome
        while medium_left and medium_right:
            if medium_left.val != medium_right.val:
                return False
            medium_left = medium_left.next
            medium_right = medium_right.next

        return True

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev



