"""
Two Sum - Greater than target
"""

class Solution:
    """
    @param nums: an array of integers
    @param target: an integer
    @return: integer
    """
    
    def twoSumGreaterThanTarget(self, nums: List[int], target: int) -> int:
        
        if not nums or len(nums) <= 1:
            return 0
        
        nums = sorted(nums)
        
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] > target:
                count += right - left
                right -= 1
            else:
                left += 1
       return count
