
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Since the array is already sorted, we can keep two pointers i and k, where ii is the slow-runner while jj is the fast-runner. 
        As long as nums[i] = nums[k], we increment k to skip the duplicate; 
        else the duplicate run has ended, so increase i by 1 and then copy its value to nums[i]

        """
        if len(nums) <= 1:
            return len(nums)
        else:
            i = 0
            for k in range(1, len(nums)):
                if nums[k] != nums[i]:
                    i = i+1
                    nums[i] = nums[k]
            return i+1
