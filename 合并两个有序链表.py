# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(ListNode):
    def merge_two_list(self, l1, l2):
        if len(l1) == 0:
            return l2
        if len(l2) == 0:
            return l1
        if l1.val<l2.val:
            l1.next = self.merge_two_list(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_list(l1, l2.next)
            return l2

    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


print(Solution().mergeTwoLists([1, 2, 4], [1, 3, 4]))