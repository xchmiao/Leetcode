class Solution:
    """
    @param nums: an array of integers
    @param target: an integer
    @return: an integer
    """
    def twoSumClosest(self, nums: List[int], target: int) -> int:

        if not nums or len(nums) == 1:
            return -1

        nums = sorted(nums)
        left, right = 0, len(nums) - 1

        min_delta = - (1 << 31)

        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                return 0
            elif two_sum > target:
                min_delta = min(abs(two_sum - target), min_delta)
                right -= 1
            else:
                min_delta = min(abs(two_sum - target), min_delta)
                left += 1

        return min_delta
