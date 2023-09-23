#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        List = []
        for n in range(1,n+1):
            if n%3 == 0 and n%5 == 0:
                List.append("FizzBuzz")
            elif n%3 == 0 and not n%5 == 0:
                List.append("Fizz")
            elif n%5 == 0 and not n%3 == 0:
                List.append("Buzz")
            else:
                List.append(str(n))
        return List

        
# @lc code=end

