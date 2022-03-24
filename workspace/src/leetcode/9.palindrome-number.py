#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        print(str(x))
        str_x = str(x)
        list = []
        for c in reversed(str_x):
            list.append(c)
        if str_x == "".join(list):
            return True
# @lc code=end

