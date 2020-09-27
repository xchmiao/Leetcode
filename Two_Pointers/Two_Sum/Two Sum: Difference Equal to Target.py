class Solution:
    """
    @param nums: an array of integers
    @param target: an integer
    @return an array of integers

    [Description] 
    1. Sort input array in ascending order
    2. Have two pointers (left, right) moving in the same direction 
        Loop over left from 0 to len(nums) - 2
         - right = max(right, left + 1)
         - while right < len(nums) and  nums[right] - nums[left] < target: right++ 
         - If right is moving out of the range, break the loop 
         - If nums[right] - nums[left] == target: return answer
         - else: left++
    """ 

    def twoSumDiff(self, nums: List[int], target: int) -> List[int]:

        if not nums or len(nums) < 2:
            return []

        target = abs(target)

        nums = sorted(nums)
        left, right = 0, 1
        while left < len(nums) - 1:
            # right doesn't need to start from left + 1
            right = max(left + 1, right)
            while right < len(nums) and nums[right] - nums[left] < target :
                right += 1
            if right >= len(nums):
                break
            if nums[right] - nums[right] == target:
                return [nums[left], nums[right]]
            else:
                left += 1

        return []
