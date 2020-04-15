# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Example:
#       Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#       Output: 7 -> 0 -> 8
#       Explanation: 342 + 465 = 807.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        x = self.next
        y = self.val
        result = []
        while True :
            result.append(y)
            if x is not None:
                y = x.val
                x = x.next
            else :
                break
        return str(result)

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    if (l1 is None) and (l2 is None) :
        result = None
    else :
        a = 0 if l1 is None else l1.val
        b = 0 if l2 is None else l2.val
        tem = a + b
        result = ListNode(tem % 10)
        n1 = None if l1 is None else l1.next
        n2 = None if l2 is None else l2.next
        result.next = addTwoNumbers(n1, n2)
        if (tp := tem // 10) :
            result.next = addTwoNumbers(result.next, ListNode(tp))
    return result