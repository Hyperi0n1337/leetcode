#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []
        for i in s:
            if len(s)%2 != 0:
                return False
            elif len(Stack) == 0 and len(Stack) % 2 == 0 :
                Stack.append(i)
            elif (Stack[-1] == "(" and i == ")") or (Stack[-1] == "[" and i == "]") or (Stack[-1] == "{" and i == "}"):
                Stack.pop()
            elif (Stack[-1] == "(" and (i == "[" or "{")) or (Stack[-1] == "[" and (i == "(" or "{")) or (Stack[-1] == "{" and (i == "[" or "(")):
                Stack.append(i)
        if Stack == []:
            return True
        return False

# @lc code=end

