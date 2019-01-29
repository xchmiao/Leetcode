
## solution - 1
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
            
        self.result = []
        self.search(sorted(nums), [], 0)
        
        return self.result
        
        
    def search(self, nums, S, index):
        
        if index == len(nums):
            self.result.append(list(S))
            return
        
        # select current element
        S.append(nums[index])
        self.search(nums, S, index + 1)
        
        # don't select current element
        S.pop()
        self.search(nums, S, index + 1)


## solution - 2：更为通用的版本

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        subsets = []
        
        if nums is None:
            return subsets
            
        nums = sorted(nums)
        self.dfs(nums, 0, [], subsets)
        return subsets
        
    def dfs(self, nums, start_index, subset, subsets):
        
        subsets.append(list(subset))
        
        for i in range(start_index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()
        
# class Solution:
#     """
#     @param nums: A set of numbers
#     @return: A list of lists
#     """
#     def subsets(self, nums):
#         # write your code here
#         self.result = []

#         if nums is None:
#             return self.result

#         nums = sorted(nums)
#         self.dfs(nums, 0, [])

#         return self.result


#     def dfs(self, nums, start_index, subset):

#         self.result.append(list(subset)) # deep copy, since subset will be changed in the following for-loop

#         for i in range(start_index, len(nums)):
#             # [1] => [1, 2]
#             subset.append(nums[i])
#             self.dfs(nums, i + 1, subset)
#             # [1, 2] => [1], back-tracking
#             subset.pop()


#     def dfs(self, nums, start_index, subset):

#         self.result.append(subset)
#         for i in range(start_index, len(nums)):
#             self.dfs(nums, i + 1, subset + [nums[i]])


## Solution-3 use bit manipulation

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here

        result = []
        if nums is None:
            return None

        numsn = sorted(nums)
        n = len(nums)

        for i in range(i << n): # i << n is equal to 2^n, the range is from 0 to 2^n - 1
            subset = []
            for j in range(n):
                if (i & (1 << j) != 0): # and with 001, 010, 100 to find which nums[j] should be included in the subset
                    subset.append(nums[j])
            result.append(subset)

        return result


## Solution-4: BFS

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        from collections import deque

        result = []
        if nums is None:
            return None

        nums.sort()

        q = deque([[]])

        while q:
            subset = q.popleft()
            result.append(subset)

            for i in range(len(nums)):
                if not subset or subset[-1] < nums[i]:
                    next_subset = list(subset)
                    next_subset.append(nums[i])
                    q.append(next_subset)

        return result

        














