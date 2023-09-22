#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_list = list(s)
            t_list = list(t)
            for i,v in enumerate(s_list[:]):
                if v in t_list:
                    t_list.remove(v)
                    if t_list == []:
                        return True
        return False
# @lc code=end

