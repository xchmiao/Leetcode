class Solution:
    """
    @param nums: an array of integers
    @param target: an integer
    @return: integer
    """

    def twoSum(self, nums: List[int], target: int) -> int:

        if not nums or len(nums) < 2:
            return 0

        nums = sorted(nums)

        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += right - left
                left += 1

        return count
