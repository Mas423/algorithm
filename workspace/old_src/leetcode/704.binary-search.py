#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        max = len(nums) - 1
        min = 0
        while min<=max:
            idx=(min+max) // 2
            if nums[idx] == target:
                return idx 
            if nums[idx] < target:
                min=idx+1
            else:
                max=idx-1
        return -1
# @lc code=end

