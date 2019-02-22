class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        self.quick_sort(A, 0, len(A) - 1)

    def quick_sort(self, A, start, end):
    	if start >= end:
    		return

    	left, right = start, end
    	pivot = A[(start + end) // 2]

    	while left <= right:
    		while left <= right and A[left] < pivot:
    			left += 1
    		while left <= right and A[right] > pivot:
    			right -= 1

    		if left <= right:
    			A[left], A[right] = A[right], A[left]
    			left += 1
    			right -= 1
    			
    	# When the while loop stops, right = left - 1
    	quick_sort(self, A, start, right)
    	quick_sort(self, A, left, end)
