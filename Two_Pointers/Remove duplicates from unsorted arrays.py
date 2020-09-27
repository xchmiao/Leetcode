class Solution:

    # time complexity O(nlogn), space complexity O(1)
    def removeDuplicatesI(self, nums: List[int]) -> None:

        if not nums:
            return 0

        # O(nlogn)
        nums.sort()
        left, right = 0, 1
        while right < len(nums):
            while right < len(nums) and nums[left] == nums[right]:
                right += 1

            if right < len(nums):
                left += 1
                nums[left] = nums[right]
                right += 1

        return left + 1


    # time complexity O(n), space complexity O(n)
    def removeDuplicatesII(self, nums: List[int]) -> None:

        if not nums:
            return 0

        uniques = set()
        for i in range(len(nums)):
            uniques.add(nums[i])

        for i in range(len(uniques)):
            nums[i] = uniques[i]

        return len(uniques)

