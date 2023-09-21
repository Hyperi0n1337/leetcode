#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List = []
        Index_Step = 0
        FirstTerm = 0
        SecondTerm = 1
        FoundMatch = False
        while FoundMatch == False:
            for n in range(0,len(nums)-SecondTerm):
                    if nums[FirstTerm] + nums[SecondTerm+n] == target:
                        FoundMatch = True
                        if nums[FirstTerm] == nums[SecondTerm+n]:
                            List.append(nums.index(nums[FirstTerm]))
                            PartOfList = nums[nums.index(nums[FirstTerm])+1:]
                            List.append(PartOfList.index(nums[FirstTerm])+1+nums.index(nums[FirstTerm]))
                            return List
                            break
                        else:
                            List.append(nums.index(nums[FirstTerm]))
                            List.append(nums.index(nums[SecondTerm+n]))
                            return List
                            break
            FirstTerm += 1
            SecondTerm += 1
        
    
        
    

# @lc code=end