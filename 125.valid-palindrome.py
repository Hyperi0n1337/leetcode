#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
 
        trimmed_s = re.sub(r'[\W_]', '', s) #retain only alphanumeric,
        trimmed_s1 = trimmed_s.lower() # convert to lowercase and list
        if trimmed_s1 == trimmed_s1[::-1]: # if the reversed is equal to the string, then its a palindrome
            return True
        return False
# @lc code=end

