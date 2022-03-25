#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0][0]
        tmp_ans = []
        ans_list = []
        i = 0
        tmp = ""
        while True:
            for j in range(len(strs)):
                print(i,j)
                if len(strs[j]) < i+1:
                    return "".join(ans_list)
                if tmp != "" and tmp != strs[j][i]:
                    tmp = ""
                    if len(ans_list) < len(tmp_ans):
                        ans_list = tmp_ans
                    break
                tmp = strs[j][i]
            tmp_ans.append(tmp)
            i += 1

# @lc code=end
