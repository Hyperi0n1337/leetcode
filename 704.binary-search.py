#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2  # Calculate the middle index
                mid_value = nums[mid]  # Get the middle element's value

                if mid_value == target:
                    return mid  # Found the target element; return its index
                elif mid_value < target:
                    left = mid + 1  # Target is in the right half of the list
                else:
                    right = mid - 1  # Target is in the left half of the list

            return -1  # Target element not found; return -1
# @lc code=end

