
'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        tmp = ListNode(0)
        res = tmp
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            sum = v1 + v2 + carry
            sum, carry = sum % 10, sum // 10

            tmp.next = ListNode(sum)
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            tmp = tmp.next

        return res.next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None   

l1 = ListNode(7)
l1.next = ListNode(8)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)

l2 = ListNode(9)

l2.next = ListNode(3)
l2.next.next = ListNode(5)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(0)
l2.next.next.next.next.next = ListNode(9)
l2.next.next.next.next.next.next = ListNode(2)
l2.next.next.next.next.next.next.next = ListNode(1)



sol = Solution()
res = sol.addTwoNumbers(l1, l2)

while res:
    print(res.val)
    res = res.next