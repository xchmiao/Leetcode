## Given a sorted array nums, and a target number,
## if target is in nums, return it's index, otherwise return -1

## Interative solution

class Solution:
	def binarySearch(self, nums, target):
		if len(nums) == 0:
			return -1

		start, end = 0, len(nums) - 1

        # start <= end ensure to find the target item is the last element
		while (start <= end):
			mid = (start + end)/2
			if nums[mid] == target:
				return mid
			if nums[mid] < target:
				start = mid + 1
			else:
				end = mid - 1

		return -1


## Recursive solution

class Solution:
	def binarySearch(self, nums, target):
		# if len(nums) == 0:
		# 	return -1
		start, end = 0, len(nums) - 1
		return self._findTarget(nums, start, end, target)

	def _findTarget(self, nums, start, end, target):
		if start > end:
			return -1

		mid = (start + end)/2
		if nums[mid] == target:
			return mid
		if nums[mid] < target:
			return self._findTarget(nums, mid + 1, end, target)
		return self._findTarget(nums, start, mid - 1, target)
