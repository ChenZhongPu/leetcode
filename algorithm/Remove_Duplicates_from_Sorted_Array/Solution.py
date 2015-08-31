class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        if len(nums) == 1:
        	return 1
        j = 0
        n = len(nums)
        for i in range(1, n):
        	if nums[i] != nums[j]:
        		nums[j+1] = nums[i]
        		j += 1
        return j + 1