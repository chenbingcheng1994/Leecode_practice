#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


        # for i in range(len(list2)):
        #     list1.append(list2[i])
        # list1.sort()
        # return list1
# @lc code=end

if __name__ == "__main__":
    l1 = [1,2,4]
    l2 = [1,3,4]
    Solution().mergeTwoLists(ListNode(l1), ListNode(l2))
