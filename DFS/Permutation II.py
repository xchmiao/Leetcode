class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if nums is None:
            return []

        visited = [False] * len(nums)
        permutations = []
        
        nums = sorted(nums) # don't forget to sort nums
        self.dfs(nums, visited, [], permutations)

        return permutations


    def dfs(self, nums, visited, permutation, permutations):
        if len(permutation) == len(nums):
            permutations.append(list(permutation)) # deep copy
            return 

        for i in range(len(nums)):
            if visited[i]:
                continue 
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, visited, permutation, permutations)
            visited[i] = False
            permutation.pop()
