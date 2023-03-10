#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        alpha = []
        for i in s:
            if i not in alpha and s.count(i) != t.count(i):
                return False
            alpha.append(i)
        return True
# @lc code=end
