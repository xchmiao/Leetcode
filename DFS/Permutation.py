class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None:
            return []

        visited = [False] * len(nums)
        permutations = []

        self.dfs(nums, visited, [], permutations)

        return permutations


    def dfs(self, nums, visited, permutation, permutations):
        if len(permutation) == len(nums):
            permutations.append(list(permutation)) # deep copy
            return 

        for i in range(len(nums)):
            if visited[i]:
                continue

            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, visited, permutation, permutations)
            visited[i] = False
            permutation.pop()
